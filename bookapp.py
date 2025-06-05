from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bhoomi90@#'       # strong secret in production!

# In-memory "databases"
users = {}
books = {}
book_id_counter = 1

# Decorator to verify JWT token and get user info
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Bearer <token>
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(data['username'])
            if not current_user:
                raise Exception('User not found')
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # default role user

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    
    hashed_pw = generate_password_hash(password)
    users[username] = {'password': hashed_pw, 'role': role}
    return jsonify({'message': f'User {username} registered successfully!'}), 201

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    
    return jsonify({'token': token})

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values()))

# Get book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = books.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify(book)

# Add a new book (admin only)
@app.route('/books', methods=['POST'])
@token_required
def add_book(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Admin privilege required'}), 403
    
    global book_id_counter
    data = request.json
    title = data.get('title')
    author = data.get('author')
    if not title or not author:
        return jsonify({'message': 'Title and author required'}), 400
    
    book = {'id': book_id_counter, 'title': title, 'author': author}
    books[book_id_counter] = book
    book_id_counter += 1
    
    return jsonify(book), 201

# Update book (admin only)
@app.route('/books/<int:id>', methods=['PUT'])
@token_required
def update_book(current_user, id):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Admin privilege required'}), 403
    
    book = books.get(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    data = request.json
    title = data.get('title')
    author = data.get('author')
    
    if title:
        book['title'] = title
    if author:
        book['author'] = author
    
    books[id] = book
    return jsonify(book)

# Delete book (admin only)
@app.route('/books/<int:id>', methods=['DELETE'])
@token_required
def delete_book(current_user, id):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Admin privilege required'}), 403
    
    if id not in books:
        return jsonify({'message': 'Book not found'}), 404
    
    del books[id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    print("Starting Book Library API...")
    print("API will run on: http://localhost:5001")
    print("Press Ctrl+C to stop the server")
    print("Test the API by going to: http://localhost:5001/books")
    app.run(debug=True, port=5001)
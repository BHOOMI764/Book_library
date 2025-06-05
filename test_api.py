import requests
import json
import time

BASE_URL = "http://localhost:5001"

def test_api():
    print("=" * 50)
    print("TESTING BOOK LIBRARY API")
    print("=" * 50)
    
    # Wait a moment for server to be ready
    print("Waiting for server to be ready...")
    time.sleep(2)
    
    try:
        # Test 1: Register admin user
        print("\n🔹 TEST 1: Registering admin user...")
        register_data = {
            "username": "admin",
            "password": "admin123",
            "role": "admin"
        }
        response = requests.post(f"{BASE_URL}/register", json=register_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 201:
            print("✅ Registration successful!")
        else:
            print("❌ Registration failed!")
            return
        
        # Test 2: Login
        print("\n🔹 TEST 2: Logging in...")
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            token = response.json()['token']
            print("✅ Login successful!")
            print(f"Token received: {token[:50]}...")
            
            # Test 3: Add first book
            print("\n🔹 TEST 3: Adding first book...")
            headers = {"Authorization": f"Bearer {token}"}
            book_data = {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald"
            }
            response = requests.post(f"{BASE_URL}/books", json=book_data, headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
            
            if response.status_code == 201:
                print("✅ Book added successfully!")
            else:
                print("❌ Failed to add book!")
            
            # Test 4: Add second book
            print("\n🔹 TEST 4: Adding second book...")
            book_data = {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee"
            }
            response = requests.post(f"{BASE_URL}/books", json=book_data, headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
            
            # Test 5: Get all books
            print("\n🔹 TEST 5: Getting all books...")
            response = requests.get(f"{BASE_URL}/books")
            print(f"Status: {response.status_code}")
            books_list = response.json()
            print(f"Number of books: {len(books_list)}")
            for book in books_list:
                print(f"  - {book['title']} by {book['author']} (ID: {book['id']})")
            
            if response.status_code == 200:
                print("✅ Successfully retrieved all books!")
            
            # Test 6: Get book by ID
            print("\n🔹 TEST 6: Getting book by ID (1)...")
            response = requests.get(f"{BASE_URL}/books/1")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                book = response.json()
                print(f"Book found: {book['title']} by {book['author']}")
                print("✅ Successfully retrieved book by ID!")
            else:
                print("❌ Failed to get book by ID!")
            
            # Test 7: Update book
            print("\n🔹 TEST 7: Updating book...")
            update_data = {
                "title": "The Great Gatsby - Updated Edition"
            }
            response = requests.put(f"{BASE_URL}/books/1", json=update_data, headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                updated_book = response.json()
                print(f"Updated book: {updated_book['title']}")
                print("✅ Book updated successfully!")
            else:
                print("❌ Failed to update book!")
            
            # Test 8: Try to access without token (should fail)
            print("\n🔹 TEST 8: Testing security (no token)...")
            book_data = {
                "title": "Unauthorized Book",
                "author": "Hacker"
            }
            response = requests.post(f"{BASE_URL}/books", json=book_data)
            print(f"Status: {response.status_code}")
            if response.status_code == 401:
                print("✅ Security working! Unauthorized access blocked.")
            else:
                print("❌ Security issue! Unauthorized access allowed.")
        
        else:
            print("❌ Login failed!")
            print(f"Response: {response.json()}")
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the server!")
        print("Make sure your Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
    
    print("\n" + "=" * 50)
    print("TESTING COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    test_api()
const express = require('express');
const app = express();
const port = 8080;

app.use(express.json());

// Dummy in-memory user object
let user = {
  name: 'John Doe',
  age: 30,
  email: 'bhom@gmail.com'
};

// ✅ GET - Read user
app.get('/user', (req, res) => {
  res.json(user);
});

// ✅ POST - Create a new user (replaces existing one)
app.post('/user', (req, res) => {
  user = req.body;
  res.status(201).json(user);  // just send the created user directly
});

// ✅ PUT - Replace entire user object
app.put('/user', (req, res) => {
  user = req.body;
  res.json(user);
});

// ✅ PATCH - Update part of the user object
app.patch('/user', (req, res) => {
  user = { ...user, ...req.body };  // merge new data with old
  res.json(user);
});

// ✅ DELETE - Remove user object
app.delete('/user', (req, res) => {
  user = {};  // reset to empty
  res.json(user);  // return the empty object
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

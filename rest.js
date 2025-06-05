const express = require('express');
const app = express();
const port = 8080;

app.use(express.json());

let user = {
  name: 'John Doe',
  age: 30,
  email: 'bhom@gmail.com'
};

app.get('/user', (req, res) => {
  res.json(user);
});


app.post('/user', (req, res) => {
  user = req.body;
  res.status(201).json(user);  
});

app.put('/user', (req, res) => {
  user = req.body;
  res.json(user);
});

app.patch('/user', (req, res) => {
  user = { ...user, ...req.body };  
  res.json(user);
});

app.delete('/user', (req, res) => {
  user = {};  
  res.json(user);  
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello from the Node.js frontend!');
});

app.listen(PORT, () => {
  console.log(`Frontend app listening at http://localhost:${PORT}`);
});

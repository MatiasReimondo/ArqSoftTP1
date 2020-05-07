const express = require('express');

const PORT = 3000;
const LOOP = 500;
const TIMEOUT = 5000;
const app = express();

app.get('/', (req, res) => {
  res.status(200).send('node - ping');
});

app.get('/timeout', (req, res) => {
  setTimeout(() => {
    res.status(200).send('node - timeout');
  }, TIMEOUT);
});

app.get('/heavy', (req, res) => {
  let start = new Date();

  for (;;) {
    let now = new Date();

    if (now - start >= LOOP) {
      break;
    }
  }

  res.status(200).send('node - heavy');
});

app.listen(PORT, "0.0.0.0", 1024, () => {
  console.log('Escuchando en el puerto', PORT);
});

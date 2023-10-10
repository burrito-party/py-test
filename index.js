// Just adding this so we can enable Default Setup for JS
console.log(":)")

const express = require('express');

const app = express();
app.get('/', (req, res) => res.send(`Hello, ${req.query.name}!`));

console.log("hello")

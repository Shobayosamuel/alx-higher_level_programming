#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, inputD) => {
  if (err) {
    console.log(err);
  } else {
    console.log(inputD.toString());
  }
});

#!/usr/bin/node
const fs = require('fs');
const [arg1, arg2, arg3] = process.argv.slice(2);
const f1 = fs.readFileSync(arg1, 'utf-8');
const f2 = fs.readFileSync(arg2, 'utf-8');
const conCat = f1 + f2;
fs.writeFileSync(arg3, conCat);

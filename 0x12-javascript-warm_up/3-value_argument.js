#!/usr/bin/node
const len = process.argv.length - 2;
const vals = process.argv;
if (len === 0) console.log('No argument');
else console.log(vals[2]);

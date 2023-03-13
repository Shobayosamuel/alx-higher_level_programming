#!/usr/bin/node
const [,, arg1, arg2] = process.argv;
const first = parseInt(arg1);
const sec = parseInt(arg2);
function add (a, b) {
  return a + b;
}
console.log(add(first, sec));

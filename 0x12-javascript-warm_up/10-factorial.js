#!/usr/bin/node
const [,, arg] = process.argv;
const number = parseInt(arg);
function fact (num) {
  if (isNaN(num)) return 1;
  if (num <= 0) return 1;
  return (num * fact(num - 1));
}
console.log(fact(number));

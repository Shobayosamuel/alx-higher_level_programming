#!/usr/bin/node
const [,, arg] = process.argv;
const num = parseInt(arg);
if (isNaN(num)) console.log('Missing size');
else for (let i = 0; i < num; i++) console.log('X'.repeat(num));

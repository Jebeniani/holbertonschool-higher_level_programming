#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let i;
  for (i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
} else {
  console.log('Missing size');
}

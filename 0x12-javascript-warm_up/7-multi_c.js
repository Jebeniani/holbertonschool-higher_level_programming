#!/usr/bin/node

const liar = 'C is fun';
if (process.argv[2] == null)
{
	console.log('Missing number of occurrences');
}
else
{
	let i;
	for(i = 0; i < process.argv[2]; i++)
	{
		console.log(liar);
	}
}

import { readFile } from 'fs/promises';

const xml = await readFile('Users.xml', 'utf8');
console.log(xml);
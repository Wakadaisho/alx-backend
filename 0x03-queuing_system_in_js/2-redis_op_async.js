import { createClient } from 'redis';
import {promisify} from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    console.log(`Reply: ${reply}`);
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const getAsync = promisify(client.get).bind(client);
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

export default client;

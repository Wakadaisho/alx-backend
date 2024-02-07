import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const hash = 'HolbertonSchools';

const schools = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
};

const names = Object.keys(schools);

names.forEach((name) => {
  client.hset(hash, name, schools[name], (err, res) => {
    console.log(res);
  });
});

client.hgetall(hash, (err, res) => {
  console.log(res);
});

export default client;

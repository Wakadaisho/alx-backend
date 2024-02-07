import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

function reserveSeat(number){
   client.set('available_seats', number, (err, reply) => {
     console.log(`Available seats: ${reply}`);
   });
}

async function getCurrentAvailableSeats(){
    const getAsync = promisify(client.get).bind(client);
    const reply = getAsync('available_seats');
    return reply;
}

reserveSeat(50);
getCurrentAvailableSeats();

export default client;

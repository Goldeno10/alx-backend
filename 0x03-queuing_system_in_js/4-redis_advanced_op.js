import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});


const hashKey = 'HolbertonSchools';
const hashData = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

client.hset(hashKey, hashData, client.print);

client.hgetall(hashKey, (err, reply) => {
  if (err) {
    console.error(`Error getting hash: ${err.message}`);
  } else {
    console.log('Hash data:');
    console.log(reply);
  }
});

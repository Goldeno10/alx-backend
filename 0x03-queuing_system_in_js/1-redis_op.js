import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (ERROR_MESSAGE) => {
  console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`);
});

await client.connect();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for key ${schoolName}: ${err.message}`);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
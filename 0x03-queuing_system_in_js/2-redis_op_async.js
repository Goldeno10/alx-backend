import { createClient } from "redis";
import util from 'util';


const client = createClient();

const getAsync = util.promisify(client.get).bind(client);


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

await client.connect();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, client.print);
}

async function displaySchoolValue(schoolName) {
    try {
      const reply = await getAsync(schoolName);
      console.log(`Value for ${schoolName}: ${reply}`);
    } catch (err) {
      console.error(`Error getting value for key ${schoolName}: ${err.message}`);
    }
  }

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  }
  
main();
  
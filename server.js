const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();

// MongoDB Atlas connection string (replace <password> and <dbname> with your actual details

const uri = 'mongodb+srv://arnavgupta0078:arnav@cluster3301.ojyvd.mongodb.net/?retryWrites=true&w=majority';

// Create a MongoClient instance
const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define a route to test the connection
app.get('/', async (req, res) => {
    try {
        await client.connect(); // Connect to MongoDB Atlas
        const database = client.db('PdoXDB'); // Use the desired database name
        const collection = database.collection('users'); // Use the desired collection name

        // Example: Find all users
        const users = await collection.find().toArray();

        res.send(users); // Send users as response
    } catch (error) {
        console.error(error);
        res.status(500).send('Error connecting to the database');
    } finally {
        await client.close(); // Close the connection
    }
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
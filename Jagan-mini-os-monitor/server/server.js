//  packages importing
const express = require('express');
const cors = require('cors');
const si = require('systeminformation');

// Created an Express app
const app = express();

// Middleware sett
app.use(cors());

// Testing routes
app.get('/', async (req, res) => {
    try {
        const cpu = await si.cpu();

        res.json({
            message: 'Mini OS Monitor Server is running!',
            cpu: cpu.manufacturer + ' ' + cpu.brand
        });
    } catch (error) {
        res.status(500).json({
            error: error.message
        });
    }
});

// Server Port
const PORT = 3000;


app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
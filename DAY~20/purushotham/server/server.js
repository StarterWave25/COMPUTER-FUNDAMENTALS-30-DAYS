const express = require('express');
const path = require('path');
const cpuRouter = require('./routes/cpu');
const memoryRouter = require('./routes/memory');
const processRouter = require('./routes/process');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON payloads
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static frontend files from the "client" directory
app.use(express.static(path.join(__dirname, '../client')));

// Wire up API routes
app.use('/cpu', cpuRouter);
app.use('/memory', memoryRouter);
app.use('/', processRouter); // Handles GET /processes and POST /process/kill

// Route fallback for client-side routing, serving index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/index.html'));
});

// Start listening for connections
app.listen(PORT, () => {
  console.log(`=========================================`);
  console.log(`  MiniOS Monitor Server is online!       `);
  console.log(`  URL: http://localhost:${PORT}          `);
  console.log(`  Press Ctrl+C to shut down.             `);
  console.log(`=========================================`);
});

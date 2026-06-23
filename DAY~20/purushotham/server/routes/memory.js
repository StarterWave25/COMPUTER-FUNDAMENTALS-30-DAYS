const express = require('express');
const router = express.Router();
const memoryService = require('../services/memoryService');

// Handles GET /memory
router.get('/', async (req, res) => {
  try {
    const data = await memoryService.getMemoryData();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve memory system metrics' });
  }
});

module.exports = router;

const express = require('express');
const router = express.Router();
const cpuService = require('../services/cpuService');

// Handles GET /cpu
router.get('/', async (req, res) => {
  try {
    const data = await cpuService.getCpuData();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve CPU system metrics' });
  }
});

module.exports = router;

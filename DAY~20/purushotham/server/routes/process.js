const express = require('express');
const router = express.Router();
const processService = require('../services/processService');

// Handles GET /processes
router.get('/processes', async (req, res) => {
  try {
    const data = await processService.getProcessesData();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to retrieve running processes' });
  }
});

// Handles POST /process/kill
router.post('/process/kill', async (req, res) => {
  const { pid } = req.body;
  
  if (!pid && pid !== 0) {
    return res.status(400).json({ error: 'Process ID (pid) is required.' });
  }

  const pidNum = Number(pid);
  if (isNaN(pidNum)) {
    return res.status(400).json({ error: 'Invalid Process ID format.' });
  }

  try {
    await processService.killProcess(pidNum);
    res.json({ success: true, message: `Process with PID ${pidNum} was terminated.` });
  } catch (error) {
    console.error(`Error terminating process ${pidNum}:`, error);
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;

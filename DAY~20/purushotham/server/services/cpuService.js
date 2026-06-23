const si = require('systeminformation');

/**
 * Fetches current CPU details and utilization.
 * @returns {Promise<Object>} Object containing model, cores, speed (GHz), and currentUsage (%)
 */
async function getCpuData() {
  try {
    const [cpuInfo, loadInfo] = await Promise.all([
      si.cpu(),
      si.currentLoad()
    ]);

    return {
      model: `${cpuInfo.manufacturer} ${cpuInfo.brand}`,
      cores: cpuInfo.cores,
      speed: cpuInfo.speed, // Speed in GHz
      currentUsage: Math.round(loadInfo.currentLoad * 100) / 100 // Round to 2 decimal places
    };
  } catch (error) {
    console.error('Error fetching CPU data:', error);
    throw error;
  }
}

module.exports = {
  getCpuData
};

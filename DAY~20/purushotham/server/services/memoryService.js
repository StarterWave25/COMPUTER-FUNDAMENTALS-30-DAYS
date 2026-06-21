const si = require('systeminformation');

/**
 * Fetches current system memory utilization.
 * @returns {Promise<Object>} Object containing total, used, free, and usagePercent.
 */
async function getMemoryData() {
  try {
    const memInfo = await si.mem();

    // In systeminformation, memInfo.active or memInfo.used represents actual RAM in use.
    // memInfo.used matches the traditional calculation: total - free - buffers - cache.
    const total = memInfo.total;
    const free = memInfo.available; // available is memory that can be allocated
    const used = total - free;
    const usagePercent = Math.round((used / total) * 100 * 100) / 100;

    return {
      total,
      used,
      free,
      usagePercent
    };
  } catch (error) {
    console.error('Error fetching memory data:', error);
    throw error;
  }
}

module.exports = {
  getMemoryData
};

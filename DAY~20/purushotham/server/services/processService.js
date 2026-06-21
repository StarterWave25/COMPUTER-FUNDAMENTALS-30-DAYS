const si = require('systeminformation');
const ps = require('ps-node');

/**
 * Retrieves the list of running processes with CPU and Memory utilization.
 * @returns {Promise<Array>} Array of process objects.
 */
async function getProcessesData() {
  try {
    const processes = await si.processes();
    
    // Map list to a clean structure, ensuring numbers are formatted nicely
    return processes.list.map(proc => ({
      pid: proc.pid,
      name: proc.name,
      cpu: Math.round(proc.cpu * 100) / 100, // round to 2 decimal places
      mem: Math.round(proc.mem * 100) / 100  // round to 2 decimal places
    }));
  } catch (error) {
    console.error('Error fetching processes:', error);
    throw error;
  }
}

/**
 * Terminates a process by its PID.
 * @param {number} pid - Process ID to terminate.
 * @returns {Promise<void>} Resolves if process is terminated, rejects on error.
 */
function killProcess(pid) {
  return new Promise((resolve, reject) => {
    if (!pid || isNaN(pid)) {
      return reject(new Error('Invalid PID provided.'));
    }

    ps.kill(pid, { signal: 'SIGKILL' }, (err) => {
      if (err) {
        // If ps-node fails, we can fall back to Node's native process.kill as a safety net
        try {
          process.kill(pid, 'SIGKILL');
          console.log(`Fallback kill succeeded for PID ${pid}`);
          return resolve();
        } catch (nativeErr) {
          console.error(`Failed to kill process ${pid}:`, err, nativeErr);
          return reject(new Error(`Failed to kill process with PID ${pid}. It may not exist or requires admin permissions.`));
        }
      }
      console.log(`Successfully killed PID ${pid} via ps-node.`);
      resolve();
    });
  });
}

module.exports = {
  getProcessesData,
  killProcess
};

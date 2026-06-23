// ==========================================================================
// CONFIGURATION & GLOBAL STATE
// ==========================================================================
const POLL_INTERVAL_METRICS = 2000;    // Poll CPU & RAM every 2 seconds
const POLL_INTERVAL_PROCESSES = 5000;  // Poll process list every 5 seconds

let allProcesses = [];
let sortKey = 'cpu';      // Default sort by CPU Usage
let sortOrder = 'desc';    // Default sort order is descending
let searchQuery = '';

// ==========================================================================
// INITIALIZATION
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  initMetricsPolling();
  initProcessPolling();
  setupEventListeners();
});

// ==========================================================================
// DOM ELEMENT REFERENCES
// ==========================================================================
const cpuUsageVal = document.getElementById('cpu-usage-val');
const cpuRadialBar = document.getElementById('cpu-radial-bar');
const cpuModel = document.getElementById('cpu-model');
const cpuCores = document.getElementById('cpu-cores');
const cpuSpeed = document.getElementById('cpu-speed');

const memUsageVal = document.getElementById('mem-usage-val');
const memRadialBar = document.getElementById('mem-radial-bar');
const memTotal = document.getElementById('mem-total');
const memUsed = document.getElementById('mem-used');
const memFree = document.getElementById('mem-free');

const processSearch = document.getElementById('process-search');
const clearSearchBtn = document.getElementById('clear-search-btn');
const processCount = document.getElementById('process-count');
const processListBody = document.getElementById('process-list-body');
const toastContainer = document.getElementById('toast-container');

// ==========================================================================
// EVENT LISTENERS Setup
// ==========================================================================
function setupEventListeners() {
  // Search Input
  processSearch.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    clearSearchBtn.style.display = searchQuery ? 'block' : 'none';
    renderProcesses();
  });

  // Clear Search Button
  clearSearchBtn.addEventListener('click', () => {
    processSearch.value = '';
    searchQuery = '';
    clearSearchBtn.style.display = 'none';
    processSearch.focus();
    renderProcesses();
  });

  // Table Column Sorting
  const sortableHeaders = document.querySelectorAll('th.sortable');
  sortableHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const field = header.getAttribute('data-sort');
      
      // If we clicked the same column, toggle order. Otherwise, sort descending by default.
      if (sortKey === field) {
        sortOrder = (sortOrder === 'asc') ? 'desc' : 'asc';
      } else {
        sortKey = field;
        sortOrder = (field === 'name' || field === 'pid') ? 'asc' : 'desc'; // Text/IDs defaults to ASC, Metrics to DESC
      }

      // Update Header arrow indicators
      sortableHeaders.forEach(h => {
        h.classList.remove('active-sort', 'asc', 'desc');
        const icon = h.querySelector('i');
        if (icon) icon.className = 'fa-solid fa-sort';
      });

      header.classList.add('active-sort', sortOrder);
      const activeIcon = header.querySelector('i');
      if (activeIcon) {
        activeIcon.className = (sortOrder === 'asc') 
          ? 'fa-solid fa-sort-up' 
          : 'fa-solid fa-sort-down';
      }

      renderProcesses();
    });
  });
}

// ==========================================================================
// SYSTEM METRICS SERVICE CALLS (CPU & Memory)
// ==========================================================================
function initMetricsPolling() {
  // Fetch immediately
  fetchCpuMetrics();
  fetchMemoryMetrics();

  // Set interval
  setInterval(fetchCpuMetrics, POLL_INTERVAL_METRICS);
  setInterval(fetchMemoryMetrics, POLL_INTERVAL_METRICS);
}

async function fetchCpuMetrics() {
  try {
    const response = await fetch('/cpu');
    if (!response.ok) throw new Error('HTTP error fetching CPU data');
    const data = await response.json();
    
    // Update labels
    cpuModel.textContent = data.model || 'Unknown';
    cpuCores.textContent = data.cores || '--';
    cpuSpeed.textContent = data.speed ? `${data.speed} GHz` : '-- GHz';
    cpuUsageVal.textContent = `${data.currentUsage}%`;
    
    // Update Radial Progress (Circumference = 2 * PI * R where R=40 -> 251.2)
    const offset = 251.2 - (data.currentUsage / 100) * 251.2;
    cpuRadialBar.style.strokeDashoffset = offset;
  } catch (error) {
    console.error('Error in CPU metrics poller:', error);
  }
}

async function fetchMemoryMetrics() {
  try {
    const response = await fetch('/memory');
    if (!response.ok) throw new Error('HTTP error fetching Memory data');
    const data = await response.json();

    // Format bytes to GB
    const totalGB = (data.total / (1024 * 1024 * 1024)).toFixed(2);
    const usedGB = (data.used / (1024 * 1024 * 1024)).toFixed(2);
    const freeGB = (data.free / (1024 * 1024 * 1024)).toFixed(2);

    memTotal.textContent = `${totalGB} GB`;
    memUsed.textContent = `${usedGB} GB`;
    memFree.textContent = `${freeGB} GB`;
    memUsageVal.textContent = `${data.usagePercent}%`;

    // Update Radial Progress
    const offset = 251.2 - (data.usagePercent / 100) * 251.2;
    memRadialBar.style.strokeDashoffset = offset;
  } catch (error) {
    console.error('Error in Memory metrics poller:', error);
  }
}

// ==========================================================================
// PROCESS MONITOR SERVICE CALLS
// ==========================================================================
function initProcessPolling() {
  // Fetch immediately
  fetchProcesses();
  // Set interval
  setInterval(fetchProcesses, POLL_INTERVAL_PROCESSES);
}

async function fetchProcesses() {
  try {
    const response = await fetch('/processes');
    if (!response.ok) throw new Error('HTTP error fetching processes');
    const data = await response.json();
    
    allProcesses = data;
    renderProcesses();
  } catch (error) {
    console.error('Error in processes poller:', error);
    if (allProcesses.length === 0) {
      processListBody.innerHTML = `
        <tr>
          <td colspan="5" class="empty-state">
            <i class="fa-solid fa-triangle-exclamation" style="color: var(--danger-color); font-size: 1.25rem;"></i>
            <br>Failed to retrieve system processes. Make sure server is running.
          </td>
        </tr>
      `;
    }
  }
}

// ==========================================================================
// RENDERING & LOCAL FILTERING/SORTING
// ==========================================================================
function renderProcesses() {
  let filtered = [...allProcesses];

  // 1. Apply Search Filter
  if (searchQuery) {
    filtered = filtered.filter(proc => 
      proc.name.toLowerCase().includes(searchQuery) || 
      proc.pid.toString().includes(searchQuery)
    );
  }

  // 2. Apply Sorting
  filtered.sort((a, b) => {
    let valA = a[sortKey];
    let valB = b[sortKey];

    // Case insensitive sorting for process names
    if (typeof valA === 'string') {
      valA = valA.toLowerCase();
      valB = valB.toLowerCase();
    }

    if (valA < valB) return (sortOrder === 'asc') ? -1 : 1;
    if (valA > valB) return (sortOrder === 'asc') ? 1 : -1;
    return 0;
  });

  // Update counter
  processCount.textContent = filtered.length;

  // 3. Render HTML Rows
  if (filtered.length === 0) {
    processListBody.innerHTML = `
      <tr>
        <td colspan="5" class="empty-state">
          No matching processes found.
        </td>
      </tr>
    `;
    return;
  }

  const rowsHtml = filtered.map(proc => {
    // Dynamic badges for high resource usage
    const cpuClass = proc.cpu > 50 ? 'high-load' : '';
    const memClass = proc.mem > 5 ? 'high-load' : ''; // Above 5% RAM is reasonably high for individual process
    
    return `
      <tr id="proc-row-${proc.pid}">
        <td class="pid-val">${proc.pid}</td>
        <td>
          <span class="process-name" title="${proc.name}">${escapeHtml(proc.name)}</span>
        </td>
        <td>
          <span class="metric-badge cpu-theme ${cpuClass}">${proc.cpu}%</span>
        </td>
        <td>
          <span class="metric-badge mem-theme ${memClass}">${proc.mem}%</span>
        </td>
        <td>
          <button class="btn-kill" onclick="confirmKillProcess(${proc.pid}, '${escapeHtml(proc.name)}')">
            <i class="fa-solid fa-ban"></i> Kill
          </button>
        </td>
      </tr>
    `;
  }).join('');

  processListBody.innerHTML = rowsHtml;
}

// Helper to escape HTML tags to protect against XSS injection if process names are malicious
function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ==========================================================================
// KILL PROCESS FLOW
// ==========================================================================
window.confirmKillProcess = async function(pid, name) {
  const isConfirmed = confirm(`Are you sure you want to terminate process "${name}" (PID: ${pid})?`);
  if (!isConfirmed) return;

  const row = document.getElementById(`proc-row-${pid}`);
  if (row) row.classList.add('highlight-kill');

  try {
    const response = await fetch('/process/kill', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ pid })
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || 'Failed to terminate the process.');
    }

    showToast('Success', `Process "${name}" (PID ${pid}) was successfully terminated.`, 'success');
    
    // Remove the row from view immediately for maximum responsiveness
    if (row) {
      row.style.opacity = '0';
      setTimeout(() => {
        // Remove from list and trigger render in case poller is delayed
        allProcesses = allProcesses.filter(p => p.pid !== pid);
        renderProcesses();
      }, 300);
    }
  } catch (error) {
    if (row) row.classList.remove('highlight-kill');
    showToast('Error', error.message, 'error');
  }
};

// ==========================================================================
// TOAST NOTIFICATIONS UTILITY
// ==========================================================================
function showToast(title, message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  
  const iconMap = {
    success: 'fa-circle-check',
    error: 'fa-circle-exclamation',
    info: 'fa-circle-info'
  };
  
  toast.innerHTML = `
    <i class="fa-solid ${iconMap[type] || 'fa-circle-info'}"></i>
    <div class="toast-content">
      <div class="toast-title">${title}</div>
      <div class="toast-msg">${message}</div>
    </div>
    <button class="toast-close"><i class="fa-solid fa-xmark"></i></button>
  `;

  // Append toast
  toastContainer.appendChild(toast);

  // Wire up manual dismiss button
  toast.querySelector('.toast-close').addEventListener('click', () => {
    dismissToast(toast);
  });

  // Automatically dismiss after 5 seconds
  setTimeout(() => {
    dismissToast(toast);
  }, 5000);
}

function dismissToast(toast) {
  toast.classList.add('fade-out');
  toast.addEventListener('transitionend', () => {
    toast.remove();
  });
}

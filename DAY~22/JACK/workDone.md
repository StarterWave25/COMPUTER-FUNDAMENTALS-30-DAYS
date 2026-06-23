# today s work done
## Module 1: CPU Monitor

* Step 2.1: Create services/cpuService.js

  * Use systeminformation package
  * Write function to fetch: CPU model, cores, speed, current usage %
  * Return as JavaScript object


* Step 2.2: Create routes/cpu.js

  * Create GET /cpu endpoint
  * Call cpuService function
  * Return JSON response
  * Test with Postman/browser
  * Module 2: Memory Monitor


* Step 2.3: Create services/memoryService.js

  * Write function to fetch: total RAM, used RAM, free RAM, usage %
  * Return as JavaScript object


* Step 2.4: Create routes/memory.js

  * Create GET /memory endpoint
  * Call memoryService function
  * Return JSON response
  * Test API

```

1. completed module one that is getting cpu info 
2. done full refactoring for whole api s
3. cpu apis tested in browser with http://localhost:3000/cpu
4. it responsed as :{
  "sussess": true,
  "data": {
    "model": "Core™ i7-10510U",
    "manufacture": "Intel",
    "cores": 8,
    "speed": "1.8GHz",
    "usage": "33.68%"
  }
}

5. same created apis for memory to get memory info 
6. done refactoring for apis 
7. memory apis tested with in browser with  http://localhost:3000/memory
8. responsed as :{
  "success": true,
  "data": {
    "totalRAM": "15.79GB",
    "usedRAM": "8.55GB",
    "freeRAM": "7.25GB",
    "usage": "54.11%"
  }
}


```
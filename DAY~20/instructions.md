# MiniOS Monitor (Week 2 Project)

## Goal

Build a simple OS monitoring dashboard with:

1. Process Monitor
2. CPU Monitor
3. Memory Monitor

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Node.js
* Express

### Packages

```bash
npm install express
npm install systeminformation
npm install ps-node
```

---

## Project Structure

```text
mini-os-monitor/

├── server/
│   ├── routes/
│   │   ├── process.js
│   │   ├── cpu.js
│   │   └── memory.js
│   │
│   ├── services/
│   │   ├── processService.js
│   │   ├── cpuService.js
│   │   └── memoryService.js
│   │
│   └── server.js
│
├── client/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

---

# Module 1: Process Monitor

## API

```http
GET /processes
```

## Display

* PID
* Process Name
* CPU Usage
* Memory Usage

## Features

* List running processes
* Search process by name
* Sort by CPU usage
* Sort by memory usage

---

# Module 2: Kill Process

## API

```http
POST /process/kill
```

### Request

```json
{
  "pid": 1234
}
```

### Features

* Kill selected process
* Show success/error message

---

# Module 3: CPU Monitor

## API

```http
GET /cpu
```

## Display

* Current CPU Usage %
* CPU Model
* Number of Cores
* CPU Speed

## Refresh Rate

Every 2 seconds

---

# Module 4: Memory Monitor

## API

```http
GET /memory
```

## Display

* Total RAM
* Used RAM
* Free RAM
* Usage %

## Refresh Rate

Every 2 seconds

---

# Dashboard Layout

```text
--------------------------------
CPU Monitor
--------------------------------

--------------------------------
Memory Monitor
--------------------------------

--------------------------------
Process Monitor
--------------------------------
```
---

# Definition of Done

✅ Process list displayed

✅ Process search works

✅ Process sorting works

✅ Kill process works

✅ CPU updates every 2 seconds

✅ Memory updates every 2 seconds

✅ Single dashboard page

✅ Project runs with:

Open:
```bash
npm start
```
```text
http://localhost:3000
```
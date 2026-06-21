# MiniOS Monitor

A real-time operating system monitoring dashboard built from scratch using Node.js, Express, and modern CSS/JavaScript. This app displays CPU load, RAM usage, and a detailed process manager that allows searching, sorting, and terminating running tasks.

---

## Features

### 💻 1. CPU Monitor
- Displays hardware specs (Model, Cores, Speed in GHz).
- Polls and tracks live CPU load percentage dynamically every 2 seconds.
- Renders system load using an animated circular gauge.

### 💾 2. Memory Monitor
- Queries system RAM metrics.
- Computes and displays Total RAM, Used RAM, and Free RAM in Gigabytes (GB).
- Visualizes real-time RAM usage % using a nebula-colored radial gauge, updated every 2 seconds.

### 📋 3. Process Monitor & Terminate Engine
- Lists all active processes with details:
  - **PID** (Process Identifier)
  - **Process Name**
  - **CPU Usage %** (per-process load)
  - **Memory Usage %** (per-process RAM)
- **Interactive Search**: Filter processes instantly by name or PID.
- **Dynamic Sort**: Sort table rows by PID, name, CPU %, or memory % in both ascending and descending directions.
- **Process Termination**: Click "Kill" to stop a process by PID. Prompts for confirmation to prevent accidental clicks, and provides instant visual feedback via a slide-in notification toast.

---

## Tech Stack & Architecture

- **Backend**:
  - [Node.js](https://nodejs.org/) (Express runtime environment)
  - [systeminformation](https://systeminformation.io/) (for querying platform-level diagnostics)
  - [ps-node](https://www.npmjs.com/package/ps-node) (cross-platform process termination tool)
- **Frontend**:
  - Semantic HTML5 & Vanilla Javascript (ES6+)
  - Glassmorphic UI with CSS Custom Properties and variables
  - Iconography via FontAwesome v6

---

## Getting Started

### 1. Prerequisites
Ensure you have [Node.js](https://nodejs.org/) (version 18+ recommended) installed on your system.

### 2. Install Dependencies
In the project directory, run:
```bash
npm install
```

### 3. Run the Server
Launch the server using:
```bash
npm start
```
This boots the server and mounts the API routes. You will see this output:
```text
=========================================
  MiniOS Monitor Server is online!       
  URL: http://localhost:3000          
  Press Ctrl+C to shut down.             
=========================================
```

### 4. Access the Dashboard
Open your web browser and go to:
```text
http://localhost:3000
```

---

## API Documentation

The server exposes the following REST APIs which can also be queried directly:

| Method | Endpoint | Description | Payload Example |
| :--- | :--- | :--- | :--- |
| `GET` | `/cpu` | Get CPU brand, physical cores, current speed, and active load %. | - |
| `GET` | `/memory` | Get total, used, free RAM (in bytes) and usage load %. | - |
| `GET` | `/processes` | List all running processes with PID, name, CPU %, and memory %. | - |
| `POST` | `/process/kill` | Terminate a process by PID. | `{"pid": 10542}` |

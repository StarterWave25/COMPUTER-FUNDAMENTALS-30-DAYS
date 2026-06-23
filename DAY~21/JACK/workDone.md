# today work done

## Phase 1: Project Setup & Foundation (Day 1)

* Step 1.1: Initialize Project Structure
1. Create project folder: mini-os-monitor
2. Setup two folders: server/ and client/
3. Initialize Node.js: npm init
4. Install core dependencies: express, systeminformation, cors

* Step 1.2: Verify Dependencies Work
 * Create basic server.js with Express
 * Test that all packages import without errors
 * Confirm no missing modules

* Step 1.3: Setup Basic Server
 * Create Express server listening on port 3000
 * Add CORS middleware (frontend will call backend)
 * Create / route that returns {status: "Server running"}
 * Test server: npm start → open browser on http://localhost:3000

## summary 
## created a file structure as 
```
mini-os-monitor/
│
├── .gitignore
├── package.json
├── package-lock.json
├── server/
│   └── server.js
├── client/
└── node_modules/   (ignored)

and installed all the dependencies and tested them and the systeminformation module gave response as 

{
  "message": "Mini OS Monitor Server is running!",
  "cpu": "Intel Core™ i7-10510U"
}

Means all packages are working well and good 

pushed into github added .gitignore file


```

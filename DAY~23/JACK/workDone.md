## todays work done 
## Module 3: Process Monitor
*  Step 2.5: Create services/processService.js

     * Write function to fetch all running processes
     * For each process: extract PID, name, CPU %, memory %
     * Return as array of objects

*  Step 2.6: Create routes/process.js

     * Create GET /processes endpoint
     * Call processService function
     * Return JSON array
     * Test API

*  Step 2.7: Create POST /process/kill/:pid endpoint

     * Accept PID from request
     * Kill the process using ps-node or system command
     * Return success/error message
     * Handle errors gracefully

```
# created processes module 
1.created processService.js whole logic for geting processes list 
2.created routes for them added into router 
3.mentioned iin server.js 
#testing
4.tested processes endpoint in browser with http://localhost:3000/processes
5.it responsed with array of objects with processes details like {pid ,name,cpu,memory}
as:{
  "success": true,
  "count": 258,
  "data": [
    {
      "pid": 0,
      "name": "System Idle Process",
      "cpu": "72.13%",
      "memory": "0.00%"
    },
    {
      "pid": 4,
      "name": "System",
      "cpu": "1.09%",
      "memory": "0.06%"
    },
    {
      "pid": 172,
      "name": "Registry",
      "cpu": "0.00%",
      "memory": "0.18%"
    }
  ]
}



## next created api for terminating process with pid
1. so i created post method and passing pid as path params to url 
2. in endpoint we will get the pid from path and we will kill that process using process.kill(pid)
3. it will kill the process
and response as terminated process message like :
        {
            "success":true,
            "message":`process with PID 1642 terminated successfully` 
        }


* we need postman to test this endpoint it is POST method so using postman send pid with in url as params ..
 
4. if we dont have permision to kill that process the message will be :
{"success":false,"message":"kill EPERM"}


```
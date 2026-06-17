# **System Calls**
## Why System Calls got introduced?

### **Problem:**
1. In time sharing systems, when multiple users execute programs one after the another in a specific time periods. Any one program with buggy code can access the hardware like disk, RAM, printer directly and may crash the entire system.
2. So, the systems need a way to protect the unsecure hardware access from programs and also protect users from each other.

### **Solution:**
#### Split the Computer into 2 worlds:
1. User Space: The place where the application runs with limited permissions.
2. Kernal Space: The OS runs here and also it has full control of hardware.

```
Chrome
VS Code
Spotify
Node.js

      ↓

Kernel

      ↓

CPU
RAM
Disk
Network
Keyboard
Monitor
```

3. They both present in RAM.
```
+------------------+
| Kernel Memory    |
| Scheduler        |
| Drivers          |
| File System      |
+------------------+

| Process A        |
| Chrome           |
+------------------+

| Process B        |
| VS Code          |
+------------------+

| Process C        |
| Node.js          |
+------------------+
```

4. Here the kernal memory is protected. No application can access it. CPU raises the exception and the program crashes when it is accessed. 

#### When program needs to access the hardware they need to do a request to the kernal space. That request is what we call the ``System Call``.
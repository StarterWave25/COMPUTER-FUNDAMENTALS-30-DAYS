# Day ~ 2 [What actually happens inside the computer when I click an application]
# Observations - Patnam Prudvinath

## Explanation on Program, Process, Thread

* **Program:**<br> 
A Program is a set of instructions written by a developer and stored on disk.  
A program is just a file.
<br><br> 
**Eg:**<br> Chrome.exe, VScode.exe, Your React app, A python script... <br><br>
**So where it lives :**
<br> Usally on SSD, HDD, USB Drive, CD/DVD<br>   
**So why we need it :**
<br> Cause computers understand only instructions. 
<br>Programs allow developers to tell computers, that what the computer should do...
<br><br>
**Program Life Cycle :**
<br>1. Developer write code in a file.
<br>2. Compiler / Interpreter converts it to machine code.
<br>3. File gets stored.
<br>4. Waiting on disk doing nothing until clicked.

---

* **Process:**<br>
A Process is a Program that is currently running. When you double-click a program file, the OS loads it into memory.
<br><br>
**Formula:**<br> Program + Execution = Process
<br><br>
**So where it lives :**
<br> Always in RAM (Memory). It does not run directly on the disk.
<br><br>
**So why we need it :**
<br> To run multiple apps at the same time securely. Each process gets its own separate sandbox (memory, variables, and files). If one process crashes, others keep working perfectly.
<br><br>
**Process Life Cycle :**
<br>1. **New:** The OS creates the process when you double-click an app.
<br>2. **Ready:** The process enters RAM and waits for its turn on the CPU.
<br>3. **Running:** The CPU is actively working on the instructions.
<br>4. **Waiting:** The process pauses to wait for things like network data or user clicks.
<br>5. **Terminated:** You close the application, and the process ends.

---

* **Thread:**<br>
A Thread is the smallest unit of execution inside a Process. The CPU actually runs threads, not processes directly.
<br><br>
**Eg:**<br> Inside Chrome, one thread loads a webpage, another plays video audio, and a third watches your mouse clicks.
<br><br>
**So where it lives :**
<br> Inside a specific Process. It cannot exist on its own.
<br><br>
**So why we need it :**
<br> To do multiple tasks at the exact same time within a single app. Without threads, an app could only do one tiny thing at a time, making it freeze constantly.
<br><br>
**Thread Life Cycle :**
<br>1. **Created:** Spun up by the parent process.
<br>2. **Ready:** Waiting for a turn on the CPU.
<br>3. **Running:** Currently being executed by a CPU core.
<br>4. **Blocked:** Waiting for a specific task or resource to finish.
<br>5. **Terminated:** The task is finished and the thread is destroyed.

---

## Complete User Flow (Summary)

<br>1. **The Program exists:** `chrome.exe` sits completely idle on your SSD.
<br>2. **The App is Clicked:** You double-click the file, and the OS loads it into RAM.
<br>3. **The Process is Born:** The OS sets up a new Process sandbox.
<br>4. **The Main Thread Starts:** The process creates its first thread to launch the window.
<br>5. **More Threads Multiply:** Chrome spins up helper threads for UI, audio, and network requests.
<br>6. **The CPU Executes:** The hardware cycles through these threads to make the app run.
<br>7. **The App is Closed:** You close the app. The threads are destroyed, the process clears out of RAM, and only the static program file remains safely on your SSD.
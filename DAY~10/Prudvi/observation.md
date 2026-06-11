# Day ~ 10 [Observations - PATNAM PRUDVINATH]

# Today's Concept: Process

---

## Part - 1 [Why Was Process Invented?]

### My Assumption:

---

Initially, I thought processes were invented to achieve:

* Multiprocessing
* Running multiple applications
* CPU switching between applications

So I assumed:

> Process exists mainly so the CPU can run many applications at the same time.

---

### My Research:

---

After researching and thinking deeper, I found that multiprocessing is not the original reason.

The real reason is:

> Programs need isolation and protection from each other.

Engineers discovered that if multiple programs share the same memory without boundaries, one program can accidentally modify another program's data.

This can happen because of:

* Bugs
* Invalid Memory Access
* Wrong Pointers
* Programming Errors

Without protection, one application could corrupt another application's data.

---

### The Problem Before Processes

Imagine:

```text
Chrome
VS Code
Spotify
```

are loaded into RAM.

Without processes:

```text
RAM
--------------------------------
Chrome Data
VS Code Data
Spotify Data
--------------------------------
```

All programs share the same memory space.

Now suppose Chrome contains a bug.

It accidentally writes into memory belonging to VS Code.

Result:

```text
Chrome Bug
↓
VS Code Data Corrupted
↓
VS Code Crash
```

Even worse:

```text
Chrome Bug
↓
Operating System Memory Corrupted
↓
System Crash
```

This makes computers unreliable.

---

### The Solution

Engineers created the concept of a Process.

A process gives every running program:

* Its Own Memory Space
* Its Own Resources
* Its Own Execution Environment

Instead of sharing everything.

Now:

```text
Chrome Process
↓
Own Memory
```

```text
VS Code Process
↓
Own Memory
```

```text
Spotify Process
↓
Own Memory
```

One process cannot directly access another process's memory.

This greatly improves stability and safety.

---

### Virtual Address Space

One of the most important ideas inside a process is:

> Virtual Address Space

Every process thinks it owns memory starting from:

```text
0
1
2
3
...
```

For example:

```text
Chrome

Address 1000
```

and

```text
VS Code

Address 1000
```

can both exist simultaneously.

At first this sounds impossible.

The reason it works is because these are virtual addresses.

The Operating System and MMU (Memory Management Unit) translate them into different physical RAM locations.

Example:

```text
Chrome Address 1000
↓
Physical RAM Address 5000
```

```text
VS Code Address 1000
↓
Physical RAM Address 12000
```

Both programs think they own address 1000.

But physically they are using different locations in RAM.

---

### Interesting Observation

Initially I thought:

> Process is mainly for multitasking.

After researching, I realized:

> Process is mainly for isolation and protection.

Multitasking becomes possible because processes provide safe boundaries between programs.

---

## Final Understanding

A process was invented so multiple programs can safely coexist on the same computer.

Without processes:

* Programs could overwrite each other's data.
* One application's bug could crash other applications.
* The operating system would become unstable.

The biggest thing I learned is:

> A process is not just a running program. A process is a protected execution environment with its own memory space and resources.

---

# Part - 2 [What Would Happen If Processes Did Not Exist?]

### My Assumption:

---

Initially, I thought:

> Without processes, computers simply could not run multiple applications.

This is partially true, but the real problem is much deeper.

---

### What Would Actually Happen?

Without processes:

```text
Chrome
VS Code
Spotify
```

would all operate inside the same memory space.

There would be no proper ownership of memory.

No clear boundaries.

No isolation.

---

### Problem 1 - Memory Corruption

Suppose Chrome accidentally writes into memory used by VS Code.

Result:

```text
Chrome Error
↓
VS Code Data Corrupted
↓
VS Code Misbehaves
```

Programs would constantly interfere with each other.

---

### Problem 2 - Application Crashes Spread

Today:

```text
Chrome Crash
↓
Chrome Closes
```

Usually VS Code and Spotify continue working.

Without processes:

```text
Chrome Crash
↓
Shared Memory Damaged
↓
Other Applications Affected
```

One application's failure could affect the entire system.

---

### Problem 3 - No Reliable Resource Ownership

The operating system would struggle to track:

* Memory Usage
* CPU Usage
* Open Files
* Permissions
* Running Applications

Everything would become mixed together.

---

### Problem 4 - Modern Applications Become Difficult

Modern software depends heavily on process isolation.

Examples:

* Browsers
* IDEs
* Games
* Databases
* Servers

Without processes, building reliable software would become extremely difficult.

---

### Problem 5 - Operating System Stability Drops

The operating system relies on process boundaries to manage applications safely.

Without processes:

```text
Application Error
↓
System Error
↓
Potential System Crash
```

System stability would be much lower.

---

## Final Understanding

Without processes:

* Programs would not be properly isolated.
* Memory corruption would become common.
* Application crashes could affect the whole system.
* Resource management would become difficult.
* Modern operating systems would be far less reliable.

The biggest thing I learned is:

> Processes are one of the main reasons modern computers can safely run many applications without those applications interfering with each other.

## Part - 3 [Important Components Of A Process And Why They Exist]

### My Assumption:

---

Initially, I thought:

> A process is simply a running program.

I imagined that when a program starts running, the CPU executes it and that's all.

After learning more deeply, I realized that a process contains much more than just program code.

A process is a complete execution environment managed by the Operating System.

---

## What Exists Inside A Process?

A process contains:

```text
Process
│
├── Program Code
├── Process Memory
├── CPU State
├── Open Files
├── Permissions
├── Process ID (PID)
└── Other Resources
```

Each component exists for a specific reason.

---

## 1. Program Code

### Why It Exists

The CPU needs instructions to execute.

Example:

```c
int add(int a, int b)
{
    return a + b;
}
```

These instructions are stored inside the program file:

```text
chrome.exe
vscode.exe
spotify.exe
```

When the program starts, the code becomes part of the process.

Without program code:

```text
No Instructions
↓
Nothing To Execute
```

---

## 2. Process Memory

### Why It Exists

Running programs constantly create data.

Examples:

```text
Variables
User Input
Open Tabs
Function Results
Downloaded Data
Application State
```

This data does not exist in the original program file.

It is created while the program is running.

The process needs memory to store all this runtime data.

Without memory:

```text
Program Runs
↓
No Place To Store Data
↓
Cannot Function Properly
```

---

## Important Observation

Most runtime data lives in:

```text
RAM
```

Example:

```c
int age = 20;
char name[] = "Prudvi";
```

These variables normally live in the process's memory inside RAM.

---

## 3. CPU State

### Why It Exists

The CPU constantly switches between processes.

Example:

```text
Chrome
↓
VS Code
↓
Spotify
↓
Chrome Again
```

When the CPU leaves Chrome, it must remember:

```text
Current Instruction
Register Values
Flags
Program Counter
```

Otherwise, when Chrome resumes:

```text
Where Was I?
```

would be unknown.

The Operating System saves this information.

This saved information is called:

```text
CPU State
```

or

```text
Context
```

---

## Important Observation

The process does NOT own:

```text
Registers
Cache
CPU
```

Those belong to the processor.

The process only stores enough information to restore them later.

---

## 4. Open Files

### Why They Exist

Programs constantly interact with files.

Examples:

```text
Photos
Videos
Downloads
Documents
Databases
```

Suppose Chrome opens:

```text
notes.txt
```

The process must remember:

```text
Which File Is Open?
Current Position?
Read Mode?
Write Mode?
```

Without this information:

```text
Every File Operation
↓
Need To Start Again
```

which would be inefficient.

---

## 5. Permissions

### Why They Exist

Not every application should access every resource.

Examples:

```text
Camera
Microphone
Network
Documents
Downloads
```

Imagine:

```text
Calculator App
```

accessing:

```text
Passwords
Camera
Microphone
```

without permission.

This would be dangerous.

The Operating System uses permissions to control what a process can access.

---

## 6. Process ID (PID)

### Why It Exists

The Operating System may run hundreds of processes.

Example:

```text
Chrome
VS Code
Spotify
Discord
Steam
```

The OS needs a way to identify each process.

It assigns:

```text
PID = Process ID
```

Example:

```text
Chrome  -> PID 1500
VS Code -> PID 2400
Spotify -> PID 3100
```

This allows the OS to track and manage processes individually.

---

## Runtime Variable Flow

Suppose:

```c
int counter = 0;
```

is stored in the process memory.

When:

```c
counter++;
```

executes:

```text
Process Memory (RAM)
↓
Cache Checked
↓
Value Loaded Into Register
↓
ALU Performs Increment
↓
Updated Value Stored
↓
Process Memory Updated
```

---

## Interesting Observation

Initially, I thought:

> Variables live inside registers.

After researching, I realized:

> Variables usually live in the process memory (RAM).

Registers are only temporary working locations used while the CPU executes instructions.

---

## Final Understanding

A process is much more than a running program.

It contains:

* Program Code
* Process Memory
* CPU State
* Open Files
* Permissions
* Process ID
* Other Resources

The biggest thing I learned is:

> A process is a complete execution environment created and managed by the Operating System.

The program provides the instructions.

The process provides everything needed to execute those instructions safely and independently.

## Part - 4 [Internal Working Of A Process]

### My Assumption:

---

Initially, I thought:

> A process is simply a program running inside the CPU.

I knew that programs execute, but I did not clearly understand:

* How a process is created
* What the Operating System does
* How the CPU executes it
* What happens when it is closed

After researching, I realized that a process has a complete lifecycle managed by the Operating System.

---

## Step 1 - Program Exists On Secondary Storage

Before execution, a program is simply a file stored permanently.

Examples:

```text
chrome.exe
vscode.exe
spotify.exe
```

These files usually exist in:

```text
SSD
HDD
```

At this stage:

```text
Program Stored
↓
Not Executing
```

The program is just data.

It cannot perform any actions.

---

## Step 2 - User Starts The Program

Suppose I double-click:

```text
chrome.exe
```

The Operating System receives the request.

Flow:

```text
User
↓
Operating System
↓
Start Program
```

The OS now begins creating a process.

---

## Step 3 - Operating System Creates A Process

The Operating System creates a new execution environment.

This includes:

```text
PID
Permissions
Memory Information
Scheduling Information
Resource Information
```

These details are stored inside a structure called:

```text
PCB
(Process Control Block)
```

Think of the PCB as the OS's record for that process.

Without it:

```text
OS Cannot Manage Process
```

---

## Step 4 - Memory Is Allocated

The Operating System allocates memory for the process.

This memory will hold:

```text
Program Code
Variables
Runtime Data
Application State
```

Flow:

```text
OS Creates Process
↓
Memory Allocated
↓
Ready To Load Program
```

---

## Step 5 - Program Is Loaded Into RAM

The CPU cannot execute programs directly from SSD.

So the OS loads the required parts of the program into RAM.

Flow:

```text
Program File (SSD)
↓
RAM
↓
Ready For Execution
```

Now the process has:

```text
Program Code
+
Process Memory
```

available in RAM.

---

## Step 6 - Process Gets CPU Time

The OS scheduler selects the process.

Flow:

```text
Ready Process
↓
CPU Scheduler
↓
CPU Assigned
```

Now the CPU starts executing instructions.

Example:

```c
int total = 0;

total++;
```

The CPU begins processing these instructions.

---

## Step 7 - Execution Begins

Suppose:

```c
int counter = 0;
```

exists inside process memory.

The execution flow is:

```text
RAM
↓
Cache Checked
↓
Register
↓
ALU Executes
↓
Register Updated
↓
RAM Updated
```

Important:

* Variables usually live in RAM.
* Registers are temporary workspaces.
* Cache speeds up access automatically.

---

## Step 8 - User Interaction Happens

Suppose the user clicks a button.

Flow:

```text
Mouse Click
↓
Mouse Hardware
↓
Interrupt Generated
↓
Operating System
↓
Event Sent To Process
↓
Application Handles Event
```

Example:

```text
User Clicks YouTube Video
↓
Chrome Receives Event
↓
Video Starts Playing
```

The Operating System delivers events.

The process decides how to react.

---

## Step 9 - Context Switching

The CPU cannot stay with one process forever.

Example:

```text
Chrome
↓
VS Code
↓
Spotify
↓
Chrome Again
```

Before switching away, the OS saves:

```text
Program Counter
Register Values
Flags
Stack Pointer
```

This information is called:

```text
Context
```

When the process runs again:

```text
Saved Context
↓
Restored
↓
Execution Continues
```

This makes multitasking possible.

---

## Step 10 - Process Continues Running

The process repeatedly performs:

```text
Receive Events
↓
Execute Instructions
↓
Update Memory
↓
Wait For CPU
↓
Resume Execution
```

This cycle continues until the process ends.

---

## Step 11 - Process Termination

Suppose the user closes Chrome.

Flow:

```text
User Closes Application
↓
OS Terminates Process
```

The Operating System removes:

```text
Process Memory
PCB
PID
CPU State
Open Files
Allocated Resources
```

These resources are returned to the system.

---

## Step 12 - Program File Still Exists

A very important observation:

The process is destroyed.

The program is not.

After Chrome closes:

```text
Process
❌ Removed
```

```text
chrome.exe
✅ Still Exists On SSD
```

That is why Chrome can be opened again later.

---

## Interesting Observation

Initially, I thought:

> Closing an application removes the application.

After researching, I realized:

> Closing an application removes the process, not the program file.

The program remains stored permanently on SSD.

Only the running instance disappears.

---

## Complete Process Lifecycle

```text
Program File Stored In SSD
↓
User Starts Program
↓
OS Creates Process
↓
PCB Created
↓
PID Assigned
↓
Memory Allocated
↓
Program Loaded Into RAM
↓
Scheduler Gives CPU Time
↓
Process Executes
↓
User Interacts
↓
Context Switching Happens
↓
Process Continues Running
↓
User Closes Application
↓
Process Terminated
↓
Resources Released
↓
Program File Remains On SSD
```

---

## Final Understanding

A process is not created by the CPU.

A process is created and managed by the Operating System.

The Operating System:

* Creates the PCB
* Assigns a PID
* Allocates Memory
* Loads Program Code
* Schedules CPU Time
* Handles Context Switching
* Terminates The Process

The biggest thing I learned is:

> A process has a complete lifecycle. It is created by the Operating System, executes using CPU time, and is eventually destroyed while the original program file remains safely stored on SSD.

## Part - 5 [How Processes Interact With Other Computer Science Concepts]

A process does not work alone.

It constantly interacts with almost every major component inside a computer system.

---

### Process & Program

A program is a file stored on secondary storage.

Example:

```text
chrome.exe
vscode.exe
```

A process is the running instance of that program.

Flow:

```text
Program (SSD)
↓
OS Creates Process
↓
Process Executes
```

---

### Process & RAM

Every process needs memory to store:

* Variables
* Runtime Data
* User Input
* Application State

Flow:

```text
Process
↓
RAM
↓
Stores Runtime Data
```

Without RAM, a process cannot execute efficiently.

---

### Process & CPU

The CPU executes the instructions belonging to a process.

Flow:

```text
Process
↓
CPU
↓
Instruction Execution
```

The CPU can execute only a very small amount of work at a time.

Therefore processes must share CPU time.

---

### Process & Registers

During execution:

```text
Process Memory
↓
Registers
↓
ALU Executes
```

Registers temporarily hold the values currently being used by the CPU.

---

### Process & Cache

Cache speeds up memory access.

Flow:

```text
Process Memory
↓
Cache
↓
Registers
↓
CPU
```

Frequently or recently used data may be copied closer to the CPU through cache.

---

### Process & Operating System

The OS is responsible for:

* Process Creation
* Process Scheduling
* Memory Allocation
* Permission Management
* Resource Management
* Process Termination

Flow:

```text
OS
↓
Creates Process
↓
Manages Process
↓
Destroys Process
```

---

### Process & Scheduler

The scheduler decides:

```text
Which Process Runs?
For How Long?
When To Switch?
```

Flow:

```text
Ready Processes
↓
Scheduler
↓
CPU Time Allocation
```

---

### Process & Virtual Memory

Each process receives its own virtual address space.

Example:

```text
Chrome Address 1000
```

and

```text
VS Code Address 1000
```

can both exist.

The OS and MMU translate them into different physical RAM locations.

This provides isolation.

---

### Process & Files

Processes interact with files through the Operating System.

Example:

```text
Process
↓
Open File
↓
Read / Write
```

The process keeps track of opened files while running.

---

### Process & Threads

A process can contain one or more threads.

Example:

```text
Chrome Process
│
├── Thread 1
├── Thread 2
├── Thread 3
└── Thread 4
```

Threads perform the actual execution work inside the process.

---

## Final Understanding

A process acts as a central unit that connects:

```text
Program
RAM
CPU
Registers
Cache
OS
Scheduler
Files
Threads
Virtual Memory
```

Almost every major operating system concept exists to support, manage, or execute processes.

---

# Part - 6 [Common Misconceptions Beginners Have]

---

### Misconception 1

> Process = Program

Reality:

```text
Program
=
File Stored On SSD
```

```text
Process
=
Running Instance Of Program
```

---

### Misconception 2

> Variables Live In Registers

Reality:

Variables usually live in RAM.

Registers temporarily hold values while instructions execute.

---

### Misconception 3

> A Process Owns Registers

Reality:

Registers belong to the CPU.

The process only stores enough information to restore register values later.

---

### Misconception 4

> Closing An Application Deletes It

Reality:

Closing an application destroys the process.

The program file remains stored on SSD.

---

### Misconception 5

> Processes Exist Only For Multitasking

Reality:

The primary purpose of a process is isolation and protection.

Multitasking becomes possible because processes provide safe boundaries.

---

### Misconception 6

> Every Process Has Different Physical RAM Addresses

Reality:

Every process usually sees its own virtual memory space.

Different virtual addresses can map to different physical RAM locations.

---

### Misconception 7

> The CPU Runs Many Processes Simultaneously

Reality:

A CPU core executes one instruction stream at a time.

The OS rapidly switches between processes.

This creates the illusion of simultaneous execution.

---

## Final Understanding

Most beginner mistakes happen because they confuse:

```text
Program
Process
Thread
Memory
CPU
```

Understanding the difference between them is a major step toward operating-system engineering.

---

# Part - 7 [Complete Flow Diagram]

```text
Program Stored On SSD
↓
User Starts Program
↓
Operating System Receives Request
↓
PCB Created
↓
PID Assigned
↓
Memory Allocated
↓
Virtual Address Space Created
↓
Required Program Code Loaded Into RAM
↓
Process Added To Ready Queue
↓
Scheduler Selects Process
↓
CPU Assigned
↓
Instructions Execute
↓
Registers Used
↓
Cache Accelerates Access
↓
RAM Stores Runtime Data
↓
User Generates Events
↓
OS Delivers Events
↓
Process Handles Events
↓
Context Switching Occurs
↓
Execution Continues
↓
User Closes Application
↓
OS Terminates Process
↓
Memory Released
↓
PCB Removed
↓
PID Released
↓
Resources Released
↓
Program File Remains On SSD
```

---

# Part - 8 [How Processes Appear In Real Software Systems]

### Google Chrome

Chrome uses many processes.

Example:

```text
Chrome
├── Browser Process
├── Tab Process
├── Extension Process
└── GPU Process
```

If one tab crashes:

```text
One Process Crashes
↓
Other Tabs Continue Working
```

---

### VS Code

VS Code creates multiple processes for:

```text
Editor
Extensions
Language Servers
Terminal
```

This improves stability.

---

### Games

Modern games often create processes that interact with:

```text
GPU
Audio
Networking
Physics Systems
```

---

### Databases

Databases create processes to:

```text
Handle Queries
Manage Connections
Perform Background Tasks
```

---

### Operating Systems

Even the operating system itself creates many processes.

Examples:

```text
File Manager
Settings
Network Services
Printing Services
```

---

## Final Understanding

Every application you use daily is built around processes.

Processes are one of the most fundamental execution units in modern computing.

---

# Part - 9 [What Experienced Engineers Think About Processes]

Beginners usually focus on:

```text
Process
=
Running Program
```

Experienced engineers think about:

```text
Isolation
Protection
Resource Ownership
Scheduling
Memory Management
Fault Containment
```

---

### Fault Containment

One of the biggest reasons processes exist:

```text
One Process Fails
↓
Entire System Does Not Fail
```

This idea is extremely important in modern software.

---

### Resource Ownership

Experienced engineers ask:

```text
Who Owns This Memory?
Who Owns This File?
Who Owns This Network Socket?
```

The answer is usually:

```text
A Process
```

---

### Security

Processes create boundaries.

Without these boundaries:

```text
Applications
↓
Could Access Each Other's Data
```

Security would become much weaker.

---

### Virtual Memory Is A Superpower

Experienced engineers know:

> The most powerful feature of a process is often its private virtual address space.

It provides:

* Isolation
* Security
* Stability
* Simpler Programming

---

## Final Understanding

Experienced engineers see processes as:

```text
Protected Execution Environments
```

rather than merely running programs.

---

# Part - 10 [Summary]

A process is a running instance of a program managed by the Operating System.

The OS creates a process when a program starts executing.

Every process receives its own memory, resources, permissions, and execution context.

Processes provide isolation, protection, and stability between applications.

The CPU executes process instructions while the OS manages scheduling and context switching.

Variables usually live in RAM, while registers act as temporary workspaces.

Each process has its own virtual address space, making programs feel like they own memory independently.

When a process ends, its resources are released, but the original program file remains on SSD.

The biggest thing I learned is:

> A process is not simply a running program. It is a protected execution environment containing everything required for safe and independent execution.

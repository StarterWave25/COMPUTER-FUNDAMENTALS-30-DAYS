Processes — The Deep Mental Model

Most beginners think:

"A process is a running program."

That's correct, but it's only about 5% of the story.

A senior engineer thinks:

A process is an isolated execution environment containing code, memory, resources, security context, and execution state managed by the operating system.

Let's build this from first principles.

1. Why Were Processes Invented?

Imagine early computers.

They ran one program:

Program Starts
↓
Uses Entire Machine
↓
Finishes
↓
Next Program Starts

Problems:

No multitasking
No isolation
One bug could crash everything
No security
Example

Suppose:

Word Processor
Calculator
Browser

all run simultaneously.

Questions:

Who gets CPU time?
Who owns memory?
How do they avoid corrupting each other?

The answer became:

Processes

A process gives each program its own protected world.

2. What Is a Process Really?

When you double-click:

chrome.exe

or

ChatGPT Desktop

the OS does NOT simply run the file.

Instead it creates:

Process
├── Code
├── Memory
├── Registers
├── Open Files
├── Threads
├── Security Context
├── Process ID
└── Execution State

A process is much more than code.

3. Program vs Process

This distinction is critical.

Program

A program is:

Passive
Stored on SSD
Not running

Example:

chrome.exe

sitting on disk.

Process

A process is:

Active
Loaded into memory
Executing

Example:

Chrome currently running

Think:

Recipe = Program

Cooking = Process
4. What Happens When You Start a Program?

Suppose you click Chrome.

Step 1: User Request
Mouse Click
↓
OS Receives Request
Step 2: Process Creation

Kernel creates:

Process Control Block (PCB)

This is the process's identity card.

Contains:

PID
Registers
State
Memory Info
Priority
Open Files
Step 3: Memory Allocation

OS creates virtual memory.

Chrome Process
│
├── Code Segment
├── Data Segment
├── Heap
└── Stack
Step 4: Load Program

Executable loaded from SSD.

SSD
↓
RAM
Step 5: Create Main Thread

Every process starts with at least one thread.

Process
└── Main Thread
Step 6: Scheduler Places Process In Queue
Ready Queue

Now process waits for CPU.

5. Internal Memory Layout

Every process gets:

+----------------+
| Code Segment   |
+----------------+
| Data Segment   |
+----------------+
| Heap           |
|     ↑          |
|     ↑ grows    |
+----------------+
| Stack          |
|     ↓ grows    |
|     ↓          |
+----------------+
Code Segment

Contains instructions.

printf("Hello");

Machine code lives here.

Data Segment

Stores global variables.

int count = 10;
Heap

Dynamic memory.

malloc()
new

Used for:

Objects
Arrays
Databases
Browser tabs
Stack

Stores:

Function Calls
Local Variables
Return Addresses
6. Process States

A process isn't always running.

Most of the time it waits.

New

Just created.

NEW
Ready

Ready for CPU.

READY

Waiting in queue.

Running

CPU currently executing it.

RUNNING
Waiting / Blocked

Waiting for something.

Examples:

Disk Read
Network Response
Keyboard Input

State:

WAITING
Terminated

Finished.

TERMINATED
Process State Diagram
          +------+
          | NEW  |
          +------+
              |
              v
         +---------+
         | READY   |
         +---------+
              |
              v
         +---------+
         | RUNNING |
         +---------+
          /      \
         /        \
        v          v
+-----------+  +-----------+
| WAITING   |  | TERMINATED|
+-----------+  +-----------+
      |
      v
+-----------+
| READY     |
+-----------+
7. How Is a Process Executed?

Suppose:

x = 5 + 3;
CPU Fetches Instruction
Program Counter
↓
Instruction Memory
Instruction Goes To Register
Instruction Register
Data Loaded
RAM
↓
Cache
↓
Registers
ALU Executes
5 + 3
Result Stored
Register
↓
Cache
↓
RAM

Repeat billions of times.

8. Context Switching

This is where OS magic happens.

Suppose:

Chrome Running

Suddenly:

Spotify Needs CPU

CPU can run only one thread per core.

OS performs:

Context Switch
Save Chrome

Store:

Registers
Program Counter
Stack Pointer
Flags

inside PCB.

Load Spotify

Restore:

Registers
PC
SP
Flags

from Spotify PCB.

Resume Spotify

Spotify continues exactly where it stopped.

User thinks:

Everything runs simultaneously

Actually:

Chrome
Spotify
VS Code
Discord

take turns

extremely fast.

9. Process vs Thread

Many beginners confuse them.

Process

Owns resources.

Memory
Files
Security
Thread

Executes instructions.

CPU Worker

Example:

Chrome Process
│
├── Renderer Thread
├── Network Thread
├── GPU Thread
├── JavaScript Thread
└── Audio Thread

One process.

Many threads.

10. Why Processes Are Expensive

Creating a process requires:

Memory Allocation
PCB Creation
Virtual Memory Setup
Security Setup
Thread Creation

Costly.

Creating a thread:

Much Cheaper

This is why modern applications use thread pools.

11. What Happens When a Process Crashes?

Example:

int* p = NULL;
*p = 5;

Invalid memory access.

CPU raises:

Segmentation Fault

OS kills process.

Good news:

Only that process dies.

Not the whole machine.

Process isolation saves us.

12. Real Browser Example

Open ChatGPT.

You may think:

One browser process

Reality:

Chrome
│
├── Browser Process
├── Renderer Process
├── GPU Process
├── Network Process
├── Audio Process
└── Utility Processes

Each isolated.

If one crashes:

Tab crashes

Browser survives.

13. What Senior Engineers Think About

Beginners focus on:

Process = running program

Senior engineers focus on:

Isolation
Scheduling
Memory
Synchronization
IPC
Context Switch Cost
Resource Ownership
Insight #1

CPU time is cheap.

Moving data is expensive.

Insight #2

Most processes spend most of their life:

WAITING

not running.

Insight #3

Performance issues often come from:

Too many context switches

rather than slow code.

Insight #4

A process is mostly:

Memory + State

not CPU execution.

Insight #5

Processes are security boundaries.

When Chrome opens a malicious page:

Renderer Process
↓
Sandbox
↓
Limited Damage

That's process isolation at work.

Complete Process Lifecycle
Executable File (SSD)
          │
          ▼
Process Creation Request
          │
          ▼
Kernel Creates PCB
          │
          ▼
Virtual Memory Allocated
          │
          ▼
Code Loaded Into RAM
          │
          ▼
Main Thread Created
          │
          ▼
NEW
          │
          ▼
READY
          │
          ▼
RUNNING
          │
     ┌────┴────┐
     │         │
     ▼         ▼
WAITING   TERMINATED
     │
     ▼
READY
     │
     ▼
RUNNING
The Mental Model

Think of a process as a private apartment inside a huge building (the operating system).

Operating System = Building
Process = Apartment
Threads = People inside apartment
CPU = Elevator
RAM = Apartment space
Registers = What a person is currently holding
Cache = Table beside the person

The OS's primary job is not running programs—it is creating, protecting, scheduling, and destroying processes efficiently while making thousands of programs believe they each own the entire computer. That illusion is one of the greatest achievements in computer science.
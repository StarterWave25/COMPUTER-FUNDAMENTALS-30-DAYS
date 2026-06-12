# Day ~ 10 [Observations - PATNAM PRUDVINATH]

# Today's Concept: Threads

---

## Part - 1 
### [Why Was Threads Invented?]
### [What Problem Existed Before]
### [What would happen if it is not existed]

### My Assumption:


Initially, I thought:

Processes already **allow multiple applications** to run, so there is no need for another concept called threads.

I thought if an application needs to perform multiple tasks, the Operating System could **simply create more processes.**

After researching and thinking deeper, I realized that processes and threads **solve different problems.**

Processes provide isolation.

Threads provide multiple execution paths inside the same process.

The Problem Before Threads

**Imagine a browser process contains:**

User Input
Button Clicks
Page Rendering
Video Playback
File Downloading
Network Requests

Now imagine this process has only:

1 Process
1 Execution Path

**The execution would look like:**

Task 1<br>
↓<br>
Task 2<br>
↓<br>
Task 3<br>
↓<br>
Task 4

Every task must wait for the previous task to finish.

Suppose a large file download takes several seconds.

**Then:**

Scrolling
Typing
Button Clicks
Rendering

must wait.

**This causes:**

Frozen UI
Poor Responsiveness
Bad User Experience
Why Not Create More Processes?

At first this sounds like an easy solution.

**Example:**

UI Process
Download Process
Rendering Process
Network Process

**But every process requires:**
Its Own Memory Space
PID
Virtual Address Space
Permissions
OS Management
Context Switching

Creating a full process for every small task becomes expensive.

**For tasks like:**

Auto Save
Spell Check
Syntax Highlighting
Background Sync

creating separate processes would be inefficient.

The Solution

Engineers introduced:

Thread

A thread is an execution path inside a process.

Instead of creating many processes:

Chrome Process<br>
│<br>
├── Thread 1 → UI<br>
├── Thread 2 → Download<br>
├── Thread 3 → Rendering<br>
└── Thread 4 → Network

**All threads share:**

Memory
Files
Resources
Permissions

while executing independently.

Important Observation

Processes and threads solve different problems.

**Process:**

Isolation
Protection
Resource Ownership

**Thread:**

Concurrent Execution
Responsiveness
Efficient Resource Sharing

## Part - 3
### [Internal Components of a Thread]

Process<br>
│<br>
├── Code Segment<br>
├── Heap<br>
├── Files<br>
├── Permissions<br>
├── Resources<br>
│<br>
├── Thread 1<br>
│   ├── TID<br>
│   ├── PC<br>
│   ├── Registers<br>
│   ├── Stack<br>
│   └── State<br>
│<br>
├── Thread 2<br>
│   ├── TID<br>
│   ├── PC<br>
│   ├── Registers<br>
│   ├── Stack<br>
│   └── State<br>

## Thread ID (TID)

**Purpose:** Uniquely identifies a thread inside the Operating System.

---

## Program Counter (PC)

**Purpose:** Stores the address of the next instruction to execute.

---

## Registers

**Purpose:** Hold the data currently being processed by the CPU.

---

## Stack

**Purpose:** Stores function-call information and temporary execution data.

---

## Thread State

**Purpose:** Represents the current condition of a thread.

---

## Scheduling Information

**Purpose:** Helps the Operating System decide when and where a thread should run.

---

## Shared Process Memory

**Purpose:** Allows all threads inside a process to access the same data.

---

## Shared Code Segment

**Purpose:** Contains the program instructions executed by all threads.

---

## Shared Files and Resources

**Purpose:** Allow threads to work with the same files, network connections, and operating-system resources.

## Part - 4
### [Internal working step-by-step]
### Complete Flow Diagram

chrome.exe (SSD)<br>
↓<br>
Double Click<br>
↓<br>
OS Creates Process<br>
↓<br>
PID Assigned<br>
↓<br>
Memory Allocated<br>
↓<br>
Main Thread Created<br>
↓<br>
CPU Executes Main Thread<br>
↓<br>
Browser Window Appears<br>
↓<br>
Additional Threads Created<br>
│<br>
├── UI Thread<br>
├── Network Thread<br>
├── Rendering Thread<br>
├── GPU Thread<br>
└── Worker Threads<br>
↓<br>
User Types Prompt<br>
↓<br>
Keyboard Interrupt<br>
↓<br>
OS Delivers Event<br>
↓<br>
UI Thread Updates Input Box<br>
↓<br>
User Presses Enter<br>
↓<br>
UI Thread Creates Request<br>
↓<br>
Network Thread Sends Request<br>
↓<br>
Internet<br>
↓<br>
ChatGPT Server<br>
↓<br>
Server Process<br>
↓<br>
Server Thread<br>
↓<br>
Response Generated<br>
↓<br>
Response Sent Back<br>
↓<br>
Network Thread Receives Response<br>
↓<br>
Rendering Thread Builds UI<br>
↓<br>
UI Thread Updates Screen<br>
↓<br>
User Sees Response

## Step 1: Thread Creation

A thread is created either when a process starts or when an existing thread requests the creation of a new thread.

When a thread is created, the Operating System allocates:

- Thread ID (TID)
- Program Counter (PC)
- Registers
- Stack
- Thread State Information
- Scheduling Information

At this stage, the thread exists but has not started executing yet.

---

## Step 2: Ready State

After creation, the thread enters the Ready state.

This means:

> "I am ready to execute, but I am waiting for CPU time."

The thread is placed into a ready queue maintained by the scheduler.

The thread may wait here for a short or long period depending on system load and scheduling decisions.

---

## Step 3: Scheduler Selection

The Operating System scheduler continuously examines all ready threads.

Its job is to decide:

- Which thread should run next
- Which CPU core should run it
- How long it should run

When selected, the scheduler assigns CPU time to the thread.

---

## Step 4: Execution Begins

The CPU loads the thread's execution context:

- Program Counter
- Register Values
- Stack Pointer

The thread begins executing instructions.

During execution, the thread:

- Reads instructions from the process's code segment
- Reads and modifies data in memory
- Uses registers for temporary calculations
- Uses its stack for function calls and local variables

This is the stage where actual work is performed.

---

## Step 5: Context Switching

The CPU cannot remain dedicated to one thread forever.

When another thread needs CPU time, the Operating System performs a context switch.

The OS saves:

- Program Counter
- Registers
- Stack Pointer
- Processor Flags

These values are stored so execution can continue later from exactly the same point.

The CPU then loads the context of another thread and begins executing it.

---

## Step 6: Waiting / Blocked State

Sometimes a thread cannot continue execution immediately.

Common reasons include:

- Waiting for disk operations
- Waiting for network responses
- Waiting for user input
- Waiting for another thread
- Waiting for a synchronization lock

Instead of wasting CPU time, the Operating System places the thread into a waiting state.

While waiting, the thread consumes almost no CPU time.

---

## Step 7: Returning To Ready State

Once the required event occurs, the thread becomes ready again.

Examples:

- Disk operation completes
- Network response arrives
- User input is received
- Lock becomes available

The Operating System moves the thread back into the ready queue.

The thread now waits for CPU time again.

---

## Step 8: Resuming Execution

When the scheduler selects the thread again, the Operating System restores the previously saved context.

The Program Counter, Registers, and Stack Pointer are restored.

Execution continues exactly from the instruction where the thread was paused.

The thread behaves as if it had never stopped.

---

## Step 9: Thread Termination

Eventually the thread completes its task.

Examples:

- Function finishes
- Download completes
- Background task finishes
- Application exits

At this point the thread enters the terminated state.

The thread will never execute again.

---

## Step 10: Cleanup

After termination, the Operating System removes:

- Thread ID
- Stack
- Saved Register Context
- Scheduling Information
- Thread Management Structures

These resources are returned to the system.

If other threads still exist inside the process, the process continues running normally.

Only the terminated thread is removed.

---

## Thread States

A thread generally moves through the following states:

- Created
- Ready
- Running
- Waiting / Blocked
- Ready
- Running
- Terminated

Not every thread enters the waiting state, but every thread eventually reaches the terminated state.

---

## Part - 6 [Common Misconceptions Beginners Have]

### 1. Thread = Small Process

**Reality:**  
A process owns resources. A thread executes instructions using those resources.

---

### 2. CPU Executes Processes

**Reality:**  
The CPU executes threads, not processes.

---

### 3. Every Thread Has Its Own Memory

**Reality:**  
Threads share process memory but have separate stacks and registers.

---

### 4. Threads Always Run Simultaneously

**Reality:**  
On a single CPU core, threads usually take turns running.

---

### 5. More Threads = More Performance

**Reality:**  
Too many threads can reduce performance due to scheduling overhead.

---

### 6. Threads Exist Only For Speed

**Reality:**  
Threads were primarily introduced for concurrency and responsiveness.

---

### 7. Threads Are Completely Independent

**Reality:**  
Threads share memory and resources inside the same process.

---

### 8. Threads Cannot Affect Each Other

**Reality:**  
Shared memory means one thread can accidentally affect another.

---

### 9. A Thread Is Just A Function

**Reality:**  
A thread is an execution context that runs functions.

---

### 10. Processes And Threads Solve The Same Problem

**Reality:**  
Processes provide isolation; threads provide concurrent execution.

---

## Part - 8 [How Threads Appear In Real Software Systems]

### 1. Chrome Browser

**Threads:**

- UI Thread
- Rendering Thread
- Network Thread
- GPU Thread
- Audio Thread

**Why?**

While a page is loading:

- UI Thread handles clicks and scrolling.
- Network Thread downloads data.
- Rendering Thread draws the webpage.
- GPU Thread renders graphics.

Without threads, Chrome would frequently freeze.

---

### 2. VS Code

**Threads:**

- UI Thread
- File System Thread
- Extension Threads
- Language Server Threads

**Why?**

While typing:

- UI remains responsive.
- Auto-save runs in background.
- Syntax highlighting updates.
- IntelliSense generates suggestions.

All happen concurrently.

---

## Part - 9 [What An Experienced Engineer Thinks About Threads That Beginners Usually Miss]

### 1. Threads Are About Concurrency First, Performance Second

**Beginner Thinks:**

> Threads exist to make programs faster.

**Experienced Engineer Thinks:**

> Threads were primarily introduced so multiple activities can progress independently.

Performance improvements are often a side effect.

---

### 2. Threads Are Cheap, But Not Free

**Beginner Thinks:**

> Just create more threads.

**Experienced Engineer Thinks:**

> Every thread consumes memory, scheduling time, and context-switching overhead.

More threads can sometimes reduce performance.

---

### 3. Shared Memory Is Both A Superpower And A Risk

**Beginner Thinks:**

> Sharing memory is convenient.

**Experienced Engineer Thinks:**

> Shared memory is the source of most multithreading bugs.

The hardest problems in multithreading usually come from threads modifying the same data.

---

### 4. Most Complexity Comes From Coordination, Not Creation

**Beginner Thinks:**

> Creating threads is the difficult part.

**Experienced Engineer Thinks:**

> Coordinating threads safely is the difficult part.

Creating a thread is easy.

Making 100 threads work together correctly is hard.

---

### 5. The CPU Never Sees "Applications"

**Beginner Thinks:**

> CPU runs Chrome, VS Code, and WhatsApp.

**Experienced Engineer Thinks:**

> CPU only runs threads.

The scheduler continuously switches between threads regardless of which application they belong to.

---

### 6. Context Switching Is An Invisible Cost

**Beginner Thinks:**

> More threads means more work gets done.

**Experienced Engineer Thinks:**

> Too many threads may spend more time switching than working.

A thread that is constantly paused and resumed becomes inefficient.

---

### 7. Processes Protect, Threads Cooperate

**Beginner Thinks:**

> Processes and threads are similar concepts.

**Experienced Engineer Thinks:**

> Processes provide isolation; threads provide execution.

They solve completely different problems.

---

### 8. Most Modern Software Is Actually A Collection Of Threads

**Beginner Thinks:**

> Chrome is one program.

**Experienced Engineer Thinks:**

> Chrome is a process containing many specialized threads working together.

The same is true for VS Code, games, databases, and web servers.

---

### 9. Waiting Is Normal

**Beginner Thinks:**

> A thread should always be running.

**Experienced Engineer Thinks:**

> Most threads spend much of their life waiting.

Waiting for:

- Disk
- Network
- User Input
- Other Threads

is completely normal.

---

### 10. A Thread Is An Execution Context

**Beginner Thinks:**

> A thread is just a task.

**Experienced Engineer Thinks:**

> A thread is a complete execution context containing its own Program Counter, Registers, Stack, and State.

This is the deepest mental model of a thread.

---

## Biggest Insight

The biggest thing experienced engineers understand is:

> A process is a resource container. A thread is the worker that executes inside that container.

Once this distinction becomes clear, most Operating System concepts become much easier to understand.
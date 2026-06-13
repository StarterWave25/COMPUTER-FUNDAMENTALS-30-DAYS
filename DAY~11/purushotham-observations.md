# Day 11 — Threads

## Learn It Like an Engineer Building a Mental Model

---

# 1. Why Was This Concept Invented & What Problem Existed Before It?

We already learned:

- A **process** is an isolated container (memory, files, sockets, etc.)
- The CPU executes instructions
- The OS schedules execution using processes

Now imagine a real application:

Chrome / ThinkStack / VS Code / PostgreSQL

`

Inside each one, multiple things must happen **at the same time**:

### Example: Browser

- UI must remain responsive
- JavaScript must execute
- Network requests must run
- Rendering must happen
- User input must be handled instantly

If everything ran in a single execution path:

One Process
→ One Task at a time
→ Everything blocks everything else

Problem:

- UI freezes during network calls
- Downloads block rendering
- One slow task blocks entire application

So the OS and runtime needed a finer unit of execution inside a process.

That unit is:

> **Thread**

---

# Core Idea

A process is a **resource container**.

A thread is an **execution path inside that container**.

---

# 2. What Would Happen If Threads Did Not Exist?

Without threads:

### In browsers:

- Webpage freezes during API calls
- No smooth scrolling
- No background rendering
- No parallel JavaScript execution

### In databases:

- Query execution blocks all other operations
- No concurrency
- No background maintenance tasks

### In servers:

- One request blocks all others
- No scalability

So the system becomes:

One process = One execution flow = No responsiveness

Modern computing would collapse.

---

# 3. Important Components of Threads

A process contains shared resources:

Process
├── Memory (Heap)
├── Files
├── Network Sockets
├── Code

Inside a process, threads exist:

Process
├── Thread 1
├── Thread 2
├── Thread 3

---

## What Each Thread Has

Each thread has its own:

### 1. Stack

- Function calls
- Local variables
- Return addresses

Why?
→ Each execution path needs its own function history

---

### 2. Registers

- Instruction pointer
- CPU state
- Temporary computation values

Why?
→ CPU must pause/resume execution exactly

---

### 3. Execution context

- Program counter
- Current instruction state

---

## What Threads SHARE (Very Important)

All threads inside a process share:

- Heap memory
- Code segment
- Open files
- Network connections

This is the biggest reason threads are powerful and dangerous.

---

# 4. Internal Working Step-by-Step

Let’s imagine:

ThinkStack backend process

has 3 threads:

- Thread A → API handling
- Thread B → Database queries
- Thread C → Background cleanup

---

## Step 1: Process starts

OS creates:

Process PCB
Memory space
Main thread

---

## Step 2: Threads are created

OS creates multiple thread control blocks:

TCB (Thread Control Block)

Each contains:

- stack pointer
- registers
- thread state

---

## Step 3: Scheduler sees threads (not just processes)

Important:

👉 Modern OS schedules **threads**, not whole processes.

So scheduler sees:

Thread A
Thread B
Thread C
Thread D (Chrome UI)
Thread E (Node server)

---

## Step 4: CPU execution starts

Thread A runs:

fetch request

---

## Step 5: Context switch between threads

OS may interrupt Thread A:

Save registers → TCB A
Load registers → TCB B

Now Thread B runs.

---

## Step 6: Shared memory access

Thread A and B access:

Heap memory (shared)

No copying needed.

---

## Step 7: Parallel illusion

On multi-core CPU:

Core 1 → Thread A
Core 2 → Thread B
Core 3 → Thread C

True parallel execution happens.

---

# 5. Interaction with Other CS Concepts

---

## CPU

Threads are the **actual units executed by CPU**

---

## Scheduler

Scheduler chooses:

Which thread runs next

---

## Context Switching

Switching happens between threads:

- save registers
- restore registers

---

## Process

Threads live inside processes.

---

## Memory (Heap/Stack)

- Stack → per thread
- Heap → shared across threads

---

## Cache

Threads heavily use CPU cache:

- cache pollution happens during switches

---

## System Calls

Threads request OS services independently.

---

## I/O (Disk + Network)

Threads handle:

- disk reads
- network requests
- async tasks

---

## Interrupts

Threads often wake due to:

- network interrupt
- disk interrupt
- timer interrupt

---

# 6. Common Misconceptions

---

## Misconception 1

“Process and thread are same”

❌ Wrong

Process = container
Thread = execution unit

---

## Misconception 2

“Threads run in parallel always”

❌ Wrong

- Single core → time slicing
- Multi core → parallel

---

## Misconception 3

“Threads have separate memory”

❌ Wrong

Only stack is separate
Heap is shared

---

## Misconception 4

“More threads = faster always”

❌ Wrong

Too many threads → overhead:

- context switching cost
- cache misses
- memory pressure

---

# 7. Complete Flow Diagram (Text)

Process Created
↓
Memory Space Allocated
↓
Main Thread Created
↓
Additional Threads Spawned
↓
Thread Control Blocks (TCB) Created
↓
Scheduler Picks Thread
↓
Load Thread Context into CPU
↓
CPU Executes Instructions
↓
Thread Requests I/O
↓
System Call to Kernel
↓
Thread Goes Waiting State
↓
Another Thread Scheduled
↓
Context Switch (Save/Restore Registers)
↓
Thread Resumes Execution
↓
Multi-Core Execution (optional parallelism)
↓
Threads Share Heap Memory
↓
Race Conditions Possible
↓
Synchronization Required (locks/mutex)
↓
Threads Continue Execution Loop

---

# 8. Real Software Systems Usage

---

## Chrome

- UI thread
- Renderer thread
- Network thread
- JS engine thread

---

## Node.js

- Single main thread (event loop)
- Worker threads optional

---

## PostgreSQL

- one thread per query (or process model depending on architecture)
- background workers
- WAL writer threads

---

## Java Servers

- thread per request (classic model)
- thread pools (modern model)

---

## React Apps (indirect)

- UI thread (browser main thread)
- rendering pipeline thread
- event loop thread

---

# 9. What Experienced Engineers Understand

Beginners think:

Threads = parallel execution

Engineers think:

Threads = controlled concurrency unit inside shared memory space

---

## Deep Insight 1

Threads are NOT for speed — they are for **responsiveness and structure**

---

## Deep Insight 2

Threads introduce:

- race conditions
- deadlocks
- memory visibility issues

---

## Deep Insight 3

Most real systems avoid raw threads:

They use:

- thread pools
- event loops
- async runtimes

---

## Deep Insight 4

Threads are where OS + CPU + memory + compiler all meet

---

# 10. Summary (5–10 Lines)

- Threads are the smallest unit of execution inside a process.
- A process provides resources; threads execute code.
- All threads in a process share heap memory and resources.
- Each thread has its own stack, registers, and execution state.
- The OS scheduler schedules threads, not just processes.
- Context switching enables multitasking between threads.
- Threads enable responsiveness and concurrency in modern systems.
- Multi-core CPUs allow true parallel thread execution.
- Threads introduce complexity like race conditions and synchronization issues.
- Modern applications rely heavily on threads for performance and structure.

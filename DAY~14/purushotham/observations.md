# Day 14 - CPU Scheduling

## Concept: Scheduling

---

# 1. What Fundamental Problem Does Scheduling Solve?

## Historical Background

Early computers in the 1940s and 1950s were extremely expensive machines.

**Examples:**

- ENIAC (1945)
- UNIVAC I (1951)

These computers were not used by multiple users simultaneously.

The workflow was:

```text
Human Operator
    |
    |
    v
Load Program
    |
    |
    v
Run Program
    |
    |
    v
Collect Result
```

A single program occupied the entire machine until completion.

---

# The Problem

The biggest problem was:

## CPU Wastage

The CPU was much faster than external devices like:

- Magnetic tapes
- Disk drives
- Input devices

**Example:**
A program might execute:

```text
Calculate something
    |
    |
    v
Request data from disk
    |
    |
    v
Wait...
```

During this waiting period:

- **CPU:** `██████████` (Idle)
- **Program:** Waiting for I/O

The most expensive hardware resource was sitting idle.

---

# Multiprogramming Solution

Operating systems introduced the concept of multiprogramming.

Instead of keeping one program in memory:

```text
Memory
+-------------+
| Program A   |
+-------------+
CPU runs A -> (wait) -> CPU idle
```

The OS loaded multiple programs:

```text
Memory
+-------------+
| Program A   |
+-------------+
| Program B   |
+-------------+
| Program C   |
+-------------+
```

Now when Program A waits for I/O:

- **Program A:** Waiting for disk
- **CPU:** Runs Program B

The CPU remains busy.

---

# The Fundamental Question

Once multiple programs existed, a new problem appeared:

```text
Multiple programs want CPU
    |
    |
    v
Only one instruction stream can execute on one CPU core
```

The operating system needed a mechanism to decide:

- Which program runs?
- When does it run?
- How long does it run?
- When should another program get CPU time?

This mechanism is called:

# Scheduling

---

# Scheduling Definition

Scheduling is the operating system mechanism that decides:

> Which process or thread receives CPU execution time and in what order.

---

# Why Scheduling Is Needed

Without scheduling:

- **Program A:** uses CPU forever
- **Program B:** waits forever

**Problems:**

- Poor CPU utilization
- Unfair resource sharing
- Slow response time
- Poor user experience

---

# Modern Example

A modern computer runs hundreds of tasks:

- Chrome
- Music Player
- Keyboard Input
- File System
- Antivirus
- Background Services
- Compiler

But the CPU cores are limited.

**Example:**

- 500 threads
- 8 CPU cores
- Only 8 threads execute at one moment.

Scheduling manages the remaining threads.

---

# Summary

Scheduling solves the fundamental problem:

> Efficiently sharing limited CPU execution time among multiple competing processes and threads.

**The goal is:**

- Keep CPU busy
- Improve performance
- Provide fairness
- Reduce waiting time
- Provide fast response

---

# 2. Components and Data Flow in Scheduling

# Components and Data Flow

Scheduling involves multiple OS components working together.

The complete flow is:

```text
Program
|
|
v
Process
|
|
v
Thread
|
|
v
Ready Queue
|
|
v
Scheduler
|
|
v
Dispatcher
|
|
v
CPU Core
|
|
v
Execution
```

---

# 1. Program

A program is a static file stored on disk.

**Example:**

- chrome.exe
- game.exe
- python.exe

It contains instructions but is not running.

---

# 2. Process

When a program starts, the OS creates a process.

A process contains:

```text
Process
+----------------+
| Memory         |
| Files          |
| Resources      |
| Threads        |
+----------------+
```

A process is an executing instance of a program.

---

# 3. Thread

The CPU does not directly execute processes. The CPU executes threads.

**Example:**

```text
Chrome Process
    |
    |
    +---- Thread 1
    |
    +---- Thread 2
    |
    +---- Thread 3
```

Threads contain the actual execution flow.

---

# 4. Ready Queue

When many threads need CPU time, they cannot all execute simultaneously. Waiting threads are placed in the ready queue.

**Example:**

```text
Ready Queue
---
Chrome Thread
Game Thread
Music Thread
Compiler Thread
Database Thread
---
```

The threads are ready but waiting for CPU allocation.

---

# 5. Scheduler

The scheduler is the OS component responsible for choosing the next thread. It decides: **Who runs next?**

**Example:**
Ready Queue: `A, B, C`
Scheduler chooses: `B`

---

# 6. Dispatcher

The scheduler selects. The dispatcher performs the actual switching.

**Responsibilities:**

- Stop current thread
- Save current state
- Load next thread state
- Give CPU control

---

# 7. CPU Core

The CPU executes instructions from the selected thread.

**Example:**

```text
Thread Selected
    |
    |
    v
CPU Registers
    |
    |
    v
Instruction Execution
```

---

# Context Switching

When the CPU changes from one thread to another, the OS performs context switching.

**Example:**
Currently running: **Thread A**

```text
CPU registers:
Instruction Pointer = 5000
Stack Pointer = 9000
Registers = Current Values
```

The OS saves this information.

Then:

```text
Thread B state
    |
    |
    v
CPU Registers
```

Thread B starts execution.

---

# Complete Scheduling Flow

```text
Application
|
v
Process Creation
|
v
Thread Creation
|
v
Ready Queue
|
v
Scheduler Decision
|
v
Dispatcher
|
v
Context Switch
|
v
CPU Execution
```

---

# Connection With Previous Concepts

### Day 1: Processes

Scheduling chooses between processes/threads.

---

### Day 2: Threads

CPU scheduling actually happens at thread level.

---

### Day 8: Registers

Context switching saves and restores registers.

---

### Day 12: Virtual Memory

Each process has its own virtual memory space while sharing CPU time.

---

# Summary

Scheduling is the bridge between:

```text
Many Programs
    |
Operating System
    |
Limited CPU Resources
```

It allows thousands of tasks to appear to run simultaneously.

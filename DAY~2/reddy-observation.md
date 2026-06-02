# Computer Internals Learning Journal (Top → Bottom Approach)

# Goal

Understand what happens inside a computer from the moment you click an application until the CPU executes instructions.

This document follows a practical, observation-first approach.

---

# Real Observation

Task Manager Screenshot:

![Task Manager Screenshot](Screenshot 2026-05-31 151729.png)

Observed:

- CPU: 37%
- Memory: 78%
- Disk: 2%
- Network: 1%

Top Process:

- Brave Browser (19 processes)
- ~2 GB RAM
- ~25% CPU

Question:

Why does Brave create 19 processes?

We will answer that by building the model from top to bottom.

---

# Layer 1: Applications

Examples:

- Brave
- Chrome
- VS Code
- WhatsApp
- Zoom

These are the things users interact with.

Question:

What happens when I click WhatsApp?

Answer:

Nothing runs directly from storage.

Windows must first load the application.

---

# Layer 2: Program

A Program is a file stored on SSD/HDD.

Examples:

- chrome.exe
- code.exe
- whatsapp.exe

Important:

A program is NOT running.

It is only a file.

Think:

Program = Recipe Book

The recipe exists.

No cooking is happening.

Questions:

- Does a program use CPU?
  - No.

- Does a program use RAM?
  - No.

Because it is only a file.

---

# Layer 3: Process

When you double-click WhatsApp:

whatsapp.exe
↓
Windows loads it into RAM
↓
Creates Process

Definition:

Process = Running instance of a program.

Think:

Program = Recipe Book

Process = Chef currently cooking

Now work is happening.

A process needs:

- RAM
- CPU Time
- Process ID (PID)
- Threads
- Open Files
- Network Connections

---

# Process IDs (PID)

Every process has an ID.

Examples:

Chrome -> PID 1234

VS Code -> PID 4321

PID = Process Identifier

Think:

Citizen
↓
Aadhaar Number

Process
↓
PID

Windows uses PID to identify processes uniquely.

---

# Why WhatsApp Remains After Closing

Observation:

Window closed.

Process still exists.

Why?

Possible work:

- Receive notifications
- Sync messages
- Wait for incoming chats
- Background updates

Closing the window does not always terminate the process.

---

# Layer 4: Threads

Inside every process are workers.

These workers are Threads.

Definition:

Thread = Smallest unit of work executed by CPU.

Think:

Windows = City

Process = Building

Thread = Worker inside building

CPU does not execute processes directly.

CPU executes threads.

Important:

Process
↓
Contains Threads
↓
CPU Executes Threads

---

# Why Applications Need Multiple Threads

Suppose Chrome has:

- UI
- Network Requests
- Video Playback
- Audio Playback

One worker:

Slow

Many workers:

Faster

Therefore:

One Process
↓
Many Threads

---

# Layer 5: CPU

CPU = General Purpose Worker

CPU Responsibilities:

- Execute instructions
- Run application logic
- Execute JavaScript
- Handle operating system tasks
- Manage calculations

Observation:

Infinite Loop:

while(true){}

CPU Usage:

1%
↓
34%

Why?

Because CPU repeatedly executes:

Check condition
↓
Loop again
↓
Check condition
↓
Loop again

Forever.

CPU usage increases when more instructions must be executed repeatedly.

---

# CPU Does NOT Execute Processes

Many beginners think:

CPU executes process.

More accurate:

CPU executes threads belonging to processes.

Flow:

Process
↓
Threads
↓
CPU Executes Threads

---

# Layer 6: CPU Cores

Your CPU:

Intel i5-12500H

Has multiple cores.

Think:

1 Worker
↓
One task at a time

12 Workers
↓
Many tasks simultaneously

This is why:

- Brave
- Zoom
- Audio Service
- Task Manager

can all work together.

---

# Scheduling

Reality:

CPU is not truly running everything at once.

Instead:

Chrome
↓
Zoom
↓
Task Manager
↓
Chrome
↓
Zoom

CPU rapidly switches between tasks thousands of times per second.

This is called Scheduling.

It creates the illusion that everything runs simultaneously.

---

# Layer 7: RAM

Observation:

Opening tabs increased memory.

450 MB
↓
2.9 GB

Why?

Each tab contains:

- HTML
- CSS
- JavaScript
- Images
- Cached Data

RAM stores active data.

Think:

RAM = Study Table

SSD = Bookshelf

You bring books from shelf to table before reading them.

---

# Why RAM Drops After Closing Tabs

Closing tabs:

↓

Data no longer needed.

Windows releases memory.

RAM usage decreases.

Some memory may remain cached for future use.

---

# Layer 8: Storage

Storage Types:

- SSD
- HDD

Your System:

512 GB NVMe Gen4 SSD

Purpose:

Store data permanently.

Examples:

- Windows
- Chrome
- VS Code
- Photos
- Videos

Storage keeps data after shutdown.

RAM does not.

---

# SSD vs RAM

RAM:

- Fast
- Temporary

SSD:

- Slower
- Permanent

Application Startup:

SSD
↓
RAM
↓
CPU Executes

---

# Why SSD Improves Startup Time

Opening application:

SSD Read
↓
Load Into RAM
↓
CPU Executes

Faster SSD
↓
Faster Loading

---

# Why Browsers Use Multiple Processes

Observed:

Brave Browser (19)

Reasons:

## Security

One malicious tab should not access everything.

## Stability

One crashed tab should not crash the entire browser.

## Performance

Multiple processes can better utilize modern CPUs.

---

# Why Applications Crash

Bug occurs.

Invalid memory access.

Windows terminates process.

Result:

Application crashes.

Important:

Program file still exists on SSD.

Only the process died.

---

# Parent and Child Processes

Example:

Chrome
↓
Creates

- Tab Process
- GPU Process
- Extension Process

This is why browsers show many processes.

---

# Complete Mental Model

Program Stored On SSD
↓
User Opens Program
↓
Windows Creates Process
↓
Process Receives RAM
↓
Process Creates Threads
↓
CPU Executes Threads
↓
GPU Draws Graphics (if needed)
↓
Output Appears On Screen

---

# Explain To A 10-Year-Old

Program = Recipe Book

Process = Chef Cooking

Thread = Workers Helping Chef

CPU = Workers Doing Actual Work

RAM = Kitchen Table

SSD = Storage Room

Operating System = Restaurant Manager

---

# Self-Test

1. Program vs Process?
2. Why does a process need RAM?
3. What is a PID?
4. Why does WhatsApp still run after closing?
5. Does CPU execute a process or thread?
6. Why does Chrome use multiple processes?
7. Why does RAM increase when tabs open?
8. Why does CPU increase during an infinite loop?
9. Why does SSD affect startup speed?
10. What is scheduling?

If you can answer all 10 in your own words, you understand the foundations.

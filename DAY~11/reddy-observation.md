# threads

# 1: How did programs work before threads?

first understand how a normal program will work before thread enter.

```text
Start

↓
Read a file

↓
Process the data

↓
Print the result

↓
End
```

The computer performs one step, finishes it completely, and then moves to the next step.

It does NOT do this:

```text
Read File          Process Data
    ↓                   ↓
 Same Time          Same Time
```

The second task starts only after the first task has finished.

## Example

```python
print("Step 1")
print("Step 2")
print("Step 3")
print("Step 4")
```

Output:

```text
Step 1
Step 2
Step 3
Step 4
```

The second `print` waits for the first to finish.

Everything happens in sequence.

### Key Idea

A program originally had a **single flow of execution**.

```text
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
Step 4
   ↓
Step 5
```

Only after Step 1 finishes can Step 2 begin.

> A traditional program executes instructions one after another in a single sequence.

---

# 2: What problem existed with this approach?

 problem was simple:

> If one task takes a long time, after that every task must wait.

Nothing else can happen until the current task finishes.

---

## ex Downloading a file

Program:

```text
Start

↓

Download File

↓

Show "Download Complete"

↓

End
```

Timeline:

```text
0 sec      Start Download

30 sec     Still Downloading

60 sec     Still Downloading

90 sec     Still Downloading

120 sec    Download Finished

121 sec    Show "Download Complete"
```

The next step cannot begin until downloading finishes.

> A traditional program had one execution path. If one operation was busy, every later operation had to wait.

## Why do we create multiple programs for different tasks?

We can divide one big program into multiple smaller programs, where each program is responsible for a specific task.

For example:

```
Program A                  Program B

Download a file            Listen for clicks

Download data              Draw the window

Save the file              Update the screen

Check progress             Handle keyboard input
```

In this example:

* **Program A** is responsible for downloading the file.
* **Program B** is responsible for the user interface (UI).

### But how do they communicate?

Suppose the user clicks the **Download** button.

The UI program (Program B) must tell the download program (Program A) to start downloading.

To make this happen, the programs need a way to communicate with each other. They cannot simply read or change each other's memory directly because each program has its own separate memory space. The operating system protects one program from accessing another program's memory for security and stability.

### Problems with using multiple programs

Using separate programs has several disadvantages:

* More memory is required because each program has its own memory space.
* Communication between programs is slower and more complex.
* Sharing data is harder.
* Creating and managing multiple programs is more complex than managing one.

### A better idea

>Instead of creating a whole new program for every task, we can have **multiple execution paths inside the same program**.
These execution paths are called **threads**.

Since all threads belong to the same process, they:

* Share the same memory.
* Share the same resources.
* Can communicate easily by accessing shared data.
* Use less memory than separate programs.

 example:

```
One Process
────────────────────────────────

Thread 1 → Download a file

Thread 2 → Listen for button clicks

Thread 3 → Draw the window

Thread 4 → Handle keyboard input

(All threads share the same memory)
```
> A thread is the smallest unit of execution inside a process.
>It is an independent execution path that runs as part of a program. Multiple threads can exist inside the same process, and they all share the same memory and resources.


## What belongs to the process?

The process owns shared resources.

For example:

```
balance = 5000

name = "Reddy"

messages = 25
```

Every thread can access them.

```
                Process

        balance = 5000

        name = "Reddy"

              ↑
      -----------------

      Thread 1

      Thread 2

      Thread 3
```

If Thread 1 reads `balance`, it sees 5000.

If Thread 2 reads `balance`, it also sees 5000.

They are looking at the same shared memory.

---

## Does every thread have its own memory?


Every thread has its own private stack.

Example:

Thread 1:

```
x = 10

y = 20
```

Thread 2:

```
x = 100

y = 200
```

These local variables are private.

Changing Thread 1's `x` does not change Thread 2's `x`.

So there are two kinds of memory:

Shared:

```
balance

name

messages
```

Private to each thread:

```
local variables

function calls

temporary values
```

---

# how the thread will created by this own or can we create manually

When you run a program, it already has one thread.

That thread is called the main thread.

```
Process

    Main Thread
```

If you never create another thread, the entire program runs using that single thread.

---

## Who creates extra threads?

The operating system does not automatically create one for every task.

Your program requests them.

Example idea:

```
Create Worker Thread

Start Worker Thread
```

After that:

```
Process

    Main Thread

    Worker Thread

    Worker Thread
```

Some libraries create threads internally, but those libraries are still asking the operating system to create them.

---

## Who manages the threads?

The operating system scheduler manages them.

**ex :** there are three threads:

```
Thread A

Thread B

Thread C
```

The scheduler decides which one gets CPU time.

Example:

```
CPU

5 ms  → Thread A

5 ms  → Thread B

5 ms  → Thread C

5 ms  → Thread A

5 ms  → Thread B
```

---

## how one thread change data used by another thread?

Suppose shared memory contains:

```
balance = 5000
```

Thread 1 changes it:

```
balance = 3000
```

Now the shared memory is:

```
balance = 3000
```

Thread 2 reads:

```
balance
```

It gets:

```
3000
```

Both threads see the same shared value.

---

## The some situation

Suppose:

```
balance = 1000
```

Thread 1 wants to subtract 100.

Thread 2 wants to subtract 200.

Thread 1 reads:

```
1000
```

Thread 2 also reads:

```
1000
```

Thread 1 writes:

```
900
```

Thread 2 writes:

```
800
```

Final result:

```
800
```

Expected result:

```
700
```

Both threads used the old value before either finished updating it.

This kind of bug is called a race condition.


#  How do we avoid Race Conditions?

Using a Lock (Mutex).

Only one thread may enter this section at a time.

Without lock:

```text
Thread A modifies balance

Thread B modifies balance
```

At the same time.

With lock:

```text
Thread A enters

Thread B waits

Thread A exits

Thread B enters
```

The protected code is called a Critical Section.

---

# What if one thread depends on another thread?

Example:

```text
Thread A → Download file

Thread B → Process file
```

Thread B cannot continue until Thread A finishes.

The scheduler does not automatically know this dependency.

The programmer must define it.

Thread B says:

```text
I cannot continue yet.
Put me to sleep.
```

The OS moves it into a waiting state.

```text
Running

↓

Waiting
```

No CPU time is wasted.

---

## When Thread A finishes

Thread A signals:

```text
File is ready
```

The OS moves Thread B from:

```text
Waiting

↓

Ready
```

The scheduler can now run Thread B.

---

## Thread States

```text
            +---------+
            |  Ready  |
            +---------+
                 |
                 v
            +---------+
            | Running |
            +---------+
                 |
       -------------------
       |                 |
       v                 v
 +---------+       +----------+
 | Waiting |       | Finished |
 +---------+       +----------+
       |
       v
 +---------+
 |  Ready  |
 +---------+
```

Ready:
Waiting for CPU.

Running:
Currently executing.

Waiting:
Blocked until some event occurs.

Finished:
Execution completed.

---

# Complete Flow of Process → Threads → Execution

```text
User Starts Program
        │
        ▼
+------------------+
|     Process      |
+------------------+
        │
        ├──────────────────────────┐
        │                          │
        ▼                          ▼

+----------------+      Shared Resources
| Main Thread    |      ----------------
+----------------+      Code
        │              Global Variables
        │              Heap Memory
        │              Open Files
        │
        ├──────────────┬──────────────┐
        │              │              │
        ▼              ▼              ▼

+----------+    +----------+    +----------+
| Thread 1 |    | Thread 2 |    | Thread 3 |
+----------+    +----------+    +----------+

Each Thread Has:

    Stack
    Registers
    Instruction Pointer
    Execution State
```

---

# How Threads Reach The CPU

```text
             Scheduler
                  │
                  ▼

        +------------------+
        | Ready Threads    |
        +------------------+
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼

   Thread A    Thread B    Thread C
```

The scheduler chooses which thread gets CPU time.

---

# Single-Core CPU

Only one thread executes at a time.

```text
Time

0ms    Thread A

5ms    Thread B

10ms   Thread C

15ms   Thread A

20ms   Thread B
```

The CPU rapidly switches between threads.

Result:

```text
Looks Simultaneous

But

Only One Thread Executes At A Time
```

This is:

```text
Concurrency
```

---

# Multi-Core CPU

```text
Core 1 → Thread A

Core 2 → Thread B

Core 3 → Thread C

Core 4 → Thread D
```

All threads execute simultaneously.

This is:

```text
Parallelism
```

---

# Context Switching

```text
CPU Running Thread A
          │
          ▼

Save Thread A Context

    Instruction Pointer
    Registers
    Stack Pointer
    CPU State

          │
          ▼

Load Thread B Context

          │
          ▼

CPU Running Thread B
```

Later:

```text
Restore Thread A Context

Continue Exactly
Where It Stopped
```

---

# Shared Memory Access

```text
            Process

       balance = 5000

               ▲
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼

 Thread A  Thread B  Thread C
```

All threads see the same balance.

Example:

```text
Thread A

balance = 3000
```

Now:

```text
Thread B Reads

balance = 3000
```

because the memory is shared.

---

# Race Condition Flow

Initial:

```text
balance = 1000
```

```text
Thread A
Read 1000
      │
      ├─────────────┐
      │             │
      ▼             │

Scheduler Switches  │
                    │
                    ▼

Thread B
Read 1000
Write 800

                    │
                    ▼

Scheduler Switches
                    │
                    ▼

Thread A
Write 900
```

Final:

```text
900
```

Expected:

```text
700
```

This is a:

```text
Race Condition
```

---

# Lock Flow

Without Lock

```text
Thread A ──┐
           ├── Access Same Data
Thread B ──┘
```

Problem:

```text
Race Condition
```

With Lock

```text
Thread A
Acquire Lock
      │
      ▼

Modify Data

      │
      ▼

Release Lock

      │
      ▼

Thread B Enters
```

Only one thread can access the critical section at a time.

---

# Dependent Threads Flow

Example:

```text
Thread A → Download File

Thread B → Process File
```

Process File depends on Download File.

```text
Thread B Starts
        │
        ▼

File Ready ?

        │
    No  │
        ▼

Waiting State
(Sleep)

        │
        ▼

Thread A Finishes

        │
        ▼

Signal Thread B

        │
        ▼

Ready State

        │
        ▼

Scheduler Gives CPU

        │
        ▼

Thread B Runs
```

No CPU time is wasted while waiting.

---

# complete workflow

```text
Process
│
├── Shared Resources
│     ├── Code
│     ├── Global Variables
│     ├── Heap
│     └── Files
│
├── Thread 1
│     ├── Stack
│     ├── Registers
│     └── Instruction Pointer
│
├── Thread 2
      ├── Stack
      ├── Registers
      └── Instruction Pointer
            │
            ▼

        Scheduler

            │
            ▼

           CPU

            │
            ▼

      Executes Threads

            │
            ▼

Shared Memory Must Be Protected

            │
            ▼

      Locks Prevent
     Race Conditions
```

### thread structure

Thread
│
├── Thread ID
├── State
├── Stack
├── Registers
├── Instruction Pointer
├── Stack Pointer
├── Pointer to PCB
└── Context Information (Context Switching)

## thread works
TCB A
│
├── Instruction Pointer = 0x500
├── Registers
└── Stack Pointer
         │
         ▼

      PCB
         │
         ▼

   Code Section
         │
         ▼

 Instruction at 0x500
         │
         ▼

        CPU
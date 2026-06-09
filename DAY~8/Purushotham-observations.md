# Day 8 - Caches & Registers

## Building an Engineer's Mental Model

> Goal: Understand why Registers and Caches exist, how they are built, how they work internally, and why they are among the most important performance concepts in computing.

---

# 1. Why Was This Concept Invented?

Computers have a fundamental problem:

```text
CPU became faster much faster than RAM.
```

Modern CPUs can execute billions of operations per second.

However, RAM cannot deliver data at the same speed.

This created a bottleneck:

```text
CPU
↓
Needs Data
↓
Waits For RAM
↓
Wastes Cycles
```

Engineers invented:

- Registers
- Cache Memory

to keep the CPU supplied with data and instructions.

Without them, most CPU cycles would be spent waiting instead of computing.

---

# 2. What Problem Existed Before It?

Imagine a chef.

Without registers:

```text
Chef
↓
Needs Ingredient
↓
Walk Somewhere
↓
Get Ingredient
↓
Return
```

For every operation.

Without cache:

```text
Chef
↓
Walk To Warehouse
↓
Get Ingredient
↓
Return
↓
Cook
```

for every ingredient.

Most time is spent fetching, not working.

Computers faced the same problem.

The CPU was faster than memory.

---

# 3. What Would Happen If This Concept Did Not Exist?

Suppose we remove:

```text
Registers
L1 Cache
L2 Cache
L3 Cache
```

and keep only:

```text
CPU
↓
RAM
```

Consequences:

### Massive Waiting

CPU constantly waits for memory.

### Wasted Processing Power

Modern processors become ineffective.

### Slow Applications

Even simple programs feel sluggish.

### Higher Energy Usage

More waiting means more wasted work.

### Modern Computing Becomes Impractical

High-performance software would be impossible.

---

# 4. Explain The Internal Working Step-by-Step

Consider:

```c
int x = 5;
int y = 10;
int z = x + y;
```

---

## Step 1

Program is loaded:

```text
SSD
↓
RAM
```

---

## Step 2

CPU requests instruction.

It first checks:

```text
L1 Cache
```

---

## Step 3

If found:

```text
Cache Hit
```

Instruction is immediately available.

---

## Step 4

If not:

```text
L2 Cache
↓
L3 Cache
↓
RAM
```

until found.

---

## Step 5

Values loaded into Registers.

Example:

```text
R1 = 5
R2 = 10
```

---

## Step 6

ALU performs:

```text
R1 + R2
```

---

## Step 7

Result stored in another register.

```text
R3 = 15
```

---

## Step 8

Result written back to Cache and RAM if necessary.

---

# 5. Explain All Important Components And Why They Exist

## Registers

Fastest memory in the computer.

Located directly inside CPU cores.

Purpose:

```text
Store values currently being processed.
```

---

### General Purpose Registers

Store:

- Numbers
- Addresses
- Intermediate Results

Example:

```text
RAX
RBX
RCX
RDX
```

---

### Program Counter (PC)

Stores:

```text
Address of next instruction.
```

Without it:

```text
CPU doesn't know what to execute next.
```

---

### Stack Pointer (SP)

Tracks:

```text
Top Of Stack
```

Required for:

- Function Calls
- Recursion
- Local Variables

---

### Instruction Register (IR)

Stores:

```text
Current Instruction
```

Example:

```text
ADD R1, R2
```

---

# Cache Memory

Cache is built using SRAM.

Purpose:

```text
Keep frequently used data close to CPU.
```

---

## L1 Cache

Closest to CPU.

Characteristics:

```text
Smallest
Fastest
Per-Core
```

---

## L2 Cache

Characteristics:

```text
Larger
Slightly Slower
```

---

## L3 Cache

Characteristics:

```text
Largest
Shared Across Cores
```

---

# Cache Internals

Each cache entry contains:

```text
Tag
Data
Valid Bit
Control Metadata
```

---

## Tag

Identifies which memory block is stored.

---

## Data

Actual cached bytes.

---

## Valid Bit

Indicates whether cache entry contains usable data.

---

## Metadata

Stores information used by replacement policies.

---

# Cache Lines

Caches do not fetch single bytes.

Instead:

```text
Entire Cache Line
```

Typically:

```text
64 Bytes
```

Example:

Need:

```text
Address 1000
```

CPU loads:

```text
1000 → 1063
```

into cache.

Reason:

Nearby data is often used next.

---

# 6. Cache Organization

A cache cannot store all RAM.

Question:

```text
Where should a memory block go?
```

This creates cache mapping.

---

## Direct Mapped Cache

Each RAM block has:

```text
One Cache Location
```

Example:

```text
RAM Block 0 → Slot 0
RAM Block 100 → Slot 0
```

Advantages:

- Fast
- Simple

Disadvantages:

- Frequent collisions

---

## Fully Associative Cache

Memory block can go:

```text
Anywhere
```

Advantages:

- Few collisions

Disadvantages:

- Expensive hardware

---

## Set Associative Cache

Most modern CPUs.

Example:

```text
8-Way Associative
```

Block may occupy:

```text
Any Of 8 Locations
```

Balances:

- Speed
- Cost
- Efficiency

---

# 7. Cache Hits And Misses

## Cache Hit

Requested data already exists in cache.

Result:

```text
Very Fast
```

---

## Cache Miss

Requested data not in cache.

Must fetch from lower memory levels.

Result:

```text
Slower
```

---

# Types Of Cache Misses

## Cold Miss

First access ever.

---

## Capacity Miss

Cache too small.

---

## Conflict Miss

Two blocks compete for same location.

---

# Cache Replacement Policies

Cache becomes full.

Need room.

Question:

```text
What should be removed?
```

---

## LRU

Least Recently Used.

Remove oldest unused block.

---

## FIFO

First In First Out.

---

## Random

Simple and surprisingly effective.

---

# Cache Write Policies

## Write Through

```text
Update Cache
+
Update RAM Immediately
```

Advantages:

- Safe

Disadvantages:

- Slower

---

## Write Back

```text
Update Cache First
Update RAM Later
```

Advantages:

- Faster

Disadvantages:

- More complex

---

# 8. Show How This Concept Interacts With Other Computer Science Concepts

## CPU

Registers and caches exist to feed the CPU.

---

## RAM

Caches sit between CPU and RAM.

```text
CPU
↓
Cache
↓
RAM
```

---

## Virtual Memory

Addresses eventually become:

```text
Virtual Address
↓
Physical Address
↓
Cache Lookup
```

---

## Processes

Frequently used process data moves into cache.

---

## Threads

Thread execution constantly uses registers.

Context switching saves and restores register values.

---

## Stack

Local variables frequently move:

```text
Stack
↓
Cache
↓
Registers
```

---

## Heap

Objects move:

```text
Heap
↓
Cache
↓
Registers
```

before processing.

---

# 9. Explain Common Misconceptions Beginners Have

## Misconception 1

Cache is just small RAM.

Reality:

```text
Cache = SRAM
RAM = DRAM
```

Different technologies.

---

## Misconception 2

CPU works directly from RAM.

Reality:

```text
RAM
↓
Cache
↓
Registers
↓
CPU
```

---

## Misconception 3

Registers and RAM are similar.

Reality:

Registers are dramatically faster.

---

## Misconception 4

More cache always means faster programs.

Reality:

Depends on access patterns.

---

## Misconception 5

Computation is the bottleneck.

Reality:

Often:

```text
Memory Access
```

is the bottleneck.

---

# 10. Give 5 Challenge Questions For Group Discussion

1. Why can't we build an entire computer using only registers?

2. Why doesn't SRAM replace DRAM completely?

3. Why does sequential array access outperform random access?

4. If cache is faster than RAM, why is cache so small?

5. Why can memory access patterns affect performance more than CPU speed?

---

# 11. Give A Complete Flow Diagram In Text Form

```text
Program Stored On SSD
↓
Loaded Into RAM
↓
CPU Requests Instruction
↓
Check L1 Cache
↓
Check L2 Cache
↓
Check L3 Cache
↓
Fetch From RAM If Necessary
↓
Load Into Registers
↓
ALU Executes Operation
↓
Store Result In Register
↓
Write Result To Cache
↓
Write Result To RAM
↓
Continue Execution
```

---

# 12. Explain How This Concept Appears In Real Software Systems

## Browsers

Frequently accessed JavaScript objects remain cached.

---

## Databases

Performance heavily depends on cache locality.

---

## Game Engines

Data structures are designed around cache efficiency.

---

## Node.js

Hot paths benefit significantly from cache hits.

---

## React & Svelte

Frequently accessed component state benefits from cache reuse.

---

# 13. Explain What Experienced Engineers Think About

Beginners think:

```text
CPU speed determines performance.
```

Experienced engineers think:

```text
Data movement determines performance.
```

Senior engineers focus on:

- Cache locality
- Cache misses
- Memory layout
- Memory access patterns
- Working set size

The key realization:

```text
The CPU is usually waiting for data,
not waiting to compute.
```

---

# Biggest Mental Movie

Imagine:

```js
count++;
```

inside a web application.

```text
Mouse Click
↓
Browser Event
↓
JavaScript Function Executes
↓
State Variable Located
↓
Cache Lookup
↓
Register Load
↓
ALU Adds 1
↓
Result Stored In Register
↓
Result Written To Cache
↓
Result Written To RAM
↓
Framework Detects Change
↓
DOM Updated
↓
GPU Draws New Frame
↓
Monitor Refreshes
↓
User Sees New Value
```

Deepest Hardware View:

```text
User
↓
Browser
↓
JavaScript
↓
Thread
↓
Process
↓
Virtual Memory
↓
MMU
↓
Cache
↓
Registers
↓
ALU
↓
Logic Gates
↓
Transistors
↓
Electrons
↓
Transistors
↓
Logic Gates
↓
Registers
↓
Cache
↓
RAM
↓
Browser
↓
Screen
↓
User
```

---

# 14. Summary

Registers are the fastest memory in a computer and store data actively being processed.

Caches exist because RAM is too slow for modern CPUs.

Cache memory uses SRAM and sits between CPU and RAM.

Modern CPUs use multiple cache levels: L1, L2, and L3.

Caches exploit temporal and spatial locality to improve performance.

Cache hits are fast; cache misses force slower memory access.

Most software performance problems are memory-access problems, not arithmetic problems.

Understanding caches explains why some code structures are dramatically faster than others.

The primary goal of registers and caches is simple:

```text
Keep The CPU Busy.
```

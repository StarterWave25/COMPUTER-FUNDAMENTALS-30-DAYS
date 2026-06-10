# Day ~ 8 [Caches & Registers]

## 1. Why Were Registers And Cache Invented?

### My Assumption:

---

Initially, I thought:

> RAM is already very fast, so why do CPUs need Registers and Cache?

I assumed they were simply faster storage devices.

### My Research:

---

After researching, I found that Registers and Cache were invented to solve two different problems.

Registers solve:

```text
CPU
↓
Current Operation
```

Cache solves:

```text
CPU
↓
RAM Speed Gap
```

As CPUs became faster, engineers discovered that RAM could not keep up with CPU speed.

This created waiting time.

To reduce this waiting:

```text
Registers
↓
Cache
↓
RAM
↓
SSD
```

were organized as a hierarchy.

---

## 2. What Problem Existed Before Them?

### Before Registers

---

Suppose the CPU executes:

```c
int a = 10;
int b = 20;
int c = a + b;
```

Without Registers:

```text
Read a From RAM
↓
Read b From RAM
↓
Perform Addition
↓
Write Result To RAM
```

for every operation.

The CPU would constantly communicate with RAM.

Even though RAM is fast, it is still much slower than the CPU.

---

### Before Cache

---

Even with Registers, the CPU still needs data from RAM.

Example:

```text
CPU Requests Data
↓
Wait For RAM
↓
Continue Execution
```

As CPU speeds increased, this waiting became a major bottleneck.

Engineers needed something between CPU and RAM.

That solution became Cache.

---

## 3. What Would Happen If Registers And Cache Did Not Exist?

### Without Registers

---

The CPU would need to read and write RAM for nearly every operation.

This would make execution significantly slower.

The ALU needs data immediately available for calculations.

Registers provide that immediate workspace.

---

### Without Cache

---

The computer would still work.

However:

```text
CPU
↓
RAM
```

communication would happen much more often.

The CPU would spend more time waiting for RAM.

Applications would feel slower even though the CPU itself remains fast.

---

## 4. Internal Working Step-By-Step

### Registers

---

When the CPU executes an instruction:

```c
int c = a + b;
```

Simplified flow:

```text
a Loaded From RAM
↓
Register
↓
b Loaded From RAM
↓
Register
↓
ALU Performs Addition
↓
Result Stored In Register
↓
Result Written To RAM
```

Registers hold the data needed for the current operation.

---

### Cache

---

Suppose the CPU needs some data.

Step 1

```text
CPU Requests Data
```

Step 2

Check Cache.

```text
Found In Cache?
```

If Yes:

```text
Cache
↓
CPU
```

If No:

```text
RAM
↓
Cache
↓
CPU
```

The Cache keeps frequently used data closer to the CPU.

This reduces RAM access.

---

## 5. Important Components And Why They Exist

### Registers

---

Registers are tiny storage locations inside the CPU.

Purpose:

```text
Store Data Needed Right Now
```

Without Registers:

```text
CPU Must Constantly Access RAM
```

---

### Program Counter (PC)

Purpose:

```text
Stores Address Of Next Instruction
```

Without it:

```text
CPU Would Not Know Which Instruction To Execute Next
```

---

### Current Instruction Register (CIR)

Purpose:

```text
Stores Instruction Being Executed
```

Without it:

```text
Instruction Could Be Overwritten During Execution
```

---

### Memory Address Register (MAR)

Purpose:

```text
Stores Address Being Accessed
```

Without it:

```text
CPU Cannot Tell Memory Which Location Is Needed
```

---

### Memory Data Register (MDR)

Purpose:

```text
Stores Data Moving Between CPU And Memory
```

Without it:

```text
Data Transfer Becomes Difficult To Manage
```

---

### Cache

Purpose:

```text
Stores Frequently Used Data
```

Without it:

```text
CPU Must Access RAM More Often
```

---

### L1 Cache

Closest cache to CPU.

Fastest cache.

Smallest cache.

---

### L2 Cache

Larger than L1.

Slightly slower.

Acts as backup for L1.

---

### L3 Cache

Largest cache.

Shared between CPU cores in many processors.

Acts as backup for L2.

---

## 6. How They Interact With Other Computer Science Concepts

### Registers ↔ CPU

Registers are located inside the CPU.

The CPU performs calculations using values stored in Registers.

---

### Cache ↔ CPU

Cache reduces how often the CPU needs to access RAM.

---

### Cache ↔ RAM

Cache stores frequently accessed data that originally comes from RAM.

---

### RAM ↔ Registers

Data usually moves:

```text
RAM
↓
Registers
↓
ALU
```

before calculations occur.

---

### Operating System ↔ RAM

The Operating System loads processes into RAM.

---

### CPU ↔ Processes

The CPU executes instructions belonging to processes stored in RAM.

---

## 7. Common Misconceptions

### Misconception 1

> Cache and RAM are the same thing.

Reality:

Cache is much smaller and much faster.

---

### Misconception 2

> Registers and Cache are the same.

Reality:

Registers are used for the current operation.

Cache stores frequently used data.

---

### Misconception 3

> Faster CPU automatically means faster programs.

Reality:

CPU speed can be limited by memory access delays.

---

### Misconception 4

> Cache stores entire programs.

Reality:

Cache stores small portions of frequently used data and instructions.

---

### Misconception 5

> Registers store lots of data.

Reality:

Registers are extremely small.

---

## 8. Challenge Questions

1. Why not build an entire computer using only Registers?
2. Why not remove RAM and use only Cache?
3. Why does increasing Cache sometimes improve performance?
4. Why are Registers located inside the CPU?
5. What happens if Cache becomes full?

---

## 9. Complete Flow Diagram

```text
Program Stored In SSD
↓
Operating System Loads Program
↓
RAM
↓
Cache
↓
Registers
↓
ALU / CPU Execution
↓
Result Stored In Registers
↓
Result Written Back To RAM
↓
Permanent Storage To SSD (If Needed)
```

---

## 10. How This Appears In Real Software Systems

### Web Browser

Frequently accessed browser data may remain in Cache.

Active tab data lives in RAM.

Current operations use Registers.

---

### Video Games

Game assets are loaded into RAM.

Frequently used data may remain in Cache.

Current calculations use Registers.

---

### Database Systems

Frequently queried data benefits from Cache.

Current computations use Registers.

---

## 11. What Experienced Engineers Usually Notice

Beginners often focus on:

```text
CPU Speed
```

Experienced engineers often focus on:

```text
Data Movement
```

because moving data is frequently more expensive than performing calculations.

A fast CPU is useless if it constantly waits for memory.

---

## 12. Summary

Registers and Cache were invented to reduce memory access delays.

Registers provide an immediate workspace for the CPU.

Cache reduces the speed gap between CPU and RAM.

Registers are the fastest and smallest storage.

Cache is slower than Registers but faster than RAM.

RAM stores running programs and active data.

Together they form a memory hierarchy:

```text
Registers
↓
Cache
↓
RAM
↓
SSD
```

The biggest thing I learned is:

> Registers help the CPU perform the current operation, while Cache helps the CPU avoid waiting for RAM too often.


---

---

## Deep Dive [Internal Working Of Registers]

### My Assumption:

---

Initially, I thought a Register was simply a tiny memory location inside the CPU.

I knew:

```text
Registers Store Data
Registers Are Fast
```

But I did not know:

* How Registers store bits.
* How the CPU finds a specific Register.
* How values move from Registers to the ALU.
* How results get stored back into Registers.

---

### My Research:

---

After researching, I found that a Register is not a single component.

A Register is actually a collection of tiny memory circuits built from transistors.

Unlike RAM:

```text
RAM
=
Capacitor + Transistor
```

Registers use transistor-based memory circuits that continuously maintain their state while power exists.

This allows Registers to be much faster than RAM.

---

### What Is A Register File?

---

Modern CPUs contain many Registers.

Example:

```text
R0
R1
R2
R3
...
```

Instead of treating them as separate components, the CPU organizes them into a structure called a Register File.

Simplified:

```text
Register File

R0
R1
R2
R3
...
```

The Register File acts as the CPU's ultra-fast internal storage area.

---

### Example Instruction

Suppose the CPU receives:

```assembly
ADD R3, R1, R2
```

Meaning:

```text
R3 = R1 + R2
```

Current values:

```text
R1 = 5
R2 = 10
```

Expected result:

```text
R3 = 15
```

---

### Step 1 - Instruction Reaches CIR

The Fetch Cycle loads the instruction into the Current Instruction Register (CIR).

```text
PC
↓
MAR
↓
Memory
↓
MDR
↓
CIR
```

Now CIR contains:

```assembly
ADD R3, R1, R2
```

---

### Step 2 - Control Unit Decodes The Instruction

The Control Unit reads:

```assembly
ADD R3, R1, R2
```

and extracts:

```text
Operation = ADD

Source Register A = R1
Source Register B = R2

Destination Register = R3
```

---

### Step 3 - Register File Selects Registers

The CPU must now access:

```text
R1
R2
```

Instead of connecting every Register directly to the ALU, the Register File uses selection circuitry.

Simplified:

```text
R0 ─┐
R1 ─┼──► Selector A
R2 ─┼
R3 ─┘
```

```text
R0 ─┐
R1 ─┼──► Selector B
R2 ─┼
R3 ─┘
```

The Control Unit selects:

```text
Selector A = R1
Selector B = R2
```

The Register File outputs:

```text
5
10
```

---

### Step 4 - Values Move To The ALU

Now the ALU receives:

```text
5
10
```

Flow:

```text
R1
 ↓
ALU

R2
 ↓
ALU
```

The Control Unit already specified:

```text
Operation = ADD
```

---

### Step 5 - ALU Performs The Calculation

The ALU executes:

```text
5 + 10
```

Result:

```text
15
```

---

### Step 6 - Result Stored Back Into Register File

The ALU output becomes:

```text
15
```

The Control Unit activates:

```text
Write To R3
```

Flow:

```text
ALU Result
     ↓
Register File
     ↓
R3
```

Final state:

```text
R1 = 5
R2 = 10
R3 = 15
```

---

### Complete Flow Diagram

```text
Instruction Loaded Into CIR
↓
Control Unit Decodes Instruction
↓
Identify Source Registers
↓
Register File Outputs Values
↓
Values Sent To ALU
↓
ALU Performs Operation
↓
Result Produced
↓
Control Unit Selects Destination Register
↓
Result Written Back To Register File
```

---

### Interesting Observation

At first, I thought the CPU somehow "looked around" for Registers.

After researching, I realized that Registers are organized inside a Register File.

The Control Unit does not search for Registers.

Instead, it sends selection signals that immediately activate the required Registers.

This allows the CPU to access Register values extremely quickly.

---

## Final Understanding

A Register is a tiny transistor-based storage circuit located inside the CPU.

Multiple Registers are organized into a Register File.

When an instruction executes, the Control Unit selects the required Registers, sends their values to the ALU, and stores the result back into the destination Register.

The biggest thing I learned is:

> Registers are not just storage locations. They are part of a highly organized hardware structure that allows the CPU to access and process data extremely quickly.


---
---

## Deep Dive [Cache Memory]

### My Assumption:

---

Initially, I thought Cache was simply a place that stores frequently used data.

So I assumed:

> CPU asks for data → Cache stores it → CPU gets it faster.

This is partly correct, but I later discovered that Cache is much more than a simple storage area.

---

### My Research:

---

After researching, I found that Cache exists because there is a huge speed difference between the CPU and RAM.

Simplified:

```text
Registers
↓
Cache
↓
RAM
↓
SSD
```

The CPU can execute instructions extremely quickly.

RAM is much slower compared to the CPU.

If the CPU had to wait for RAM every time it needed data, much of the CPU's time would be wasted waiting.

Cache was invented to reduce this waiting.

---

### The Problem Before Cache

Suppose the CPU needs:

```c
total += arr[0];
total += arr[1];
total += arr[2];
total += arr[3];
```

Without Cache:

```text
CPU
↓
RAM
↓
CPU
↓
RAM
↓
CPU
↓
RAM
```

The CPU repeatedly waits for RAM access.

Even though RAM is fast, it is still much slower than the CPU.

---

### What Cache Solves

---

Cache stores copies of recently accessed memory blocks closer to the CPU.

Flow:

```text
CPU Requests Data
↓
Check Cache
↓
Cache Hit → Return Data
↓
Cache Miss → Fetch From RAM
↓
Store In Cache
↓
Return Data To CPU
```

This reduces expensive RAM accesses.

---

### Cache Does Not Store Single Values

---

One thing I learned is that Cache usually does not load a single value.

Suppose RAM contains:

```text
Address 1000 → A
Address 1001 → B
Address 1002 → C
Address 1003 → D
```

CPU requests:

```text
Address 1000
```

Instead of loading only:

```text
A
```

Cache may load:

```text
A B C D
```

together.

This block is called a:

```text
Cache Line
```

---

### Why Load Multiple Values?

---

Programs often access nearby memory locations.

Example:

```c
for(int i = 0; i < 4; i++)
{
    total += arr[i];
}
```

Access pattern:

```text
arr[0]
arr[1]
arr[2]
arr[3]
```

The CPU predicts that nearby data will likely be needed soon.

So it loads a whole memory block instead of a single value.

This idea is called:

```text
Spatial Locality
```

---

### Cache Hit

---

Suppose Cache already contains:

```text
Tag = Address 1000
Data = A B C D
```

CPU requests:

```text
Address 1002
```

Cache finds the block immediately.

Flow:

```text
CPU
↓
Cache
↓
Data Found
↓
Return Data
```

This is called:

```text
Cache Hit
```

---

### Cache Miss

---

Suppose CPU requests:

```text
Address 5000
```

but Cache does not contain it.

Flow:

```text
CPU
↓
Cache
↓
Not Found
↓
RAM
↓
Load Memory Block
↓
Store In Cache
↓
Return Data
```

This is called:

```text
Cache Miss
```

---

### What Happens When Cache Becomes Full?

---

Cache storage is limited.

Example:

```text
Cache
├── Line A
├── Line B
└── Line C
```

Now CPU needs:

```text
Line D
```

Cache must remove an existing line.

The removed line is chosen using a replacement policy.

Common idea:

```text
Least Recently Used (LRU)
```

Meaning:

```text
Remove the data that has not been used for the longest time.
```

---

### Internal Structure Of Cache

---

A Cache Line stores:

```text
Tag
Data
Status Information
```

Example:

```text
Tag     Data
----    --------
1000    A B C D
```

The Tag identifies which RAM addresses belong to that cache line.

When the CPU requests an address:

```text
Address 1000
```

Comparator circuits check:

```text
Requested Tag
==
Stored Tag ?
```

If they match:

```text
Cache Hit
```

Otherwise:

```text
Cache Miss
```

---

### Why Cache Is Faster Than RAM

---

RAM stores bits using:

```text
Capacitor + Transistor
```

and requires refreshing.

Cache is built using SRAM technology.

SRAM cells use transistor-based memory circuits.

This allows Cache to:

* Respond faster
* Avoid refresh operations
* Stay closer to the CPU

Because of this, Cache is much faster than RAM.

---

### Complete Flow Diagram

```text
Program Running
↓
CPU Needs Data
↓
Check Cache
↓
┌───────────────┐
│ Cache Hit     │
└───────┬───────┘
        ↓
    Return Data

OR

┌───────────────┐
│ Cache Miss    │
└───────┬───────┘
        ↓
      RAM
        ↓
Load Cache Line
        ↓
Store In Cache
        ↓
Return Data
```

---

### Interesting Observation

At first, I thought Cache stored frequently used data.

After researching, I found that Cache mainly tries to keep data that will probably be needed again soon.

This works because most programs repeatedly access recent data and nearby memory locations.

---

## Final Understanding

Cache is a small, extremely fast memory located inside or very close to the CPU.

It acts as a bridge between the CPU and RAM.

Instead of fetching individual values, Cache stores memory blocks called Cache Lines.

When data is found inside Cache, a Cache Hit occurs and the CPU gets the data quickly.

When data is not found, a Cache Miss occurs and the data must be fetched from RAM.

The biggest thing I learned is:

> Cache does not exist to store everything. Cache exists to reduce expensive RAM accesses by keeping recently and nearby-used memory closer to the CPU.


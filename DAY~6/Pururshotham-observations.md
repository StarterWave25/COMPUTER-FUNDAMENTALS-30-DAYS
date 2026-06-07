# Day 6 - Investigating The CPU

**Name:** A. Purushotham

---

# Mission Goal

Today's mission was not to memorize CPU definitions.

The goal was to answer:

> How does a computer actually execute software?

By the end of the investigation, I wanted to understand the journey from:

```text
JavaScript Code
↓
Binary
↓
CPU
↓
Electricity
↓
Transistors
```

---

# The Core Question

Imagine a computer with:

- RAM
- SSD
- Monitor
- Keyboard
- Mouse

but no CPU.

What happens?

Answer:

Nothing.

The computer can store data.

The computer can display data.

But no component can execute instructions.

The CPU is the execution engine of the computer.

Without it:

```text
SSD = Storage
RAM = Temporary Storage
Monitor = Display

No component is actually processing instructions.
```

---

# What Does The CPU Actually Do?

The CPU does not run applications.

The CPU executes instructions.

Example:

```js
let x = 5;
let y = 10;
let z = x + y;
```

The CPU never sees JavaScript.

Eventually this becomes something closer to:

```text
LOAD x
LOAD y
ADD
STORE z
```

The CPU performs billions of these operations every second.

---

# The CPU Execution Cycle

Every CPU follows the same fundamental cycle:

```text
Fetch
↓
Decode
↓
Execute
↓
Repeat
```

---

## Fetch

The CPU fetches the next instruction from memory.

---

## Decode

The CPU determines what the instruction means.

Example:

```text
10110110
```

may represent:

```text
ADD
```

---

## Execute

The CPU performs the requested operation.

Example:

```text
ADD R1,R2
```

The ALU performs the addition.

---

# What Does 3 GHz Mean?

Example:

```text
3 GHz
```

means:

```text
3,000,000,000 clock cycles per second
```

A clock cycle is a synchronization pulse used internally by the CPU.

Important:

```text
GHz ≠ Instructions Per Second
```

Some instructions require multiple cycles.

Modern CPUs may execute multiple instructions during one cycle.

---

# How Does Software Become Binary?

The CPU cannot understand:

```js
console.log("Hello");
```

The instruction must be translated.

Example:

```text
JavaScript
↓
V8 Engine
↓
Machine Code
↓
Binary Instructions
↓
CPU
```

For C:

```text
C
↓
Compiler
↓
Machine Code
↓
CPU
```

---

# How Does The CPU Understand Binary?

The CPU does not understand binary the way humans do.

Binary is simply:

```text
Voltage Present = 1
Voltage Absent  = 0
```

The CPU responds to electrical signals.

---

# Main Components Inside The CPU

```text
CPU
├── Control Unit
├── ALU
├── Registers
├── Cache
└── Cores
```

---

# Control Unit

Responsible for:

```text
Fetch
Decode
Execute
```

Acts like the coordinator of the CPU.

---

# ALU (Arithmetic Logic Unit)

Performs:

```text
Addition
Subtraction
Comparison
AND
OR
XOR
Bit Operations
```

All mathematical and logical operations eventually reach the ALU.

---

# Registers

Registers are the fastest memory inside a computer.

Example:

```text
Register Speed
↓
Cache Speed
↓
RAM Speed
↓
SSD Speed
```

Registers exist because even RAM is too slow for immediate CPU calculations.

---

# Cache

Cache exists because RAM is much slower than the CPU.

Hierarchy:

```text
Registers
↓
L1 Cache
↓
L2 Cache
↓
L3 Cache
↓
RAM
↓
SSD
```

As storage gets larger:

```text
Capacity ↑
Speed ↓
```

---

# Where Does The CPU Fetch Instructions From?

The instruction journey:

```text
SSD
↓
RAM
↓
Cache
↓
Registers
↓
CPU Execution
```

The CPU usually executes instructions loaded into RAM.

---

# Why Are Applications Slow?

Many people assume:

```text
Slow App = Slow CPU
```

This is often incorrect.

Most delays occur because the CPU waits for:

```text
RAM
SSD
Network
Database
User Input
```

The CPU is frequently idle while waiting for data.

---

# Why Do CPUs Have Multiple Cores?

A core is an independent execution unit.

Example:

```text
1 Core
↓
1 Instruction Stream
```

Multiple cores allow multiple instruction streams to run simultaneously.

---

# Do Cores Execute Processes Or Threads?

Cores execute:

```text
Threads
```

not processes.

Example:

```text
Process
├── Thread
├── Thread
└── Thread
```

The operating system schedules threads onto CPU cores.

---

# Electrical Foundations

To understand CPUs deeply, I investigated how electronics perform computation.

---

# Binary At The Electrical Level

Binary represents electrical states.

```text
High Voltage = 1
Low Voltage  = 0
```

Computers are ultimately electrical systems.

---

# The Transistor

A transistor is a tiny electronic switch.

Think:

```text
Electricity In
↓
Switch
↓
Electricity Out
```

When the switch opens:

```text
Current Flows
```

When it closes:

```text
Current Stops
```

Modern CPUs contain billions of transistors.

---

# Logic Gates

Transistors are combined to create logic gates.

Examples:

```text
AND
OR
NOT
XOR
```

Logic gates perform the basic decision-making operations inside computers.

---

# Adders

Adders are circuits built from logic gates.

They perform binary arithmetic.

Example:

```text
0010
+
0011
=
0101
```

Adders are part of the ALU.

---

# Memory Cells

Special transistor arrangements called flip-flops can store bits.

Example:

```text
1 Flip-Flop
=
1 Bit
```

Many flip-flops create registers.

---

# Semiconductors

CPUs are built from silicon.

Pure silicon is neither:

```text
Good Conductor
nor
Good Insulator
```

This makes it a semiconductor.

---

# Doping

Engineers modify silicon by adding impurities.

Examples:

```text
Phosphorus
Boron
```

This creates:

```text
N-Type Silicon
P-Type Silicon
```

which allows electrical behavior to be controlled.

---

# MOSFETs

Modern CPUs use MOSFET transistors.

A MOSFET controls current using an electric field.

```text
Gate Voltage Applied
↓
Channel Forms
↓
Current Flows
```

Remove the voltage:

```text
Channel Disappears
↓
Current Stops
```

This creates a controllable electronic switch.

---

# The Deepest Mental Movie

When a user clicks a button:

```text
Finger Movement
↓
Mouse Signal
↓
Operating System Event
↓
Browser Event
↓
JavaScript Execution
↓
Machine Instructions
↓
Binary Instructions
↓
Voltage Patterns
↓
Transistor Switching
↓
Logic Gates
↓
Adder Circuits
↓
ALU Operations
↓
Register Updates
↓
Memory Updates
↓
Screen Updates
↓
Pixels Change
```

---

# Final Understanding

At the beginning of the mission, a CPU appeared to be a mysterious chip.

After the investigation, I understand that:

```text
Programs
↓
Instructions
↓
Binary
↓
Voltage
↓
Transistors
↓
Logic Gates
↓
Circuits
↓
CPU
```

Every application ultimately becomes billions of transistor state changes occurring every second inside silicon.

The CPU is fundamentally an electrical machine that transforms electrical signals into computation.

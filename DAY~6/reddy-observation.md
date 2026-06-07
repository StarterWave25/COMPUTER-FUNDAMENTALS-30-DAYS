# CPU - Complete Study Notes

# What is a CPU?

## Simple Definition

CPU (Central Processing Unit) is the brain of the computer.

Its job is to:

* Execute instructions
* Process data
* Control the flow of information
* Coordinate all hardware components

Without the CPU, the computer cannot perform any task.

---

# What Happens If There Is No CPU?

Without a CPU:

* Programs cannot run.
* Operating systems cannot start.
* RAM cannot process data.
* SSD can only store data.
* Keyboard and mouse cannot be used.
* Monitor cannot display useful information.

A computer without a CPU is just a collection of hardware components.

---

# CPU's Main Responsibilities

## 1. Process Data

Examples:

* Addition
* Subtraction
* Multiplication
* Division
* Comparison
* Logical operations

---

## 2. Control Data Flow

Examples:

* Read data from RAM
* Store results in RAM
* Communicate with SSD
* Communicate with input/output devices

---

# Important CPU Components

## 1. Control Unit (CU)

### Definition

The manager of the CPU.

### Responsibilities

* Fetch instructions
* Decode instructions
* Control execution
* Coordinate all CPU parts

### Easy Remember

Control Unit = Manager

---

## 2. Arithmetic Logic Unit (ALU)

### Definition

The calculator of the CPU.

### Responsibilities

* Arithmetic operations
* Logical operations
* Comparisons

### Easy Remember

ALU = Calculator

---

## 3. Registers

### Definition

Tiny storage locations inside the CPU.

### Characteristics

* Fastest memory in the system
* Very small capacity
* Stores currently used data

### Easy Remember

Registers = CPU's Desk

---

## 4. Cache

### Definition

High-speed memory near the CPU.

### Purpose

* Store frequently used data
* Reduce RAM access time
* Improve performance

### Easy Remember

Cache = Quick Access Storage

---

## 5. Program Counter (PC)

### Definition

A special register that stores the address of the next instruction.

### Responsibilities

* Tracks execution progress
* Points to next instruction
* Updates after every instruction

### Easy Remember

PC = Instruction Tracker

---

# What is a Transistor?

## Definition

A transistor is an electronic switch.

States:

* ON = 1
* OFF = 0

All modern computers are built from billions of transistors.

### Easy Remember

Transistor = Switch

---

# CPU Building Hierarchy

Transistors

↓

Logic Gates

↓

Circuits

↓

ALU + Registers + Control Unit + Cache

↓

CPU

---

# Logic Gates

Logic gates are built using transistors.

Types:

* AND
* OR
* NOT
* XOR

Purpose:

Process binary data.

### Easy Remember

Logic Gates = Basic Decision Makers

---

# Adder Circuits

Built using logic gates.

Purpose:

Perform binary addition.

Adders become part of the ALU.

### Easy Remember

Adder = Binary Calculator

---

# Binary

Computers use binary.

Binary contains only:

* 0
* 1

Physical Representation:

* Low Voltage = 0
* High Voltage = 1

### Easy Remember

Binary = Computer Language

---

# Does CPU Understand Python or Java?

No.

CPU understands only machine code.

CPU does NOT understand:

* Python
* Java
* JavaScript
* C++
* C

These languages must be translated into machine code.

---

# What is Machine Code?

Machine code is the instruction language of the CPU.

Machine code is stored as binary.

CPU directly executes machine code.

### Easy Remember

Machine Code = CPU Language

---

# What is ISA?

ISA = Instruction Set Architecture

Definition:

The instruction language supported by a CPU.

Examples:

* x86
* ARM
* RISC-V
* MIPS

ISA defines:

* Instructions
* Registers
* Memory rules
* Binary format

### Easy Remember

ISA = CPU Vocabulary

---

# Memory Hierarchy

Fastest → Slowest

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

### Rule

Higher Speed = Smaller Size

Lower Speed = Larger Size

---

# Fetch Decode Execute Cycle

This is the heartbeat of every CPU.

CPU repeats this cycle billions of times every second.

---

## Step 1: Fetch

CPU reads the next instruction from memory.

Uses:

* Program Counter

Output:

Instruction enters CPU.

---

## Step 2: Decode

Control Unit examines the instruction.

Determines:

* What operation to perform
* Which registers to use
* Which hardware component is needed

---

## Step 3: Execute

Required hardware performs the operation.

Examples:

* ALU adds numbers
* ALU compares values
* Data is moved

---

## Step 4: Store Result

Result is written into:

* Register
* Cache
* RAM

---

## Step 5: Update PC

Program Counter moves to next instruction.

Cycle repeats.

---

# Real CPU Workflow

Program Counter

↓

Fetch Instruction

↓

Control Unit Decodes

↓

Load Data Into Registers

↓

ALU Executes Operation

↓

Store Result

↓

Update Program Counter

↓

Next Instruction

---

# Important Data Flow

CPU never directly processes data from RAM.

Actual Flow:

RAM

↓

Registers

↓

ALU

↓

Registers

↓

RAM

### Easy Remember

RAM → Registers → ALU → Registers → RAM

---

# Complete Program Execution (Start To End)

This is one of the most important workflows.

---

## Stage 1: Programmer Writes Code

Human writes:

Source Code

Examples:

* Python
* Java
* C++
* JavaScript

---

## Stage 2: Translation

Compiler or Interpreter converts code.

Source Code

↓

Machine Code

---

## Stage 3: Binary Generation

Machine code becomes binary.

Everything becomes:

0s and 1s

---

## Stage 4: Store on SSD

Binary executable is stored on disk.

SSD stores:

* Program
* Libraries
* Resources

---

## Stage 5: User Runs Program

User double-clicks application.

Operating System receives request.

---

## Stage 6: Operating System Loads Program

Operating System:

* Creates process
* Allocates memory
* Loads executable into RAM

Flow:

SSD

↓

RAM

---

## Stage 7: CPU Starts Execution

Program Counter points to first instruction.

CPU begins:

Fetch

↓

Decode

↓

Execute

---

## Stage 8: Data Loading

Required data moves:

RAM

↓

Registers

---

## Stage 9: Execution

ALU performs operations.

Examples:

* Add
* Compare
* Logical operations

---

## Stage 10: Store Result

Result moves:

ALU

↓

Registers

↓

RAM

---

## Stage 11: Program Continues

Program Counter advances.

CPU executes next instruction.

Billions of times.

---

## Stage 12: Program Ends

Operating System:

* Frees RAM
* Closes process
* Releases resources

Execution completed.

---

# Full End-to-End Layer View

Programmer

↓

Source Code

↓

Compiler / Interpreter

↓

Machine Code

↓

Binary

↓

SSD

↓

Operating System

↓

RAM

↓

Program Counter

↓

Fetch

↓

Decode

↓

Registers

↓

ALU

↓

Registers

↓

RAM

↓

Output

↓

Program Ends

---

# Important Terms To Remember

CPU = Brain

CU = Manager

ALU = Calculator

Registers = CPU Desk

Cache = Quick Storage

RAM = Working Memory

SSD = Permanent Storage

PC = Instruction Tracker

ISA = CPU Vocabulary

Transistor = Switch

Logic Gate = Decision Maker

Machine Code = CPU Language

Binary = 0 and 1

Fetch = Read Instruction

Decode = Understand Instruction

Execute = Perform Operation

Store = Save Result

---

# One-Line Summary

A CPU is a hardware processor built from billions of transistors that repeatedly fetches, decodes, and executes machine-code instructions while controlling the movement of data throughout the computer.

# Day ~ 6 [CPU Fundamentals]

# Observations - Patnam Prudvinath

## Part - 1 [What happens if a computer does not have a CPU?]

### My Assumption:

---

I initially thought the computer might still turn on because RAM, SSD, keyboard, monitor and all other hardware are still connected.

But after researching, I found that all those components can only store data or send signals. None of them can actually understand instructions or decide what to do next.

### My Research:

---

The CPU is the component that continuously reads instructions and executes them.

Without a CPU:

* RAM can store data, but nobody reads it.
* SSD can store programs, but nobody loads them.
* Keyboard can send signals, but nobody processes them.
* The Operating System never starts.

So technically the computer becomes a collection of hardware components that cannot perform any useful work.

A simple way I understood it:

> Programs exist.<br>
> Data exists.<br>
> Instructions exist.<br>
> But nothing executes them.

So a general-purpose computer cannot work without a CPU.

---

## Part - 2 [What does the CPU actually do?]

### My Assumption:

---

Before researching, I know the CPU was will execute instructions, but not how.

### My Research:

---

After reading about the Fetch-Decode-Execute cycle, I realized calculations are only one small part of the CPU's job.

The main responsibility of the CPU is:

* Fetch instructions from memory.
* Decode what those instructions mean.
* Execute those instructions.

This process keeps repeating billions of times every second.

### The Fetch Stage:

---

The CPU first checks the Program Counter (PC).

The PC contains the address of the next instruction.

1. PC copies the address into MAR (Memory Address Register).
2. MAR requests the instruction from memory.
3. The instruction arrives in MDR (Memory Data Register).
4. MDR copies the instruction into CIR (Current Instruction Register).
5. PC moves to the next instruction address.

### The Decode Stage:

---

The Control Unit reads the instruction stored inside CIR.

It separates:

* Opcode → What operation to perform.
* Operand → Which data is needed.

Then the CPU prepares the required resources.

### The Execute Stage:

---

Finally, the CPU performs the actual operation.

Examples:

* Addition
* Multiplication
* Comparing values
* Moving data
* Storing data

If calculations are needed, the ALU (Arithmetic Logic Unit) performs them.

After execution finishes, the CPU immediately starts fetching the next instruction.

---

## Interesting Observation [Why MDR and CIR Both Exist?]

While reading the Fetch-Decode-Execute cycle, I had a doubt.

If the instruction already exists in MDR, why copy it again into CIR?

After understanding it better, I found:

* MDR is a temporary memory-transfer register.
* CIR stores the instruction currently being executed.

During execution, the CPU may need MDR again to fetch additional data from memory.

If the instruction stayed only inside MDR, it would get overwritten.

So the CPU moves the instruction into CIR and keeps it safe while MDR gets reused for other memory operations.

This separation allows the CPU to execute instructions while still communicating with memory at the same time.

## Main Components I Found:
Control Unit (CU) → Directs the operations inside the CPU.<br>
ALU (Arithmetic Logic Unit) → Performs calculations and comparisons.<br>
Registers → Tiny ultra-fast storage locations inside the CPU.<br>
RAM → Not part of the CPU, but constantly communicates with it.

## [How Instructions Are Stored]

The CPU understands these binary instructions using something called an Opcode.

Every instruction contains:

Opcode → What operation to perform.
Operand → The data or memory location involved in the operation.

Example:

LOAD_A 14

Here:

LOAD_A = Opcode
14 = Operand

The CPU reads the opcode first and then performs the corresponding action.

## [What Controls the Speed of the CPU?]

I also learned about the CPU Clock.

The CPU Clock generates regular electrical pulses.

Each pulse tells the CPU to move forward in its work.

Example:

Fetch
↓
Decode
↓
Execute
↓
Next Instruction

The clock helps synchronize these operations.

CPU speed is measured in Hertz (Hz).

Examples:

1 Hz = 1 cycle per second
1000 Hz = 1000 cycles per second
1 MHz = 1 million cycles per second
1 GHz = 1 billion cycles per second

Modern processors operate at several GHz, meaning they can perform billions of clock cycles every second.

## Part - 3 [Code to Binary what CPU see - Practically wathcing what CPU actually sees from my code]

![C to Aseembly](cToAssembly.png)

### What Triggered This Question?

After learning about the CPU, registers, ALU, and the <br>Fetch → Decode → Execute cycle, a new question came to my mind.

We write programs like:

> int a = 5;<br>
let a = 5;<br>
a = 5<br>

But the CPU only understands binary instructions.

So my doubt was:

>If developers write code in human-readable languages, how does that code eventually become something the CPU can execute?

My Initial Thought

>At first, I assumed every programming language directly becomes Assembly and then Binary.

After researching, I found that this is mostly true for learning purposes, but different languages actually take different routes before reaching machine code.

The common thing is:

Source Code<br>
    ↓<br>
Some Translator<br>
    ↓<br>
Machine Code<br>
    ↓<br>
CPU

No matter which language is used, the CPU eventually receives machine instructions.

Understanding the Complete Flow with C

Since Assembly is easier to understand than raw binary, I decided to follow the journey using C.

### Example<br>
int a = 5;<br>

Stage 1 - Source Code 
---

This is the code written by the developer.

int a = 5;

At this point it is just plain text inside a file.

The CPU has no idea what this means.

Stage 2 - Compiler
---

The compiler reads the C code and translates it into Assembly Language.

Example:

mov eax, 5

Which roughly means:

Move the value 5 into register EAX

This was the first time I saw something that looked closer to what the CPU actually executes.

Stage 3 - Assembler
---

The assembler converts Assembly into Machine Code.

Example:

mov eax, 5

becomes:

10111000 00000101

Now the instruction is in binary form.

At this stage, the CPU can finally understand it.

Stage 4 - Loading Into Memory
---

The Operating System loads the machine code into RAM.

SSD<br>
 ↓<br>
RAM<br>
 ↓<br>
Ready To Execute

The program is no longer just a file on disk.

It is now a running process in memory.

Stage 5 - CPU Execution
---

The CPU begins executing instructions.

Fetch<br>
 ↓<br>
Decode<br>
 ↓<br>
Execute

The machine instruction is decoded and executed.

Result:

EAX = 5

The CPU has successfully performed the operation.

Complete C Journey
--
C Source Code <br>
      ↓ <br>
Compiler <br>
      ↓ <br>
Assembly <br>
      ↓ <br>
Assembler <br>
      ↓ <br>
Machine Code <br>
      ↓ <br>
RAM <br>
      ↓ <br>
CPU <br>
      ↓ <br>
Fetch → Decode → Execute  <br>

How Other Languages Reach the CPU
---
Java
--
Java Source Code <br>
      ↓ <br>
javac <br>
      ↓ <br>
Bytecode (.class) <br>
      ↓ <br>
JVM <br>
      ↓ <br>
Machine Code <br>
      ↓ <br>
CPU <br>

Python 
--

Python Source Code <br>
      ↓ <br>
Python Bytecode  <br>
      ↓ <br>
Python Interpreter <br>
      ↓ <br>
Machine Code <br>
      ↓ <br>
CPU <br>

JavaScript (Chrome)
--
JavaScript Source Code <br>
      ↓ <br>
V8 Engine <br>
      ↓ <br>
Bytecode <br>
      ↓ <br>
JIT Compiler <br>
      ↓ <br>
Machine Code <br>
      ↓ <br>
CPU


-------------

# [How the CPU Understands Binary Instructions]



## Part - 1 [What Changed Computers from Calculator-Like Machines to Fast Modern Systems?]

### My Assumption:

---

I initially thought modern computers became fast mainly because modern RAM is much more powerful than older RAM.

### My Research:

---

After researching, I found that faster RAM is only one part of the story.

The real improvement came from multiple technologies advancing together:

* Faster CPUs
* Faster RAM
* Cache Memory
* Better CPU Architectures
* Faster Storage Devices
* Smaller and More Efficient Transistors

One interesting thing I learned is that modern CPUs are often much faster than RAM.

This creates a problem:

> The CPU can execute instructions very quickly, but it must wait for data to arrive from memory.

To reduce this waiting time, engineers introduced Cache Memory.

### Simplified Memory Flow

---

CPU <br>
↓ <br>
L1 Cache <br>
↓ <br>
L2 Cache <br>
↓ <br>
L3 Cache <br>
↓ <br>
RAM <br>
↓ <br>
Storage <br>

Frequently used data is stored closer to the CPU, allowing instructions to be executed much faster.

### My Understanding

---

Computers did not become fast because of a single invention.

They became fast because CPU speed, memory systems, storage technology, and processor design improved together.

One major breakthrough was reducing the amount of time the CPU spends waiting for data.

---

## Part - 2 [Who Converts My Code into Binary?]

### My Assumption:

---

I assumed pre-programmed software such as compilers and interpreters convert code into binary.

### My Research:

---

This assumption was mostly correct.

The CPU cannot understand programming languages such as:

```c
int a = 5;
```

or

```javascript
let a = 5;
```

These are human-readable languages.

Before the CPU can execute them, they must be translated into machine instructions.

### Example Flow Using C

---

Source Code <br>
↓ <br>
Compiler <br>
↓ <br>
Assembly Language <br>
↓ <br>
Assembler <br>
↓ <br>
Machine Code (Binary) <br>
↓ <br>
CPU <br>

### Interesting Observation

---

While researching, another question came to my mind.

> If compilers convert programs into machine code, who converted the compiler itself?

I found that the earliest compilers were written using Assembly Language and Machine Code.

Over time, newer compilers were built using older compilers.

This process is called:

> Bootstrapping

---

## Part - 3 [How Does the CPU Understand Binary Instructions?]

### My Assumption:

---

I knew the CPU executes binary instructions, but I had no idea how it actually understands them.

### My Research:

---

The biggest thing I learned was:

> The CPU does not actually "understand" binary the way humans understand language.

Instead, it is physically built to react to specific binary patterns.

### Example

Suppose engineers decide:

0001 = ADD <br>
0010 = SUBTRACT <br>
0011 = LOAD <br>
0100 = STORE <br>

These rules are built directly into the CPU's hardware design.

When a particular binary pattern arrives, specific circuits inside the CPU become active.

### Simplified Flow

---

Binary Instruction <br>
↓ <br>
Instruction Decoder <br>
↓ <br>
Control Signals <br>
↓ <br>
Hardware Circuits Activated <br>
↓ <br>
Operation Executed <br>

The CPU is not reading binary like a language.

Instead, the hardware reacts automatically to specific bit patterns.

---

## Part - 4 [How Does Hardware React to Binary?]

### My Research:

---

To understand this better, I followed the path all the way from transistors to the CPU.

### Step 1 - Transistors

---

A transistor acts like a tiny electronic switch.

Very simplified:

Voltage Present → ON (1) <br>
No Voltage → OFF (0) <br>

This creates the foundation for binary.

### Step 2 - Logic Gates

---

By connecting transistors together, engineers create Logic Gates.

Examples:

* AND Gate
* OR Gate
* NOT Gate

These gates perform simple logical operations using binary values.

### Step 3 - Adders

---

Engineers combine multiple logic gates to create Adders.

Adders are circuits that can perform binary addition.

Example:

1 + 1 = 10

The circuit produces the result automatically through electrical signals.

### Step 4 - ALU

---

Multiple arithmetic circuits are combined together to create the:

Arithmetic Logic Unit (ALU)

The ALU can perform:

* Addition
* Subtraction
* Comparisons
* Logical Operations

### Step 5 - CPU

---

The ALU becomes one major part of the CPU.

A simplified view looks like:

Transistors <br>
↓ <br>
Logic Gates <br>
↓ <br>
Adders <br>
↓ <br>
ALU <br>
↓ <br>
CPU <br>

---

## Interesting Observation

At first I imagined the CPU was reading binary instructions and somehow translating them like a human reading words.

After researching, I realized something surprising:

> The CPU does not learn binary instructions.

> The CPU is physically designed so that certain binary patterns automatically activate specific electrical circuits.

Because these pathways already exist in hardware, operations happen extremely fast.

The CPU is not thinking about instructions.

It is simply allowing electrical signals to travel through pre-built pathways inside the chip.

---

## Final Understanding

The CPU does not understand binary like a language.

Binary instructions are simply electrical patterns.

When those patterns enter the CPU:

Binary Instruction <br>
↓ <br>
Decoder <br>
↓ <br>
Control Signals <br>
↓ <br>
ALU / Registers / Other Hardware <br>
↓ <br>
Result Produced <br>

Everything ultimately comes down to billions of tiny transistors acting as electrical switches.

By combining those switches into larger and larger circuits, engineers created Logic Gates, Adders, ALUs, and eventually modern CPUs capable of executing billions of instructions every second.

-----------

# [Inside the CPU, Registers, Instruction Fetching & Why Applications Become Slow]

## Part - 1 [What Are The Main Parts Inside The CPU? Why Are They Needed?]

### My Assumption:

---

I knew the CPU executes instructions, but I was not sure which internal components actually make that possible.

### My Research:

---

After researching, I found that the CPU is not a single component.

Instead, it is made up of several specialized components that work together to execute instructions.

### Simplified CPU Structure

---

Instruction <br>
↓ <br>
Control Unit <br>
↓ <br>
Registers <br>
↓ <br>
ALU <br>
↓ <br>
Result <br>

### Main Components I Found

---

### Control Unit (CU)

The Control Unit acts like a coordinator.

Its job is to:

* Fetch instructions
* Decode instructions
* Generate control signals
* Direct data movement inside the CPU

Without the Control Unit, all CPU components would exist but would not know when or how to work together.

---

### ALU (Arithmetic Logic Unit)

The ALU performs calculations and logical operations.

Examples:

* Addition
* Subtraction
* Comparisons
* AND
* OR
* NOT

Whenever a program performs calculations, the ALU is usually involved.

---

### Registers

Registers are tiny storage locations inside the CPU.

Their purpose is to temporarily hold:

* Instructions
* Addresses
* Operands
* Results

They are used constantly during instruction execution.

---

### Cache Memory

Cache stores frequently used data closer to the CPU.

Instead of accessing RAM repeatedly, the CPU first checks cache memory.

Simplified Memory Hierarchy:

CPU <br>
↓ <br>
Registers <br>
↓ <br>
Cache <br>
↓ <br>
RAM <br>
↓ <br>
Storage <br>

---

### Clock

The clock generates timing signals.

It keeps CPU operations synchronized.

Without the clock, different parts of the CPU would operate at unpredictable times.

---

## Interesting Observation

At first, I thought the ALU was the most important part of the CPU.

After researching, I realized that calculations are only one part of execution.

The Control Unit and Registers are equally important because they organize and supply the data needed by the ALU.

---

## Part - 2 [Why Do Registers Exist If RAM and Cache Already Exist?]

### My Assumption:

---

I assumed Registers exist because they are very close to the CPU and therefore faster than RAM and Cache.

### My Research:

---

My assumption was mostly correct.

However, I learned that physical distance is only one reason.

Registers are designed to be the fastest storage locations in the entire computer.

### Why Registers Are Faster

---

### 1. Registers Are Inside The CPU

RAM is located outside the CPU.

Even Cache is a separate memory structure inside the processor.

Registers are directly connected to the CPU's execution units.

This reduces access time significantly.

---

### 2. Registers Are Very Small

Modern computers may have:

* Gigabytes of RAM
* Megabytes of Cache

But only a small number of Registers.

Because they are tiny, they can be accessed almost instantly.

---

### 3. Simpler Access

To read RAM:

CPU <br>
↓ <br>
Memory Controller <br>
↓ <br>
Memory Bus <br>
↓ <br>
RAM <br>

To read a Register:

CPU <br>
↓ <br>
Register <br>

Much less work is required.

---

### Example

Suppose the CPU needs to calculate:

5 + 10

Instead of repeatedly reading values from RAM, the CPU first loads them into Registers.

RAM <br>
↓ <br>
Registers <br>
↓ <br>
ALU <br>
↓ <br>
Result Register <br>

This allows calculations to happen much faster.

---

## Interesting Observation

I originally thought Cache was the fastest memory.

After researching, I found:

Registers are faster than Cache.

Cache is faster than RAM.

RAM is faster than Storage.

---

## Part - 3 [From Where Does The CPU Fetch Instructions?]

### My Assumption:

---

I thought the CPU fetches instructions from special registers such as CIR.

### My Research:

---

I discovered that instructions are actually fetched from RAM.

The CIR only stores the instruction currently being executed.

### Instruction Fetch Flow

---

Program Stored In RAM <br>
↓ <br>
Program Counter (PC) <br>
↓ <br>
Memory Address Register (MAR) <br>
↓ <br>
RAM <br>
↓ <br>
Memory Data Register (MDR) <br>
↓ <br>
Current Instruction Register (CIR) <br>
↓ <br>
Decode & Execute <br>

### Role Of Important Registers

---

### Program Counter (PC)

Stores the address of the next instruction.

---

### MAR

Stores the memory address being accessed.

---

### MDR

Temporarily stores data received from memory.

---

### CIR

Stores the instruction currently being executed.

---

## Interesting Observation

I originally thought instructions permanently live inside CIR.

After researching, I realized:

Instructions live in RAM.

CIR only acts as temporary storage during execution.

---

## Part - 4 [What Is The Actual Reason Applications Become Slow?]

### My Assumption:

---

I assumed applications become slow because the CPU constantly switches between multiple running applications.

### My Research:

---

This can happen, but it is only one possible reason.

Applications can become slow for several different reasons.

### Reason 1 - CPU Bottleneck

---

The CPU is busy performing calculations.

Example:

* Video Rendering
* Scientific Simulations
* Game Physics

CPU Usage → High

---

### Reason 2 - RAM Bottleneck

---

Too many applications consume available RAM.

The Operating System starts moving data between RAM and Storage.

RAM Full <br>
↓ <br>
Disk Used As Extra Memory <br>
↓ <br>
System Slows Down <br>

---

### Reason 3 - Storage Bottleneck

---

Applications may spend time waiting for files.

Storage <br>
↓ <br>
Data Request <br>
↓ <br>
CPU Waits <br>

---

### Reason 4 - Network Bottleneck

---

Many applications depend on the internet.

Slow Network <br>
↓ <br>
Application Waits <br>
↓ <br>
Feels Slow <br>

---

### Reason 5 - Context Switching

---

This is the reason I initially thought of.

Modern operating systems rapidly switch the CPU between tasks.

App A <br>
↓ <br>
App B <br>
↓ <br>
App C <br>
↓ <br>
App D <br>

This creates the illusion that everything runs simultaneously.

Too much switching creates overhead and can reduce performance.

---

## Interesting Observation

I used to think a slow application automatically meant a slow CPU.

After researching, I learned that applications often spend much of their time waiting.

Waiting for:

* RAM
* Storage
* Network
* User Input

In many cases, the CPU is not the real bottleneck.

---

## Final Understanding

A CPU is made of multiple components working together:

Control Unit <br>
↓ <br>
Registers <br>
↓ <br>
ALU <br>
↓ <br>
Execution <br>

Registers exist because even Cache and RAM are too slow for immediate calculations.

Instructions are fetched from RAM and temporarily stored in CIR during execution.

Applications become slow for many reasons, including CPU limitations, memory shortages, storage delays, network delays, and excessive context switching.

The biggest thing I learned is:

> A slow computer is not always caused by a slow CPU. The actual bottleneck can exist anywhere in the path between Storage, RAM, Cache, Registers, and the CPU itself.

# [CPU Cores, Processes, Threads & Parallel Execution]

## Part - 1 [Why Does A CPU Have Multiple Cores?]

### My Assumption:

---

I knew modern CPUs have multiple cores, but I was not sure why they were needed.

Since CPUs are already extremely fast, I wondered why one powerful CPU could not simply execute everything by itself.

### My Research:

---

Initially, CPUs had only a single core.

A single-core CPU can execute only one thread at a time.

Example:

Task A <br>
↓ <br>
Task B <br>
↓ <br>
Task C <br>

Even though this switching happens extremely quickly, only one task is actually executing at any given instant.

---

As software became more complex, a problem appeared.

A single core had to handle:

* Operating System
* Browser
* Music Player
* Games
* Background Services

All at the same time.

This forced the CPU to constantly switch between tasks.

### Single-Core CPU

---

Core 1 <br>
↓ <br>
Task A <br>
↓ <br>
Task B <br>
↓ <br>
Task C <br>
↓ <br>
Task D <br>

Only one task can execute at a time.

---

### Multi-Core CPU

---

Core 1 → Task A <br>
Core 2 → Task B <br>
Core 3 → Task C <br>
Core 4 → Task D <br>

Now multiple tasks can execute simultaneously.

---

### Why Not Just Increase CPU Speed?

---

For many years, manufacturers increased CPU clock speed.

Example:

500 MHz <br>
↓ <br>
1 GHz <br>
↓ <br>
2 GHz <br>
↓ <br>
3 GHz <br>

Eventually, higher clock speeds created problems:

* More heat
* More power consumption
* More cooling requirements

Instead of making one core infinitely faster, engineers started adding more cores.

This allowed more work to be done in parallel.

---

## Interesting Observation

At first, I thought more cores simply meant a faster CPU.

After researching, I found that:

> More cores do not necessarily make a single task faster.

Instead:

> More cores allow multiple tasks to run at the same time.

---

## Part - 2 [Do CPU Cores Execute Processes or Threads?]

### My Assumption:

---

I assumed CPU cores execute Processes.

### My Research:

---

I discovered that CPU cores actually execute Threads.

This was one of the biggest things I learned.

---

### Process

A Process is an independent running program.

Examples:

* Chrome
* VS Code
* Spotify
* Discord

Each running application usually creates a process.

---

### Thread

A Thread is the actual unit of execution inside a process.

Example:

Chrome Process

├── Thread 1 → UI <br>
├── Thread 2 → Rendering <br>
├── Thread 3 → Network Requests <br>
└── Thread 4 → JavaScript Execution <br>

One process can contain multiple threads.

---

### What Does The CPU Execute?

---

Operating System Scheduler <br>
↓ <br>
Select Thread <br>
↓ <br>
Assign To CPU Core <br>
↓ <br>
Execute <br>

The CPU never executes an entire process directly.

It executes one thread at a time.

---

## Interesting Observation

I originally thought:

Process = Execution Unit

After researching, I found:

Process = Container

Thread = Execution Unit

The CPU executes threads, not processes.

---

## Part - 3 [Even If A CPU Is Fast, Why Can't It Simply Execute Threads One After Another?]

### My Assumption:

---

I thought the CPU already executes threads one after another.

### My Research:

---

My assumption is partially correct.

A single core really does execute threads one after another.

Example:

Thread A <br>
↓ <br>
Thread B <br>
↓ <br>
Thread C <br>

This switching happens so quickly that users feel everything is happening simultaneously.

---

### Example

Suppose:

* Music Playing
* Video Downloading
* Typing In Browser

Single Core:

Music <br>
↓ <br>
Browser <br>
↓ <br>
Download <br>
↓ <br>
Music <br>
↓ <br>
Browser <br>

The CPU rapidly switches between them.

This is called:

> Context Switching

---

### The Problem

Imagine four heavy tasks:

* Video Rendering
* Game Physics
* AI Model
* File Compression

With one core:

Core 1

Task A <br>
↓ <br>
Task B <br>
↓ <br>
Task C <br>
↓ <br>
Task D <br>

All tasks must wait for turns.

---

With four cores:

Core 1 → Task A <br>
Core 2 → Task B <br>
Core 3 → Task C <br>
Core 4 → Task D <br>

Now all tasks execute simultaneously.

---

### Why This Matters

Suppose every task requires:

10 seconds

Single Core:

10 + 10 + 10 + 10 = 40 seconds

Four Cores:

≈ 10 seconds

Because work is divided across multiple cores.

---

## Interesting Observation

A single-core CPU creates the illusion of multitasking through rapid switching.

A multi-core CPU provides actual parallel execution.

This was an important distinction I had not understood before.

---

## Part - 4 [How The Operating System Uses CPU Cores]

### My Research:

---

The Operating System contains a component called the Scheduler.

The Scheduler decides:

* Which thread should run
* Which core should run it
* How long it should run

### Simplified Flow

---

Threads Waiting <br>
↓ <br>
Scheduler <br>
↓ <br>
Available Core <br>
↓ <br>
Execution <br>

The Scheduler continuously repeats this process thousands of times every second.

---

## Final Understanding

A CPU contains multiple cores because a single core can execute only one thread at a time.

Modern computers run many applications simultaneously, making parallel execution necessary.

I originally thought CPU cores execute processes.

After researching, I learned:

Process <br>
↓ <br>
Contains Threads <br>
↓ <br>
CPU Executes Threads <br>

A single-core CPU performs multitasking through rapid context switching.

A multi-core CPU allows true parallel execution by running multiple threads at the same time.

The biggest thing I learned is:

> A Process is a container, but a Thread is the actual unit of execution. CPU cores execute threads, not processes.

# Process 

# 1. Before the Concept of a Process Existed

The old computers there is no concept of a process.

They had:

* CPU
* Memory
* Input devices
* Output devices

The CPU simply executed instructions stored in memory.

Conceptually:

```text
        +---------+
        |  CPU    |
        +---------+
             |
             v
        +---------+
        | Memory  |
        +---------+
```

The CPU did not know:

* Programs
* Processes
* Users
* Applications
* Operating Systems

It only knew:

```
Fetch Instruction
        ↓
Decode Instruction
        ↓
Execute Instruction
        ↓
Fetch Next Instruction
        ↓
Repeat
```

---

# 2. How Programs Were Executed

The program was loaded into memory.

```text
Memory

+----------------------+
| LOAD A               |
| ADD B                |
| STORE C              |
| HALT                 |
+----------------------+
```

The CPU executes the instructions one by one using the Program Counter (PC).

```text
Program Counter
      |
      v

Memory

0 -> LOAD A
1 -> ADD B
2 -> STORE C
3 -> HALT
```

It worked well, but why do we need processes?

When an instruction is running, it may need some I/O devices or other data to read or write. To get that data, it has to wait, and this waiting takes a lot of time. During this time, the CPU remains idle, wasting its processing power.

Instead of:

```text
Program A

(waiting)

CPU idle
```

why not we can keep it like this:

```text
Program A waiting
        |

CPU ---> Program B

Program B waiting
        |

CPU ---> Program C
```

Now the CPU is always busy.
---

# 3. But it is not an easy task. What happens when we switch programs?

The main problem is that the CP U registers store the data of the currently running program. When another program is loaded, the register values are replaced with the new program's data. If we later switch back to the old program without saving its register values, all of its previous execution state is lost.

**Example:**

Program A is running.

CPU registers:

```text
PC = 150

R1 = 20

R2 = 50

SP = 9000
```

Now switch to Program B.

Program B needs the CPU registers, so the old values are replaced with Program B's data. It starts executing with:

```text
PC = 900

R1 = 5

R2 = 100

SP = 4000
```

When Program A comes back:

```text
Where was I?

No idea.
```
---
# 4. Technique for Storing a Program's Execution State

## Instead of remembering only the program code:

They decided to save:

• Program Counter (PC)

• Registers

• Stack

• Memory Information

• Running State

• Other Execution Information

                CPU

             Running A
                 │
                 ▼
        Save complete state
                 │
                 ▼
        Load Program B state
                 │
                 ▼
             Run Program B
                 │
                 ▼
        Save Program B state
                 │
                 ▼
       Reload Program A state
                 │
                 ▼
 Continue exactly where A stopped

>Result: **By saving the complete execution state**, no information is lost, and the program can continue exactly from where it was paused.

---

# 5. Now We Introduce the Process

The above technique is known as a **process**.

Engineers did not invent processes because programs could not run.

Programs were already running.

They invented the **process abstraction** because they needed a reliable way to:

* Pause a running program
* Save its execution state
* Run another program
* Resume the first program exactly where it left off

This idea made **multitasking** practical and became one of the fundamental concepts of modern operating systems.

```text
          Program
              │
              │ (Start Execution)
              ▼

    +------------------------+
    |        PROCESS         |
    |------------------------|
    | Code                   |
    | Data                   |
    | Heap                   |
    | Stack                  |
    | Registers              |
    | Program Counter (PC)   |
    | Open Files             |
    | Execution State        |
    +------------------------+
```

## Real Definition

A <span style="font-size: 18px;">**process**</span> is a program in execution. It includes the program's code and its current execution state, such as the program counter, registers, stack, heap, memory, open files, and other resources needed to run and resume correctly.

``It is the information needed to execute that program correctly.
``
---
# 6. How Does the Operating System Save a Process's Execution State?

The CPU does **not** save registers or execution state on its own. It simply executes instructions.

When the operating system needs to pause a process (for example, during multitasking), it runs instructions that copy the CPU's current state into memory.

Example:

```text
STORE R1 -> Memory[1000]
STORE R2 -> Memory[1001]
STORE R3 -> Memory[1002]
STORE PC -> Memory[1003]
```

After execution:

```text
Memory

1000 -> R1 Value (25)
1001 -> R2 Value (80)
1002 -> R3 Value (150)
1003 -> PC Value (103)
```

The CPU is simply following these instructions and copying the values into memory.

The **operating system itself is also a program** stored in memory, just like any user program.

```text
+----------------------+
| Operating System     |
+----------------------+

+----------------------+
| User Program         |
+----------------------+
```

When required, the CPU executes the operating system's instructions, which save the process state. Later, the operating system restores those saved values, allowing the process to continue exactly from where it stopped.

# 7. How Does the CPU Start Executing the Operating System?

> CPU contain special hardware called **Interrupt Logic**.

Conceptually, the CPU looks like this:

```text
+---------------------------+
|            CPU            |
|---------------------------|
| Control Unit              |
| Registers                 |
| Arithmetic Logic Unit     |
| Interrupt Logic           |
+---------------------------+
```

The **Interrupt Logic** is real hardware built into the CPU.

Its job is to continuously monitor interrupt signals coming from hardware devices such as:

* Keyboard
* Timer
* Mouse
* Disk Controller
* Network Card

When an interrupt signal arrives, the CPU temporarily stops its normal execution and transfers control to the operating system so it can handle the event.

---

# 8. What Is an Interrupt?

An **interrupt** is a hardware signal that tells the CPU:

> **"Stop what you're doing for a moment and handle this important event."**

For example, when you press a key:

```text
Keyboard
     │
     │ Interrupt Signal
     ▼
+-------------+
|     CPU     |
+-------------+
```

Or when the hardware timer expires:

```text
Timer
     │
     │ Interrupt Signal
     ▼
+-------------+
|     CPU     |
+-------------+
```

These are actual electrical signals generated by hardware devices.

Without interrupts, the CPU would have to constantly check every device itself, wasting valuable processing time.

---
## How Does an Interrupt Come?

An interrupt is a signal sent to the CPU to notify it that an event has occurred and needs immediate attention.

### 1. Keyboard Interrupt

When you press a key:

```text
Press Key
     │
     ▼
Keyboard Controller
     │
Interrupt Signal
     │
     ▼
+-------------+
|     CPU     |
+-------------+
```

The keyboard hardware sends an electrical interrupt signal to the CPU.

---

### 2. Timer Interrupt

The computer has a hardware timer that generates interrupts at regular intervals.

```text
Hardware Timer
       │
       │ Interrupt Signal
       ▼
+-------------+
|     CPU     |
+-------------+
```

The operating system uses these timer interrupts for multitasking and scheduling.

---

### 3. Disk Interrupt

When a disk finishes reading or writing data:

```text
Disk Controller
        │
Interrupt Signal
        │
        ▼
+-------------+
|     CPU     |
+-------------+
```

The CPU is notified that the requested operation has completed.

---

### What Happens Next?

```text
Device Generates Interrupt
            │
            ▼
Interrupt Signal Reaches CPU
            │
            ▼
CPU Finishes Current Instruction
            │
            ▼
CPU Saves Required State
            │
            ▼
CPU Jumps to Interrupt Handler
            │
            ▼
Operating System Handles the Event
            │
            ▼
Program Resumes Execution
```

**In simple words:** An interrupt is just a hardware or software signal that says, **"CPU, something important has happened. Please handle it."**

---


---

# 8. What Is a Program?

A program is simply a collection of instructions stored on disk.

Example:

```
calculator.exe
```

It is only a file.

By itself, it does nothing.

---

## . What Is a Process?

A process is a program together with everything required for execution.

It includes:

* Program code
* Data
* Stack
* Heap
* Program Counter
* CPU registers
* Execution state
* Open resources

Conceptually:

```
+---------------------------+
|         Process           |
|---------------------------|
| Program Code              |
| Data                      |
| Heap                      |
| Stack                     |
| Program Counter           |
| CPU Registers             |
| Execution State           |
| Open Resources            |
+---------------------------+
```

---

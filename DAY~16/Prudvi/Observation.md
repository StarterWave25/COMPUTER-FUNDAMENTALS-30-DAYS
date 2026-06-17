# PATNAM PRUDVINATH - OBSERVATION ON "SYSTEM CALLS"

## Part - 1 [Purpose of Inventing System Calls]

```
So in Early Days the User Written Programs are able to Directly access the Hardware.
-> They can access - RAM, Disk, CPU, Printer, Keyboard.
```
```
Problem 1:
- Programs could destroy the entire system.
  - Something like "Write to Random Access" will leads to
  - OS Corrupted, Others Programs Corrupted -> System Crash.

- So Users programs should not access the Hardware.
```

```
Problem 2:
- But still Programs need to:
  - Read File
  - Write File
  - Allocate memory
  - Create Process
  - Send Data to Network.
- But if we allow direct access:
  - Security Problems
  - Stability Problems
  - Resource Conflicts will appear...

```

```
So they need to:
- Protect Hardware
- Protect Other Programs

- And programs need to use Hardware. 
```

```
So they, created OS as a gate Keepter. But,
 - How does a user program ask the OS to do something?

So this becomes 
  - Programs -> System call -> Kernel -> Hardware
```

```
And system call is not just a function, it's a permission request to access Hardware.
```

## Part - 2 [Data & Data Flow]

```
Data Here:
- File Names
- Memory Requests
- Process Information
- Network Data
- Keyboard Input
- Data To Write
- Data To Read
```

```
Components & Flow:

User Program
[Needs OS Service]

↓

System Call Interface
[Gateway Between User Space & Kernel Space]

↓

Kernel
[Validates Request & Chooses Appropriate Service]

↓

Kernel Subsystem
[File System / Memory Manager / Process Manager / Network Stack]

↓

Hardware
[Disk / RAM / CPU / Network Card]

↓

Kernel
[Receives Result]

↓

System Call Return Value
[Success, Failure, or Requested Data]

↓

User Program
[Continues Execution]
```

### And there is something like modes in Computer to operate this System calls effectively...

**1. User Mode** - Where our programs, No need to access for Hardware.<br>
**2. Kernel Model** - Where our programs run without limits.

What Happens During A System Call?

```
Suppose Python executes:

open("data.txt")

Step 1
CPU is currently in:
User Mode

Step 2
Python triggers:
System Call

Step 3
CPU performs:

Mode Switch
User Mode
↓
Kernel Mode

Step 4
Kernel executes:

Open File
Read Metadata
Check Permissions

Step 5
Result prepared.

Step 6
CPU switches back:

Kernel Mode
↓
User Mode

Step 7
Python receives result.
```
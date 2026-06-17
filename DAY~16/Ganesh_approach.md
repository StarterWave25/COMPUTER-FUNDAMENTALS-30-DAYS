# System Calls

## What Fundamental Problem Did System Calls Solve?

### Historical Background

In the earliest computers (1940s–1950s), there was no operating system as we know it today. A single program was loaded into memory and executed directly on the hardware. The program had complete control over the machine.

The application could:

* Access memory directly
* Control hardware devices
* Read and write storage devices
* Execute privileged CPU instructions

This worked because only one program was running at a time.

### Problem 1: Multiple Programs

As computers became more expensive and valuable, organizations wanted to run multiple programs on the same machine.

Example:

```text
Program A
Program B
Program C
```

If every program could directly access hardware, one program could accidentally overwrite another program's data.

Result:

* Data corruption
* System instability
* Program interference

---

### Problem 2: Hardware Protection

Hardware resources are shared and sensitive.

A buggy program might execute:

```c
while(1){
    write_to_disk();
}
```

or

```c
disable_interrupts();
```

Such actions could make the entire system unusable.

The operating system needed a way to prevent applications from directly controlling hardware.

---

### Problem 3: Security

In multi-user systems:

* User A owns some files
* User B should not access those files

Without protection, a program could bypass security and directly read disk sectors.

Example:

```text
Read sector 5000
```

This completely bypasses file permissions.

---

### Historical Solution

Operating systems introduced two execution modes:

#### User Mode

Applications run here.

Restrictions:

* Cannot access hardware directly
* Cannot execute privileged instructions
* Cannot modify kernel memory
* Cannot manage other processes

#### Kernel Mode

The operating system runs here.

Capabilities:

* Hardware access
* Memory management
* Process management
* Device control

---

### The New Problem

If applications cannot access hardware directly:

**How can they request services from the operating system?**

The answer is:

# System Calls

A system call provides a controlled gateway between user programs and the kernel.

```text
Application
      |
      v
System Call
      |
      v
Kernel
      |
      v
Hardware
```

---

## Mental Model

Imagine a bank vault.

Customers cannot enter the vault directly.

Instead:

```text
Customer
    |
Request Form
    |
Bank Employee
    |
Vault
```

Mapping:

* Customer → Application
* Request Form → System Call
* Employee → Kernel
* Vault → Hardware

The customer asks for a service. The employee verifies the request and performs the operation safely.

---

# Components and Data Flow

Consider:

```c
printf("Hello");
```

Eventually, this becomes:

```c
write()
```

which is a system call.

---

## Components

### 1. User Program

The application code written by the developer.

Example:

```c
write(fd, buffer, size);
```

---

### 2. C Library

Libraries such as libc provide convenient wrapper functions.

Example:

```c
write()
```

Internally, the wrapper prepares the system call.

---

### 3. System Call Interface

The CPU executes a special instruction such as:

```assembly
syscall
```

or

```assembly
int 0x80
```

This transfers execution from user mode to kernel mode.

---

### 4. Kernel

The kernel receives the request and validates it.

Example:

```text
Write 5 bytes to stdout
```

---

### 5. Device Driver

The kernel communicates with the appropriate device driver.

Example:

```text
Display these bytes
```

---

### 6. Hardware

The hardware performs the requested operation.

Example output:

```text
Hello
```

---

## Data Flow Example

Program:

```c
write(1, "Hi", 2);
```

Flow:

```text
User Program
      |
      | fd=1
      | buffer="Hi"
      | size=2
      v
System Call
      |
      v
Kernel
      |
      v
Terminal Driver
      |
      v
Screen
```

Output:

```text
Hi
```

---

# What Happens Inside the CPU?

Before the system call:

```text
CPU Mode = User Mode
```

Application executes:

```assembly
syscall
```

The CPU performs:

1. Saves current execution state
2. Switches to kernel mode
3. Jumps to kernel handler

The kernel executes the requested service.

After completion:

```assembly
sysret
```

The CPU:

1. Restores saved state
2. Switches back to user mode
3. Continues executing the application

---

# Small Program: Simulating System Calls

## Mini Kernel

```python
class MiniKernel:

    def handle_syscall(self, call, *args):

        if call == "write":
            print(args[0])

        elif call == "getpid":
            return 1001

        else:
            raise Exception("Unknown syscall")
```

---

## User Program

```python
kernel = MiniKernel()

kernel.handle_syscall("write", "Hello")

pid = kernel.handle_syscall("getpid")

print(pid)
```

Output:

```text
Hello
1001
```

Conceptually:

```text
User Program
      |
      v
handle_syscall()
      |
      v
Kernel Service
```

---

# Breaking the Program

A systems engineer must always ask:

> What can go wrong?

---

## Edge Case 1: Unknown System Call

```python
kernel.handle_syscall("hack")
```

Result:

```text
Exception
```

---

## Edge Case 2: Missing Arguments

```python
kernel.handle_syscall("write")
```

Result:

```text
IndexError
```

Kernel crashes.

---

## Edge Case 3: Huge Input

```python
kernel.handle_syscall("write", "A" * 1000000000)
```

Possible consequences:

* Memory exhaustion
* Performance degradation
* Application freeze

---

## Edge Case 4: Wrong Data Type

```python
kernel.handle_syscall("write", 123)
```

Unexpected behavior may occur.

---

## Edge Case 5: Unauthorized Requests

```python
kernel.handle_syscall("shutdown")
```

If no permissions exist, any application could shut down the system.

---

# Optimized Version

```python
class MiniKernel:

    MAX_SIZE = 1000

    def handle_syscall(self, call, *args):

        if call == "write":

            if len(args) != 1:
                return "ERROR"

            data = args[0]

            if not isinstance(data, str):
                return "ERROR"

            if len(data) > self.MAX_SIZE:
                return "TOO LARGE"

            print(data)
            return "OK"

        elif call == "getpid":
            return 1001

        else:
            return "UNKNOWN SYSCALL"
```

---

## Improvements

The optimized version protects against:

* Missing arguments
* Invalid data types
* Oversized requests
* Unknown system calls

---

# How Real Operating Systems Protect Themselves

When Linux receives:

```c
read(fd, buffer, size);
```

The kernel performs several checks:

1. Is the file descriptor valid?
2. Does the process own the descriptor?
3. Is the memory address accessible?
4. Is the requested size reasonable?
5. Is the device available?
6. Does the process have permission?

Only after validation does the kernel execute the request.

---

# Common System Calls

| System Call | Purpose                       |
| ----------- | ----------------------------- |
| read()      | Read data                     |
| write()     | Write data                    |
| open()      | Open a file                   |
| close()     | Close a file                  |
| fork()      | Create a process              |
| exec()      | Execute a program             |
| wait()      | Wait for a child process      |
| mmap()      | Map memory into address space |
| socket()    | Create a network socket       |
| connect()   | Connect to a remote server    |

---

# Complete Mental Model

```text
Application
     |
     | System Call
     v
Kernel
     |
     +--> Process Management
     |
     +--> Scheduler
     |
     +--> Memory Manager
     |
     +--> File System
     |
     +--> Network Stack
     |
     +--> Device Drivers
     |
     v
Hardware
```

Everything an application wants to do—creating processes, reading files, allocating memory, communicating over networks, or interacting with devices—ultimately goes through a system call.

A system call is the controlled doorway between user-space applications and the privileged kernel.

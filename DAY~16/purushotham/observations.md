# Day 16 --- System Calls

## 1. Fundamental Problem System Calls Solve

Before operating systems became powerful, programs directly controlled
hardware.

A program had to know:

- How the disk works
- How memory works
- How the keyboard/display works
- How hardware controllers communicate

This created major problems:

1.  Every program became hardware dependent.
2.  Programs could damage each other's memory.
3.  Any program could perform dangerous operations.
4.  Resource management became impossible.

The operating system solved this by creating a controlled interface
between applications and hardware.

That interface is called **System Calls**.

---

# 2. What is a System Call?

A system call is a controlled request from a user program to the
operating system kernel.

A normal application cannot directly access hardware.

Instead:

    Application
          |
          |
     System Call
          |
          |
     Kernel
          |
          |
     Hardware

The program requests a service, and the kernel performs the operation.

Examples:

- Opening a file
- Reading data
- Creating a process
- Allocating memory
- Sending network data

---

# 3. User Mode and Kernel Mode

Modern operating systems separate execution into privilege levels.

## User Mode

Where normal applications run:

Examples:

- Browser
- Games
- Editors
- User programs

Restrictions:

- Cannot directly access hardware
- Cannot modify kernel memory
- Cannot execute privileged instructions

---

## Kernel Mode

Where the operating system runs.

The kernel can:

- Access hardware
- Manage memory
- Schedule processes
- Control devices

The CPU switches to kernel mode only through controlled mechanisms.

---

# 4. Why This Separation Exists

Without protection:

A program could:

- Delete important files
- Modify another program's memory
- Disable hardware
- Crash the entire system

The kernel acts as a security boundary.

Applications request.

The kernel decides.

---

# 5. System Call Data Flow

Example:

```c
read(fd, buffer, 100);
```

Meaning:

"Kernel, read 100 bytes from this file."

Flow:

    User Program

          |
          v

    Library Function

          |
          v

    System Call Instruction

          |
          v

    CPU switches User Mode -> Kernel Mode

          |
          v

    Kernel System Call Handler

          |
          v

    Kernel Subsystem

          |
          v

    Device Driver

          |
          v

    Hardware

---

# 6. CPU Mode Switching

A system call is not a normal function call.

Normal function:

    Function A
         |
         v
    Function B

System call:

    User Program

         |
         |
     syscall instruction

         |
         v

    Kernel Entry Point

The CPU:

1.  Saves current execution information.
2.  Changes privilege level.
3.  Jumps to kernel code.
4.  Executes the requested operation.
5.  Returns back to user mode.

---

# 7. Passing Data to Kernel

The user program passes information through CPU registers.

Example:

    Register

    RAX -> System call number

    RDI -> First argument

    RSI -> Second argument

    RDX -> Third argument

Example:

    write(fd, buffer, size)

    RAX = write syscall number
    RDI = file descriptor
    RSI = buffer address
    RDX = size

---

# 8. System Call Table

The kernel maintains a mapping between syscall numbers and kernel
functions.

Example:

    Number        Function

    0             read()

    1             write()

    2             open()

    3             close()

The kernel receives:

    syscall number

Then:

    System Call Number

            |

            v

    System Call Table

            |

            v

    Correct Kernel Function

---

# 9. System Call Handler

The basic kernel flow:

    System Call Entry

            |

    Save registers

            |

    Check syscall number

            |

    Find function in syscall table

            |

    Execute kernel function

            |

    Return result

---

# 10. Trap vs Syscall Instruction

Older systems used general software interrupts:

    int 0x80

Modern systems use:

    syscall

The syscall instruction is optimized specifically for entering kernel
mode.

---

# 11. Library Wrapper vs Real System Call

Programmers usually do not directly call system calls.

Example:

    printf()

does not directly become:

    Kernel

Usually:

    Application

        |

        v

    Library (glibc)

        |

        v

    System Call

        |

        v

    Kernel

Libraries provide:

- Easier APIs
- Error handling
- Portability
- Buffering

---

# 12. Blocking System Calls

Some operations need waiting.

Example:

```c
read(socket, buffer, 100);
```

If data is not available:

The process should not waste CPU.

Instead:

    Process

    calls read()

          |

          v

    Kernel puts process to sleep

          |

          v

    CPU runs another process

          |

          v

    Data arrives

          |

          v

    Process wakes up

---

# 13. Non-Blocking System Calls

A non-blocking call returns immediately.

Example:

    Request data

            |

    Data available?
            |
            |
           No

            |

    Return immediately

Used heavily in:

- Servers
- Networking
- High-performance applications

---

# 14. Security Checks During System Calls

The kernel never trusts user input.

Before performing operations it checks:

## Memory validation

Is the provided address valid?

## Permission checking

Does this user have access?

## Resource limits

Does this process have enough resources?

## File descriptor validation

Is this file handle valid?

---

# 15. System Call Performance

System calls have overhead because they require:

    User Mode

         |

    CPU privilege switch

         |

    Kernel Mode

         |

    Return

         |

    User Mode

Optimizations:

## Reduce unnecessary system calls

Bad:

    write()
    write()
    write()

Better:

    combine data

    write()

---

## Buffering

Libraries store data and perform fewer system calls.

Example:

    printf()

          |

    buffer

          |

    one write syscall

---

## vDSO

Some operations avoid entering the kernel.

Example:

Getting time can sometimes happen directly through shared
kernel-provided memory.

---

# 16. Simple System Call Program

Example using Linux write syscall:

```c
#include <unistd.h>

int main()
{
    char msg[] = "Hello System Calls\n";

    write(
        1,
        msg,
        sizeof(msg)
    );

    return 0;
}
```

Explanation:

    write(
        file descriptor,
        buffer,
        size
    )

File descriptors:

    0 -> stdin

    1 -> stdout

    2 -> stderr

---

# 17. Breaking the Program

Testing failure cases:

## Invalid file descriptor

    write(999, ...)

Kernel rejects it.

---

## Invalid memory address

    write(1, invalid_address, size)

Kernel prevents unsafe access.

---

## Huge size request

    write(1, buffer, huge_number)

Kernel validates memory boundaries.

---

# 18. Connection With Previous Concepts

## Processes

Processes use system calls to request OS services.

## Threads

Every thread can execute system calls.

## Virtual Memory

Kernel checks whether user addresses are valid.

## CPU

CPU provides instructions to switch privilege levels.

## Memory Protection

System calls maintain isolation between programs.

---

# Final Mental Model

A system call is a safe bridge:

    Application

          |

          v

    System Call Interface

          |

          v

    Kernel

          |

          v

    Hardware

The application asks.

The kernel validates.

The kernel performs the operation.

The result returns safely.

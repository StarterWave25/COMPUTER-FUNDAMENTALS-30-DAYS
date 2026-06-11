# **Process**

## **Why Process was invented and what problem it solves?**
### **Problem:**
- In the early 1950s computers, the programs are directly loaded into the memory, CPU executed from beginning to end and there is no concept of multitasking, no protection & no resource management.
- CPU uitilization is very poor because when a program is waiting for Disk Reading or writing, Input, printer operations during these operations the CPU is idle.
- In 1960s, multiprogramming was introduced which is like loading the multiple programs into the memory and if one program blocks for I/O then save its execution state and run another program. This increased CPU utilization.
- But the OS needs a way to represent the program execution state because now the program is not just code. The OS needs to remember its current instruction, register values, files it opened, stack & heap used, etc.

### **Solution:**
- So that representation is called a Process.
- A process is a program in execution together with all information which is needed to resumes its execution later.
- It consists of Execution Context, Memory Context, Resource Context and Scheduling Context.
---


## **What happens if Process don't exists?**
- If process don't exists then we cannot implement the multiprogramming & multiprocessing because these two methods need a program execution state has to be stored. So that they can pause & resume their execution. But if they don't exists then we cannot store the program's execution state.
- Memory corruption may happens as One program can overwrite the another program memory without a seperate assigned memory space for different programs.
- OS cannot manage which resources own by which program and it is difficult the release the unused resources by the programs.
- Security on Programs cannot be implemented because without the identification of a program it is difficult allow which process can read, write, modify the memory.
---


## **What are the Components inside the Process?**

### When a program execution wants to resume by the OS, How does CPU know where it stopped?
- The OS needs to save its Program Counter, CPU Registers, CPU Flags, etc.
- All the information which is related execution of a program comes under ``Execution Context``.

### How every program maintains their function calls seperately?
- For every function call they need seperate memory to maintain their function calls, local variables, return addresses, etc.
- To store all of them each program has their own ``Stack``.

### How runtime memory allocation of a program takes place?
- For every program it needs seperate memory that can grow dynamically and exists until explicitly released.
- And stack cannot maintain because the memory is released implicitly whenever a function is executed. So, we need a seperate region which is called ``Heap``.

### Where the program instructions are stored?
- When a program is executing, the CPU needs compiled machine code instructions. It needs seperate memory region which is called ``Code Segment``.

### Where the global variables of a program are stored?
- The global variables of a program has to live until the process lifetime. So, they cannot be stored in stack or heap.
- They need a seperate memory region that is called ``Data Segment``. It stores all the Global & Static variables of a process.

### How does OS know which process owns files?
- The OS needs to track which files a process is owned so that they cannot be allocated to other processes.
-  To track that OS maintains ``File Descriptor Table`` for every process.

### How does OS know which process has to run next?
- The OS needs a process state, priority, CPU usage and some scheduling parameters to allocate the CPU to a process.
- ``Scheduling information`` stores all the scheduling parameters.

### How does OS identifies a process and terminate it?
- Every process should be identified uniquely for that each process is assigned a unique ID called ``Process ID``.

### How does OS know parent & childs of a process?
- ``Process Related Information`` contains Parent PIDs, Child PIDs, Process Group & Session info.

### Where does OS stores the entire information of process?
- This is where PCB comes in it is data structure like an object which contains all the information & references related to a process.
- If PCB contains Stack, Heap then the OS should copy all the memory to PCB. It creates redundancy. So, only references to the Stack and Heap are only stored in it.
---


## **From Process Creation to Termination**
### 1. When double click on chrome.exe, the OS receives a request to create a process.
### 2. Kernal creates a PCB with PID, ``NEW`` state and Creates Address space, Load Machine Code into the Code Segment.
### 3. Kernal initializes Execution Context with PC = main(), Stack Pointer = TOS, Registers with inital values.
### 4. The scheduler places the process into Ready Queue. Now its state is ``READY``.
### 5. Schedular decides the process with PID should run next. Kernal performs context load like copying the registers from PCB into CPU Registers.
### 6. Now CPU has next instruction address into PC. CPU Repeatedly perform fetch, decode & execute. The Process state is ``RUNNING``.
### 7. Suppose CPU needs memory to read data then CPU provides the virtual address but RAM uses physical address. MMU translates the address into physical address.
### 8. If a function call happens then OS creates a stack frame and updates stack pointer. When function returns stack frame is removed & stack pointer is updated.
### 9. If an instruction needs to allocate dynamic memory then the OS Kernal expands the heap and process gets the memory.
### 10. Suppose the timer interrupt occurs then current process is interrupted and CPU state is preserved and the kernal saves them into PCB. This is called ``Context Saving.``
### 11. Now, schedular chooses another process and kernal loads PCB of another process. This is called ``Context Switching``.
### 12. And the old process is in waiting queue with ``BLOCKED`` State.
### 13. Whenever the old process needs to execute then the schedular places it into Ready Queue and the schedular selects it again.
### 14. When the process completes its execution then the Kernal perform cleanup. It releases memory, close files, remove scheduling info, destroy PCB. Now, the process state is ``TERMINATED``.
---

## What experienced software engineer thinks about process?
- Process creates a boundary on memory, files, resources for different programs.
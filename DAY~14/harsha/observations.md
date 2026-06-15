# Scheduling

## Why Scheduling exists and what problem it solves fundamentally?
1. In the early industrial period, factories had multiple jobs has to be done with workers & machines but there is no systematic way to decide like which worker should get the machine and how much time a worker should with and which work should be completed first.
2. Without a clear plan on what we need to do we will end up by wasting resources & time.
3. For to build the clear plan, scheduling was introduced as a process of deciding the order & time of the work.
4. In the early computers like ENIAC could execute a single program at a time. The CPU spent most of its time as idle.
5. So, the problem was to keep the expensive resources like CPU, Printer, Memory, Disk, etc busy not idle because many tasks need them to complete their task.

### To solve this someone needs to manage the resources in an order between the tasks. And it is called the Schedular.



## Why each component in scheduling exists?

### How does schedular knows which process needs to get the resources?
1. The schedular needs a list of processes which are waiting to store the waiting processes in a place.
2. ``Ready Queue`` is introduced which stores all the processes that are ready to execute by the CPU.

### How does schedular selects the process to execute?
1. Schedular can select a process randomly but it is inefficent because some processes may have urgency & some may execute at less time.
2. Schedular needs some rules to select a process from the ready queue. Those rules are ``Scheduling Algorithms``.

### How does long processes are stopped for to give resources to short processes?
1. To solve the problem, for all processes should have a time limit to stop the execution and to begin the next process.
2. For that ``Timer`` is introduced, whenever a process executes upto a particular time. A timer interrupt is generated and CPU stops executing and begins the next process.

### How does processes with different states are organized?
1. Processes generally have New, Ready, Running, Waiting, Terminated states. To organize them they are stored in different queues except running & terminated processes.
2. Process with New State are stored in ``Job Queue``, processes with Ready State are stored in ``Ready Queue`` and processes with waiting state are stored in ``Wait Queue/Device Queue.``

### Schedular only selects the processes in the ready queue. It doesn't give the CPU Contorl to selected process, then who?
``Dispatcher`` performs the context swtiching first then CPU gets the execution context then CPU executes the instructions.


### Three types of schedulars are there:
#### 1. Long term scheduler: At a time, too many processes want to enter into memory like for example 1000 tasks. Only 50 jobs can hold by the memory. The CPU Schedular cannot solve this because those processes are not in memory yet. To solve this ``Long Term Schedular`` was introduced. Without it all processes will enter into the memory & memory fills up. It contorls the multiprogramming.

#### 2. Medium term schedular: What if the memory was full? And some processes are inactive like waiting for user input for several minutes and removing them doesn't effect anything. To remove these type of processes the ``Medium term schedular`` is used. It manages the memory utilization by removing the inactive processes.

### 3. Short term schedular: It selects the processes which are ready to run by the CPU and which are present in the ready queue.



## Flow of Scheduling
1. The program is present in disk as app.exe.

2. When user double clicks on app.exe the OS receives a request to create a process with PCB and it has NEW as state.

3. OS creates a virtual address space in Kernal memory with range of addresses which are assigned only for this program.

4. The page table by mapping the virtual addresses with physical address is stored in RAM.

5. And only necessary which are needed to execute the process are loaded into RAM.

6. Now, the process is in READY state and enters into Ready Queue to wait for the CPU.

7. Short term schedular selects the process from the ready queue using a scheduling algorithm.

8. Now, Dispatcher loads the registers, program counter, switch address space and CPU is now assigned to this process. State changes to RUNNING.

9. CPU reads PC and fetches instruction, decoder decodes the instruction and CPU executes it. This cycle repeats.

10. When an instruction needs RAM then CPU requests the virtual address and MMU converts into physical address.

11. RAM access the address if the page is not present then CPU triggers Page fault. 

12. Now, OS locate the page from the disk, the disk requests for IO as disk is much slower than CPU. Process states changes to WAITING after saving its execution context. Schedular picks another process and CPU switches to that.

13. Disk controller signals interrupt to OS and OS changes the process state to READY again and moves into ready queue.

14. Again the short term schedular selects it and dispatcher performs the context switch.

15. CPU repeats the cycle of fetch, decode, execute in billion times and also the process switches between states.

16. After completion of its execution, the exit() system call is executed and process state is changed to TERMINATED and OS cleans all the resources.
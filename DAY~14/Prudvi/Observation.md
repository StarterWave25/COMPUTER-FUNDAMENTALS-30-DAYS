# PATNAM PRUDVINATH - OBSERVATION ON COMPUTER SCHEDULINGss...

## Part - 1 [History & Purpose of Computer Scheduling]

```
1. We know Many Process need CPU - to execute it.. But the CPU can only execute only one thing at a time.
```

```
2. Early days mostly CPU time goes on - waiting, YES waitng for Humans(in 1940), waiting for I/O, waiting for punch cards.

- So CPU most of the time sits IDLE.
```

```
Question for Birth of Scheduling:

- What is the need for a million dollar machine WAITING for a Disk?
```

```
Scheduling was not invented for -
 ~ Multitasking, User Experience, Responsiveness
   (This come laterrr...)

 - It is invented for 
  "Choose Another Job When One Cannot Use It".
   Beacuse CPU Time is Valuable & Expensive - We shouldn't waste it... 
```

## Evolution of Scheduling:

```
Stage 0 [No Scheduling]:

Problem: CPU need to wait for most of the time, For Humans, IO...

```

```
Stage 1 [Batch Systems]:

Solution Proposed: 
- Let's load many jobs at once, So no more waiting for Humans.

New Problem:
- Long job will blocks the everyone. 
- Ex: Job 1[2 hrs], Job 2[5 min], Job 3[4 mins]

```

```
Stage 2 [First Come First Serve (FCFS)]:

Solution Proposed:
- Who arrives first will run first.

Problem: 
- Truck Behind Cycle Problem.
- Still Short Jobs need to wait.

```

```
Stage 3 [Shortest Job First (SJF)]:

Solution Proposed:
- Shorted Jobs will execute First.

Problem:
- How do we know future job Length?

(Impossible For Many Cases).

```

```
Stage 4 [Multiprogamming -> Round Robin]:

Solution Proposed:

- If a Job waiting for Disk (or) IO, 
  Instead of 'CPU Waiting' Do 'Run Next Job'. 
  (Multiprogramming).

- If we have multiple process to execute. Give fixed time like 10s for every process and force Prempt it. 
  (Round Robin).

Problem:

- Some Jobs are Important. (Priority)

```

```
Stage 5 [Time Sharing]:

- It is an organizational Problem Solving Method.
- Where Multiple Users, use same CPU but from different computers.
- So if one user using CPU another users should wait, to remove that waitng every user will get CPU time for some time.

```

```
Stage 6 [Priority Scheduling]:

Solution Proposed:
- Now High Priority will Run First.

New Problem:
- Low Priority job may never run. (Starvation). 

```

```
Stage 7 [Multilevl Feedback Queues]:

Solution Proposed:
- Now Processes are grouped as Fast, Medium, Slow Queues.
- CPU moves between Queues.

```

```
Stage 8 [Modern Scheduling]:

Old:
Which Process gets CPU?

Now:
Which CPU Core?
How Long?
Which Thread?
Which Cache?
Which Priority?
Which Power State? [To reduce heat & save power, CPU should Reduce Speed or Temporarily Sleep].

Modern scheduler must decide:
- Which thread runs on which core?

while also considering:
- Responsiveness
- Battery
- Heat
- Cache Efficiency
- Fairness

```


## Part - 2 [Data Flow, Components, Internal Working]

### Complete Flow of Data:
```
Process Created
[OS creates PCB]
↓
Ready Queue
[Waiting for CPU]
↓
Scheduler
[Chooses next process]
↓
CPU
[Runs process]
↓
Timer Interrupt
[Time slice finished]
↓
Scheduler
[Gets control again]
↓
Save CPU State Into PCB
[Registers, PC, etc.]
↓
Choose Another Process
↓
Load Its PCB Data
↓
CPU Runs New Process

````

**Questions to know for internal working of Scheduling.**
```
1. What information does the scheduler use?
2. Where is it stored?
3. How is context switching performed?
4. How does the scheduler regain control?
```

```
First Answer:

PCB
↓
PID
Process State
Priority
CPU Usage
Waiting Time
Program Counter
Register Values

```

```
Second Answer:

PCB (Process Control Block) -> Which lives in Kernam Memory (RAM).

```

```
Third Answer:

1. Timer Interrupt Occurs.
2. OS Saves current Process state (CPU State) to PCB.
3. Scheduler will chooses next Process.
4. OS Fetches that Process State from PCB to Registers.

```

```

Chrome Running
↓
10ms Completed
↓
Timer Interrupt
↓
CPU Stops Chrome
↓
Jump To Kernel
↓
Scheduler Runs


Scheduler didn't politely ask Chrome.
The hardware forced Chrome to stop.
```
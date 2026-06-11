### 1. Why was this concept invented?
## RAM
to provide a place for the cpu to temporarily store and immediatly manipulate the data it is working right now data can not be procssed directly in ram so it must first brought into registers for alu operations .
if we do this then they are accessed instantly they are physically built into the processer they eliminate the transfer delay
## CACHE
becz ram is too slow to keep up with cpu and registers are too small to hold data to run programs .to prevent cpu constantly request data from ram cache acts high speed buffer 
cache uses predective algorithms like principle of locality to pre load data or instructions it suspects the cpu will need next .for next time cpu requests.it checks in cache first if present it is cache hit cpu recives data in nano seconds

### 2. What problem existed before it?
## cpu spents most of its time in sitting completly idle ,waiting for data to arrive
## data and instructions are need to share single data bus from memory to processor 

### 3. What would happen if this concept did not exist?
## extreeme performance drop processor would slow down by 99% it will slow down 
## software growth would freeze ,incredibly sloww downs to complete tasks like web browsing ,vedio editing etc..
## massive power consumption waste all the time the cpu will wait for data to be arrived and poling so the massive power consumption will be wasted.

### 4. Explain the internal working step-by-step.
### REGISTER
## registers are made up of flip flops made by circuits of 4 - 6 transistors a flip flop holds 1 bit of data 
## it has direct addressing registers do not have memory addresses instead they have hard wired names like rax,rbx like this name were used ex: instruction says add rax,rbx cpu activates wires leading to those specific register circuites
## 1. fetch pull two numbers from register 2.execute alu operation 3.result writes back to register  
### CACHE

5. Explain all important components and why each component exists.
6. Show how this concept interacts with other computer science concepts.
7. Explain common misconceptions beginners have.
8. Give 5 challenge questions for group discussion.
9. Give a complete flow diagram in text form.
10. Explain how this concept appears in real software systems.
11. Explain what an experienced engineer thinks about this concept that beginners usually miss.
12. Summarize the concept in 5-10 Lines.
# **Why Does A Computer Need A CPU?**

## **What problem would exist if a computer had no CPU?**
### As of now, I know CPU executes instructions & performs some calculations. 
### So, if it doesn't exists then OS cannot be executed, nothing displays on the screen, files & apps cannot be opened, even no calculations gets performed.

### **What is an instruction?**
### They are the commands that CPU can understand & execute. Ex: ADD 3, 5; MOV R1, 3; LOAD X, etc.

---

## **How these instructions are executed?**
### CPU continously performs a cycle called FETCH, DECODE, EXECUTE.
1. **FETCH:** Find out the next instruction from the RAM.
2. **DECODE:** CPU understands the instruction.
3. **EXECUTE:** CPU performs or executes the instruction.

### I observed the instructions executing by the CPU of the below program in a practical way.
    int a = 5, b = 3;
    int c = a + b;
    printf("%d", c);

- Run the program using this command ``gcc -S filename.c``.

### These are assembly level language instructions of the above program.
![assembly-instructions](screenshots/one.png)

---

## **How can you feel the Speed of the CPU?**

### And we can observe the speed of CPU, my Laptop's CPU speed is 2.5GHz. 

### 1Hz = 1 event per second, 2.5GHz = 2,500,000,000 events per sec.

### It means the CPU can perform nearly 2.5 Billion cycles in 1 Second. We don't even capable of counting them.

### We can feel that speed by counting operation programs.
    long long x = 0;
    while(1) {
        x++;
    }

### In 5 Sec CPU incremented the value in x from 0 to 59098. So, we can feel how speed it is.

---

## **What is the one thing that changed the computers being like a calculator in olden days to speedy machines?**

### Transistors made the computer so fast than before where they allowed to store an electric charge like 0 or 1. 

### Before Transistors, Vaccum Tubes were used. They are huge, expensive, consume lots of electricity and generates lots of heat.

## **How Transistors increased the speed of the computer?**

### As they are small in size they can be used at high scale and more calculations can be performed.

## **Flow of execution of program with transistors**

```
int a = 5;

int b = 3;

int c = a + b;
```
### The above code is written in C, a high level language code.

### When it is compiled it becomes:
1. MOV R1, 5
2. MOV R2, 3
3. ADD R3, R1, R2

### The assembly level instructions are converted into Binary instructions by the Assembler using Instruction Set Architecture.

### In ISA the engineers will predefine the Binary Instruction for every instructions like a dictionary.
- Ex: 0001 = MOV, 0010 = LOAD, 0011 = ADD, 0100 = SUB

### So, the above instructions are converted into binary:
1. MOV R1, 5 -> 0001000100000101
2. MOV R2, 3 -> 0001001000000011
3. ADD R3, R1, R2 -> 0011001100010010

### These all instructions are stored in RAM.

### Next CPU fetches each instruction from the RAM. And it fetches the data of those instructions from the Registers.

### The CPU decodes the instructions using transistors like if the first 4 bits are 0001 then they will consider it as a MOV operation. It is done through connecting the physical wirings to different parts of CPU.

### CPU stores 5 in R1 & 3 in R2.

### Now, the ALU takes the R1 & R2 registers and performs addition operation using half & full adders. And it stores the result into R3. 
---

## What are the Parts inside the CPU?

### 1. Registers
- Modern CPUs are very fast like performing 3 Billion operations per second but the RAM gives the data for only ~1 Billion operations in 1 second.
- There is a much speed gap between CPU & RAM. And CPU waits most of its time.
- Engineers introduced tiny storage units called **Registers** inside the CPU.
- They store ~1KB of data because very small in size & expensive for to build large ones.
- They are used to store operands for the Arithmetic or Logical operations. So, ALU directly interacts with them.

Feel the Registers:

```
int c = 5 + 3;

call	___main
movl	$5, 28(%esp)
movl	$3, 24(%esp)
movl	28(%esp), %edx
movl	24(%esp), %eax
addl	%edx, %eax
```

### 2. Cache
- For to store large size of frequent data. The registers aren't enough because of their size.
- So, CPU needs another layer called Cache. This layer has 3 levels: L1, L2, L3 Cache.
- It stores the frequent instructions or data to give it to the CPU.

Feel Cache:
```
Turn On the System, Open VS Code. You observe some what slow.
Next again reopen the VS Code, it will open faster than before.
- As the data of VS Code is already stored in Cache. So the CPU fetches the instructions or data from the Cache which faster than RAM and execute them.
```

## Biggest Lesson: Almost all the applications are slow because of RAM & Storage not CPU. CPU is faster than all of them. So, we have to optimize our apps for Caching, Memory & Storage. 

### 3. ALU
- It performs Arithmetic & Logical opeartions on the operands present in the CPU Registers of an instruction.
- Without it we cannot any Arithmetic & Logical opeartions.
- This ALU is built using combinational circuits like Half Adder, Full Adder & comparators, etc.

### 4. Control Unit
- It triggers the units in the CPU for to execute an instruction using control signals.
- For Example: add eax, ebx
- Control Unit generates signal to:
Read EAX,
Read EBX,
Enable ADD path,
Write result.

---

## Why does CPU Cores exists?
- If a CPU has no cores then it has to execute only one thread at a time.
- For many years, the engineers had increased the performance by increasing the clock speed.
1GHz -> 2GHz -> 3GHz -> 4Hz
- But as we know even the CPU is faster, fetching the instructions from RAM & Cache is slow. So, the CPU has to wait.
- So, instead of 1 very fast CPU. Divide the CPU into parts called cores.
- A Core is a mini CPU. It has its own Registers, ALU, Cache, Decoder, etc.
- 
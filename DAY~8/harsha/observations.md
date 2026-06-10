# Caches & Registers

## **Why Registers & Cache are invented with problems exist before?**
### **Registers**: Early computers stored the operands of an instruction in accumulators, RAM or any other hardware units but each operation requires data movement between these hardware units. Engineers realized CPU uses the same values during instrction execution. So, they invented Registers where frequently used data is stored directly inside the CPU.

### **Cache**: During 1960s-1980s the CPUs speed increased rapidly, memory speed improved much more slowly. The CPU spent most amounts of time waiting. This became known as von Neumann bottleneck. Researchers found that programs do not access data randomly instead they reuse same instructions, same variables & near by addresses. This became:
- Temporal Locality: If data was used recently, it is likely to be used again soon.
- Spatial Locality: If address X was used, nearby addresses will likely be used soon.

- These observations made Cache memory to be introduced. It is placed between RAM & CPU.


## **What happens if Registers & Cache doesn't exists?**
### **No Registers**:
- CPU has ALU, control unit, RAM but no registers. For every instruction the CPU has to fetch the every operand from the RAM.
- It increases the memory traffic between RAM and ALU. 
- The ALU may finish a calculation in 1 cycle but accessing the operands from RAM may takes 80-100 cycles. 
- So, ALU spends most of the time idle.

### **No Cache**:
- If cache doesn't exists then as we knew for every access CPU communicates with RAM directly.
- Some processes needs nearby memory locations which are predictable and can be stored in cache and can access them faster but if it doesn't exists then for every near by addresses CPU should access from RAM. 
- It also increases latency between CPU & RAM.
- The CPU could execute hundreds of instructions while waiting for one memory read. 


## **Internal working of Registers**
```Assembly
MOV R1, 5
MOV R2, 3
ADD R3, R1, R2
```
1. Suppose we execute above instructions, the instruction address is fetched from PC in CPU. The instruction address is sent to RAM.
2. Instruction enters into the IR.
3. Decoder sees the instruction MOV R1, 5 and MOV R2, 3 it decodes as Destination Register = R1, Data = 5 & Register = R2, Data = 3.
4. Control signals are generated and sent to the Register File. 
5. The Register file contains all the registers. It receives the control signal to write data. Internally the signal is in binary, the decoder decodes it.
6. The Register file writes the data 5 in the Register R1 & data 3 in the Register R2.
7. The each bit in the register is stored in flip-flops and the data remains stable until overwritten.
8. Now, CPU fetches the ADD R3, R1, R2 and decoder identifies Source1 = R1, Source2 = R2, Destination = R3.
9. Register file contains Read PortA, Read PortB & Write Port. CPU simultaneously reads R1 -> PORT-A, R2->PORT-B.
10. ALU receives those operands and ALU executes the addition operation.
11. Again the result is written back to Register file through write port like Destination = R3, Value = 8. R3 contains 8.


## **Internal Working of Cache**
1. If CPU wants to execute this instruction, MOV R1 [0x2000].
2. CPU requests the cache controller -> [0x2000].
3. Address is split by cache controller as TAG, INDEX & OFFSET.
4. Cache looks the set by using the INDEX.
5. Cache set contains stored tag, valid bit & data.
6. If stored tag == requested tag then it is Cache Hit. The OFFSET selects the required bytes of data returned.
7. If it is Cache Miss then Cache controller sends request to L2 Cache. 
8. If L2 misses then L3 Cache. If L3 misses then DRAM.
9. Memory controller fetches the entire Cache set usually it is 64 bytes.
10. The cache is moved from DRAM to L3 -> L2 -> L1 -> Registers.


## **Important components in Registers**
1. The CPU needs to remember the values between the execution of instructions. If instruction executes the value disappears. To store them ``Flip-Flops`` are used where they store 1 bit. If a Register needs to store 32 bits then it needs 32 flip-flops to build it.
2. There are many registers inside the CPU. Every Register has to connect by seperate wires with ALU but it makes the architecture clumsy. So, to solve this ``Register File`` is introduces where all the registers are connected at one place and only it is connected to the ALU.
3. The CPU wants to place the data into a register. How it can send the data to a specific register. To solve this ``Write Ports`` are introduced where it contains Write Data, Write Address, Write Enable.
4. How does ALU get operands from Registers? without a read mechanism the data is trapped inside the Registers. The solution to this is ``Read Ports``. These Read Ports fetches the data from the specific register and gives to the ALU.
5. How does Register File knows that an instruction needs specific registers?
``Decoder`` solve this problem by decoding the Register IDs from binary instructions.
6. There are many registers. When the data is reading from READ PORT without selection of specific register. All register try to send data simulatenously. To solve this ``Multiplexer`` is used and it selects only one register from many.
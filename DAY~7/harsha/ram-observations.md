# **RAM - Random Access Memory**

## **Why RAM was invented?**
### 1. RAM was not invented for increase the storage capacity. It was invented to reduce the CPU latency of accessing the data from secondary storage devices.
### 2. CPU needs a memory device that can allow read/write the data in any memory location at a constant time. 
### 3. Finally, RAM was invented to allow the CPU to access any random location in the memory at a same constant time.


## **What Problem exists before the RAM?**
### 1. Before RAM was invented punch cards, magnetic drums & magnetic tapes were used.
### 2. They allow sequential access of memory like if we need to access the 900 memory location then we have move from 0-899 locations.
### 3. As CPU execution speed was increasing, the memory devices accessing or supplying time was low compared to CPU. So, ultimately CPU is idle while fetching the instructions or data.
### 4. And CPU needs a memory system which allows direct access at any memory location with constant time and read/write speed should be also very fast.

## This is why RAM is called ```RANDOM ACCESS MEMORY```. Any address can be accessed at same amount of time.  

## The First RAM is DRAM which is invented by Robert H. Dennard at IBM in 1968. The Key innovation is that ```One transistor + One capacitor for each bit```.


## **What would happen if RAM did not exist?**
### 1. The CPU continously need variables, code, heap, stack, etc to execute the instructions of a program. They should be provided with low latency.
### 2. If RAM doesn't exists then all the program essential has to be provided by the SSD. The RAM speed is 50-100ns and SSD speed is 100000ns. For fetching every instruction the CPU has to wait 1000-2000ns.
### 3. If only hard disks exists then its latency is 500000-1000000ns and it makes the CPU even more slower and even small apps are unusable.
### 4. Without RAM, variables doesn't have best place to store, function calls cannot be maintain in the stack, dynamic memory allocation in heap is impossible, multiple cannot be executed efficently.


## **Internal working of RAM**
### In the modern CPUs DRAM chips are used for RAM. DRAM contains billions of memory cells. Each cell stores only 1 bit. Each cell contains 1 transistor + 1 capacitor. The capacitor is the actual storage element.
### The cells in the DRAM are organized into millions of rows and thousands of columns.
### 1. For suppose CPU wants to execute the below line:
```C
int x = arr[100];
```
- CPU needs the data stored at some address. For example, 0x7A3B91F0 is that address.

### 2. The address is sent to the memory controller which is inside the CPU. It decodes the memory address and determines bank, row, column. For suppose it is 1500 Row, 20 Column. The controller now exactly knows where data lives.

### 3. DRAM cannot read a specific cell, instead it activates the entire row. The memory controller sends ``ACTIVATE ROW 1500``.

### 4. After activating the entire row the whole row is copied into a structure called Row Buffer. This is the one reason sequential access fast.

### 5. The charge inside RAM is extremely small. They cannot be read directly. Special circuits called Sense amplifiers detect a cell is charged or not. If the charge is weak then it is refreshed by the sense amplifier.

### 6. Now, the row is open. The memory controller requests ``COLUMN 20``. Sense amplifiers read the required bits from the row buffer.

### 7. The selected data is sent through RAM -> Memory Bus -> Memory Controller -> CPU.

### 8. Now, after completion of instruction. The CPU wants to write the data the data to RAM. Again the CPU sends address, data, write command to the memory controller.

### 9. RAM activates the row and the data is stored as 1 -> charged, 0 -> discharged.

### 10. The capacitors in RAM slowly lose their charge. So, the DRAM constantly refreshes itself automatically. This is why it is called DRAM because stored charge must be refreshed continously.

### When RAM has no power supply it eventually loses all the charges in the capacitors in the each cell refreshing needs power. So, the entire data is erased and that's why it is called Volatile memory.

### If we observe the above steps RAM doesn't understand variables, objects, arrays, etc. It only understands addresses, read, write, bits.


## **Important components and why each component exists.**
### Problem 1: We need to store a bit
- A bit is either 0 or 1 in terms of computers but physically they have to represent in voltage or charge.
- Engineers need a special device that can store electrical charge.
- The device is called ``Capacitor`` it can store a bit as electrical charge.

### Problem 2: How do we read one capacitor without disturbing others?
- Suppose we connect millions of capacitors together, how can access only one among them?
- We use a ``Transistor`` where it acts as switch.
- When transistor is off then capacitor doesn't have any charge. When it is on then capacitor has charge.

### Problem 3: How do we connect all memory cels?
- Imagine billions of memory cells we cannot connect every cell with seperate wire, it's too many wires.
- Instead cells are arranged in rows & cols and each row gets a special wire called ``Word Line``.
- When Word line is high it activates all the transistors in a row.

### Problem 4: How do we carry the data?
- The charge in the capacitor should be shared to someone.
- To share it each column connects as wire called ``Bit Line``.
- When a specific Word Line is HIGH then all the transistors in that row are active. Now a specific capacitor will connect to a Bit Line.
- And the charge can be carried.

### Problem 5: Capacitor charges are tiny
- The charge difference between on & off is very low in DRAM capacitors.
- To detect those tiny difference ``Sense Amplifier`` is used.
- It converts the weak electric charges into strong digital signals.

### Problem 6: Reading destroys charge
- When a capacitor connected with a bit line it loses some charge. Read operation damages stored bit.
- We need to restore the charge when it is lost. To do that ``Refresh Circuit`` is introduced.
- For every few milli-seconds the refresh circuit reads, restore and write backs the charges for every bit.
- Without refreshing all the memory disappers that's why it is called DRAM.

### Problem 7: CPU gives only addresses
- CPU asks the data at a particular address but RAM doesn't understand hexadecimal addresses it needs to translated.
- For that ``Memory Controller`` is introduced where it converts Address into Bank, Row & Column.

### Problem 8: Every access needs an entire row opened again
- When we want to access multiple columns in a row then we have to reactivate the row for every access, which is inefficent.
- Instead we use ``Row Buffer`` where we store the entire activated row temporarily.
- And we can access multiple columns without reactivating the entire row.


## **Common misconceptions beginners have**
### 1. RAM is just temporary storage. Actually it's not a most important property of RAM. It is Random Access, Low Latency, Directly accessable.
### 2. CPU directly talks to RAM. That's not true because modern CPUs has many layers exists between CPU & DRAM like L1 Cache, L2 Cache, L3 cache & RAM.
### 3. The Address == Physical Location in RAM. It is not always true because virtual addresses are also used while executing the programs.


## **Complete Flow Diagram of RAM**
```
SSD
 ↓
OS Loads Program
 ↓
RAM
 ↓
CPU Fetches Instruction
 ↓
L1 Cache
 ↓
L2 Cache
 ↓
L3 Cache
 ↓
Memory Controller
 ↓
Channel
 ↓
Rank
 ↓
Bank
 ↓
Row Decoder
 ↓
Word Line
 ↓
Transistor Opens
 ↓
Capacitor Charge
 ↓
Bit Line
 ↓
Sense Amplifier
 ↓
Row Buffer
 ↓
Column Decoder
 ↓
Memory Bus
 ↓
Memory Controller
 ↓
L3 Cache
 ↓
L2 Cache
 ↓
L1 Cache
 ↓
CPU Register
 ↓
ALU
 ↓
Instruction Completes
```


## **How RAM appears in real software systems?**
### 1. SBTET Results Page: Every request we sent to see the result. The server needs to fetch the result data from disk to RAM next to CPU and that result is sent as response. When we sent multiple requests the data movement between disk to RAM increases and eventually  we receive responses at very low rates.
### 2. Redis: It enables to store the data directly into the RAM instead of disk. This is why Redis operation takes micro seconds. And it is not a database technology, it is a memory optimizer.
### 3. Chrome: When we open 50 tabs in chrome all the HTML, CSS, JS Objects, Images, DOM Tree all live inside the RAM. So, large websites consume lots of memory.


## **What an experienced engineer thinks about RAM?**
### 1. When you are building an algorithm if it prefers caching then which data structure would you choose Linked List or Array. Array needs to be chosen because it allows contigous memory access.
### 2. Beginners think CPU executes programs but experienced engineer sees CPU waits for memory. Many performance problems are not CPU problems they are memory problems.
### 3. If we need more memory then beginners think allocate more but experienced engineers think do we actually need this data.
### 4. We think:
```JS
user.name
```
It is just a JS object but experienced engineers see it as memory access like RAM -> Cache -> CPU Register.

## **SUMMARY in 5 Lines**
- RAM enables the CPU to execute the instructions with low latency by providing the data or instructions of an active process to its units.
- It allows direct access to any random memory location in less time without following the sequential access technique.
- It contains memory cells where each cell contains 1 transistor + 1 capacitor to store bits as electrical charges.
- The capacitors stores electrical charges but eventually they will lost their charge capacity after few seconds and they has to be restored. So, that it is called Dynamic RAM.
- And if it doesn't get any power supply then those charges doesn't get restored and all the data stored will be lost. So, that's why it is called Volatile memory.


## **As we are the future software engineers we have to optimize our applications for to reduce data movement between memory units and CPU.**
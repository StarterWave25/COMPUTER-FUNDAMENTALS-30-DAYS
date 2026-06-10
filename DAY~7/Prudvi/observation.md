# Day ~ 7 [Observations - PATNAM PRUDVINATH]

## Part - 1 [Why Was RAM Invented?]

### My Assumption:

---

Initially, I thought RAM was invented because SSDs and Hard Disks are slow.

So I assumed:

> CPU needs RAM because RAM is faster than SSD.

### My Research:

---

After researching and thinking deeper, I found that speed is only part of the answer.

The real problem is that running programs constantly create temporary data that changes every moment.

Examples:

* Variables
* Open Tabs
* Video Buffers
* Browser State
* Process Data
* Thread Data
* Function Results

This data usually does not exist before the program starts running.

The program creates it while executing.

---

### The Problem Before RAM

Imagine a computer has:

CPU <br>
↓ <br>
SSD <br>

But no RAM.

Now suppose a program contains:

```c
int total = 0;

for(int i = 0; i < 1000000; i++)
{
    total++;
}
```

The value of `total` changes one million times.

Without RAM:

CPU <br>
↓ <br>
Read SSD <br>
↓ <br>
Modify Data <br>
↓ <br>
Write Back To SSD <br>

This would happen again and again.

The CPU would spend most of its time waiting for storage operations instead of executing instructions.

---

### What RAM Solves

---

RAM provides a place for:

* Temporary Data
* Frequently Changing Data
* Running Programs
* Fast Reading
* Fast Writing

Flow:

Program Stored In SSD <br>
↓ <br>
Program Loaded Into RAM <br>
↓ <br>
CPU Reads & Modifies Data <br>
↓ <br>
Program Executes <br>

---

### Interesting Observation

At first, I thought:

> RAM is just a faster SSD.

After researching, I realized that this is not true.

SSD and RAM have different jobs.

SSD is designed to store data permanently.

RAM is designed to store active and temporary data while programs are running.

---

### What Would Happen If RAM Did Not Exist?

---

Without RAM:

* Programs would execute much slower.
* The CPU would constantly wait for storage.
* Temporary data would have no proper workspace.
* Running multiple applications would become very inefficient.
* Modern operating systems would struggle to function smoothly.

---

## Final Understanding

RAM was not invented only because storage devices were slow.

RAM was invented because running programs constantly create temporary data that must be read, modified, and written very quickly.

SSD stores programs permanently.

RAM acts as a workspace where those programs can run efficiently.

The biggest thing I learned is:

> RAM is not a faster SSD. RAM is the CPU's working area where active and constantly changing data lives while a program is running.

## Part - 2 [What ]

>Before RAM, computers lacked a dedicated workspace for storing and managing temporary, constantly changing data created by running programs.

>SSD is permanent storage and not designed for continuously changing data.<br>
So the missing piece was:<br>
>>A large, temporary, read-write workspace between storage and the CPU.

## Part - 3 [What Would Happen If RAM Did Not Exist?]

### What Happens During Boot?

---

Normally:

SSD <br>
↓ <br>
Operating System Loaded Into RAM <br>
↓ <br>
CPU Executes OS Instructions <br>
↓ <br>
Computer Starts <br>

Without RAM:

SSD <br>
↓ <br>
No Working Memory Available <br>
↓ <br>
Operating System Cannot Function Properly <br>

Modern operating systems are built around the assumption that RAM exists.

Without RAM, they would require a completely different design.

---

### What Happens To Running Programs?

---

Consider Chrome.

While running, Chrome continuously stores:

* Open Tabs
* Page State
* JavaScript Variables
* Download Information
* Video Buffers

Normally:

Chrome Process <br>
↓ <br>
RAM <br>
↓ <br>
CPU <br>

Without RAM:

Chrome Process <br>
↓ <br>
SSD <br>
↓ <br>
CPU <br>

Every small change would require communication with storage.

The CPU would spend much of its time waiting instead of executing instructions.

---

### What Happens To Unsaved Work?

---

Suppose I am writing a document in Word.

Normally:

Keyboard Input <br>
↓ <br>
RAM <br>
↓ <br>
Word Document <br>

Only when I save:

RAM <br>
↓ <br>
SSD <br>

Without RAM, software would have no efficient place to keep temporary changes.

Applications would need to constantly depend on storage.

---

### What Happens To Multitasking?

---

Modern operating systems manage:

* Processes
* Threads
* Memory Information
* Running Applications

All of this information must remain available while the system is running.

Without RAM:

Operating System <br>
↓ <br>
Storage Dependency For Active Data <br>
↓ <br>
Much Less Efficient Multitasking <br>

Running multiple applications would become significantly more difficult.


---

## Part - 4 [Building Intuition About RAM Using A Real-World Analogy]

### My Assumption:

---

Initially, I tried comparing:

SSD → Textbook <br>
RAM → Teacher Notes <br>
Registers → My Notes <br>

This seemed reasonable because each level contained less information and was easier to access.

However, after thinking deeper, I realized that RAM is not simply a summarized version of SSD.

RAM often contains data that never existed inside SSD.

Examples:

* Open Browser Tabs
* Variables
* Process Information
* Thread Information
* Unsaved Work

This made me look for a better analogy.

---

### My Research:

---

The best analogy I found was a restaurant.

A restaurant contains:

* Storage Room
* Order Board
* Chef
* Chef's Hands
* Waiters / Manager

Each of these maps surprisingly well to a computer system.

---

### Mapping The Components

Storage Room → SSD <br>

Contains:

* Rice
* Vegetables
* Spices
* Ingredients

Similarly, SSD stores:

* Programs
* Photos
* Videos
* Documents

The storage room holds resources, but cooking does not happen there.

Likewise, SSD stores data, but execution does not happen there.

---

Order Board → RAM <br>

Contains:

* Current Orders
* Pending Orders
* Active Work

Example:

Table 1 → Biryani <br>
Table 2 → Noodles <br>
Table 3 → Fried Rice <br>

The order board constantly changes.

Orders are added, modified, and removed.

Similarly, RAM stores:

* Running Programs
* Variables
* Process Data
* Thread Data
* Buffers

RAM is where active work exists.

---

Chef → CPU <br>

The chef reads orders and performs work.

Similarly, the CPU reads instructions and executes them.

The CPU does not store large amounts of information.

Its job is to process and execute tasks.

---

Chef's Hands → Registers <br>

While cooking, the chef only holds a few items at a time.

For example:

* Knife
* Vegetables
* Spoon

Similarly, registers hold only the data currently needed by the CPU.

Registers are extremely small but extremely fast.

---

Waiters & Manager → Operating System <br>

The waiters:

* Take orders
* Deliver information
* Update the order board

The manager:

* Decides priorities
* Organizes work
* Coordinates the restaurant

Similarly, the Operating System:

* Loads programs into RAM
* Manages processes
* Manages threads
* Allocates resources
* Schedules CPU time

---

### Complete Flow

Customer <br>
↓ <br>
Waiters / Manager (OS) <br>
↓ <br>
Order Board (RAM) <br>
↓ <br>
Chef's Hands (Registers) <br>
↓ <br>
Chef (CPU) <br>
↓ <br>
Food Prepared <br>

Computer Equivalent:

User <br>
↓ <br>
Operating System <br>
↓ <br>
RAM <br>
↓ <br>
Registers <br>
↓ <br>
CPU <br>
↓ <br>
Program Output <br>

---

## Part - 5 [How Does RAM Actually Work Internally?]

### My Assumption:

---

Initially, I thought RAM was simply a fast storage device that stores running programs.

I knew:

* Programs are loaded into RAM.
* CPU reads data from RAM.
* RAM is faster than SSD.

But I had no idea:

* How RAM physically stores data.
* How RAM reads data.
* How RAM writes data.
* Why RAM loses data when power is removed.

### My Research:

---

After researching, I found that RAM is not one large storage area.

Instead, RAM is made up of billions of tiny memory cells.

Each memory cell stores a single bit:

```text
0
or
1
```

These memory cells are organized into rows and columns, similar to a spreadsheet.

---

### Internal Structure of a RAM Cell

---

A typical DRAM memory cell contains:

* One Capacitor
* One Transistor

Structure:

```text
Bit Line
   |
   |
[Transistor]
   |
   |
[Capacitor]
   |
 Ground
```

The capacitor stores the actual data.

The transistor acts like a switch that controls access to the capacitor.

---

### What Does The Capacitor Do?

---

The capacitor stores a tiny electrical charge.

Very simplified:

```text
Charge Exists
=
1
```

```text
No Charge
=
0
```

So RAM stores data using electrical charge.

---

### What Does The Transistor Do?

---

The transistor acts like a gate.

When OFF:

```text
Bit Line
   |
   X
[Transistor]
   |
[Capacitor]
```

The capacitor cannot be accessed.

When ON:

```text
Bit Line
   |
   |
[Transistor]
   |
[Capacitor]
```

The memory controller can read or write data.

---

### How Memory Cells Are Organized

---

RAM does not store bits randomly.

Memory cells are arranged in rows and columns.

Example:

```text
      C0 C1 C2 C3

R0    0  1  0  1

R1    1  1  0  0

R2    0  0  1  1

R3    1  0  1  0
```

Each cell has an address.

The CPU uses these addresses to access data.

---

### How Reading Data Works

---

Suppose the CPU needs data stored at a particular address.

Step 1

The CPU sends the address to the Memory Controller.

```text
CPU
 ↓
Memory Controller
```

Step 2

The Memory Controller locates the correct row and column.

```text
Select Row
 ↓
Select Column
```

Step 3

The transistor is opened.

```text
Memory Cell
 ↓
Accessible
```

Step 4

The capacitor's charge is checked.

```text
Charge Exists
↓
1
```

or

```text
No Charge
↓
0
```

Step 5

The value is returned to the CPU.

```text
RAM
 ↓
CPU
```

---

### Interesting Observation

---

One thing that surprised me was that reading DRAM slightly disturbs the stored charge.

Because of this:

```text
Read Data
 ↓
Charge Weakens
 ↓
Write Back Again
```

The memory controller automatically restores the value after reading it.

The CPU never notices this process.

---

### How Writing Data Works

---

Suppose the CPU wants to store:

```text
1
```

Step 1

The CPU sends the address and value.

```text
CPU
 ↓
Memory Controller
```

Step 2

The correct row and column are selected.

Step 3

The transistor is opened.

Step 4

Electrical charge is placed into the capacitor.

```text
Capacitor Charged
=
1
```

If the CPU wants to store:

```text
0
```

The capacitor is discharged.

```text
Capacitor Empty
=
0
```

---

### Why RAM Loses Data

---

Capacitors cannot hold electrical charge forever.

Over time:

```text
Charge
 ↓
Slow Leakage
 ↓
Data Lost
```

This is why RAM requires constant electrical power.

When power is removed:

```text
No Power
 ↓
No Charge
 ↓
No Data
```

The stored information disappears.

This is why RAM is called:

> Volatile Memory

---

### What Is Refreshing?

---

Because charge naturally leaks away, RAM must continuously refresh its data.

Flow:

```text
Read Value
 ↓
Rewrite Value
 ↓
Maintain Charge
```

This happens automatically millions of times every second.

Without refreshing:

```text
Stored Data
 ↓
Charge Leakage
 ↓
Data Corruption
```

---

### How Programs Are Loaded Into RAM

---

Suppose I open Chrome.

Step 1

Chrome exists as a file inside SSD.

```text
Chrome.exe
 ↓
SSD
```

Step 2

The Operating System requests the program.

```text
User
 ↓
Operating System
```

Step 3

The program data is copied into RAM.

```text
SSD
 ↓
RAM
```

Step 4

The CPU begins executing instructions from RAM.

```text
RAM
 ↓
CPU
```

---

### How Data Is Removed From RAM

---

When a program closes, RAM is usually not immediately erased.

Instead:

```text
Program Closed
 ↓
Operating System Marks Memory As Free
```

Those memory locations become available for future programs.

Later:

```text
New Program
 ↓
Overwrite Old Data
```

---

### Complete Internal Flow

```text
Program Stored In SSD
 ↓
Operating System Loads Program
 ↓
RAM Receives Data
 ↓
Memory Controller Locates Addresses
 ↓
CPU Requests Data
 ↓
Memory Controller Selects Row & Column
 ↓
Transistor Opens
 ↓
Capacitor Read / Written
 ↓
Data Sent To CPU
 ↓
CPU Executes Instructions
```

---

## Final Understanding

Initially, I thought RAM was simply a fast storage device.

After researching, I realized that RAM is actually a massive collection of tiny memory cells built using capacitors and transistors.

Each cell stores a single bit using electrical charge.

The Memory Controller manages reading, writing, refreshing, and locating data.

The CPU constantly communicates with RAM while executing programs.

The biggest thing I learned is:

> RAM stores information as electrical charge inside billions of tiny memory cells, and the Memory Controller continuously manages those cells so the CPU can access data extremely quickly.

## Part - 6 [Important Components Inside RAM And Why They Exist]

### My Assumption:

---

Initially, I thought RAM was just a collection of memory cells that store data.

So I assumed:

> As long as RAM can store 0s and 1s, it should work.

After researching, I realized that storing data is only one part of the problem.

A RAM system must also:

* Store Data
* Access Data
* Locate Data
* Transfer Data
* Preserve Data

Different components exist to solve each of these problems.

---

### My Research:

---

While studying RAM, I noticed that every component exists because engineers needed to solve a specific problem.

Instead of memorizing component names, I found it easier to think:

```text
Problem
↓
Component Invented
↓
Problem Solved
```

---

### 1. Capacitor

#### Why Does It Exist?

The computer needs a place to physically store a bit.

A capacitor solves this problem.

Structure:

```text
[Capacitor]
```

A capacitor stores a tiny electrical charge.

Very simplified:

```text
Charge Exists
=
1
```

```text
No Charge
=
0
```

Without capacitors:

```text
No Place To Store Data
```

So the capacitor is the component where the actual bit lives.

---

### 2. Transistor

#### Why Does It Exist?

Suppose the capacitor stores data.

Now another problem appears:

> How can the CPU access that capacitor?

Engineers solved this using a transistor.

Structure:

```text
Bit Line
   |
[Transistor]
   |
[Capacitor]
```

The transistor acts like a switch.

When OFF:

```text
No Access
```

When ON:

```text
Access Allowed
```

Without transistors:

```text
Data Exists
↓
But Cannot Be Reliably Accessed
```

---

### 3. Memory Cells

#### Why Do They Exist?

One capacitor and one transistor together form a memory cell.

Structure:

```text
[Transistor]
     |
[Capacitor]
```

Each memory cell stores:

```text
1 Bit
```

Examples:

```text
0
```

or

```text
1
```

Without memory cells:

```text
No Organized Storage
```

---

### 4. Rows And Columns

#### Why Do They Exist?

Modern RAM contains billions of memory cells.

Engineers needed a way to organize them.

So memory cells are arranged like a spreadsheet.

Example:

```text
      C0 C1 C2 C3

R0    0  1  0  1

R1    1  1  0  0

R2    0  0  1  1

R3    1  0  1  0
```

Without organization:

```text
Billions Of Cells
↓
Impossible To Locate Data Efficiently
```

---

### 5. Memory Addresses

#### Why Do They Exist?

Even with rows and columns, the CPU still needs a way to identify specific locations.

Each memory location receives an address.

Example:

```text
Address 1000
Address 1001
Address 1002
```

The CPU requests data using addresses.

Without addresses:

```text
Data Exists
↓
CPU Cannot Find It
```

---

### 6. Memory Controller

#### Why Does It Exist?

Now another problem appears.

Who manages:

* Reading
* Writing
* Address Lookup
* Refreshing

This is the job of the Memory Controller.

Flow:

```text
CPU
 ↓
Memory Controller
 ↓
RAM
```

The Memory Controller acts as the manager of RAM operations.

Without it:

```text
CPU Would Need To Control Billions Of Cells Directly
```

which would be impractical.

---

### 7. Address Bus

#### Why Does It Exist?

The CPU must tell RAM:

> Which memory location do I need?

The Address Bus carries this information.

Example:

```text
CPU
 ↓
Address Bus
 ↓
RAM Address
```

Without an Address Bus:

```text
CPU Cannot Specify A Memory Location
```

---

### 8. Data Bus

#### Why Does It Exist?

After locating the correct memory cell, the actual data must travel.

The Data Bus carries that data.

Example:

```text
RAM
 ↓
Data Bus
 ↓
CPU
```

Without a Data Bus:

```text
Data Cannot Move Between RAM And CPU
```

---

### 9. Refresh Circuitry

#### Why Does It Exist?

Capacitors slowly lose charge over time.

Flow:

```text
Charge Stored
 ↓
Charge Leakage
 ↓
Data Lost
```

To prevent this, RAM continuously refreshes stored values.

Flow:

```text
Read Value
 ↓
Rewrite Value
 ↓
Maintain Charge
```

Without refresh circuitry:

```text
Stored Data
 ↓
Gradually Disappears
```

---

### Interesting Observation

At first, I tried finding the "most important" RAM component.

I thought the capacitor was the most important because it stores the actual data.

After researching, I realized that RAM works as a complete system.

For example:

```text
Capacitor Without Transistor
=
Cannot Access Data
```

```text
Capacitor + Transistor Without Addresses
=
Cannot Find Data
```

```text
Everything Without Refresh
=
Data Lost
```

Every component solves a different problem.

Removing any one of them breaks the system.

---

### Complete Picture

```text
Capacitor
↓
Stores Data

Transistor
↓
Controls Access

Memory Cell
↓
Stores One Bit

Rows & Columns
↓
Organize Cells

Addresses
↓
Locate Data

Memory Controller
↓
Manages RAM Operations

Address Bus
↓
Carries Addresses

Data Bus
↓
Carries Data

Refresh Circuitry
↓
Prevents Data Loss
```

---

## Final Understanding

Initially, I thought RAM was simply a storage device.

After researching, I learned that RAM is actually a collection of components working together to solve different problems.

Some components store data.

Some locate data.

Some transfer data.

Some preserve data.

The biggest thing I learned is:

> RAM is not a single component. It is a complete system where every component exists to solve a specific problem required for storing and accessing data efficiently.

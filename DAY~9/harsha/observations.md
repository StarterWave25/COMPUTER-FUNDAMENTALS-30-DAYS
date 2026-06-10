# **HDD & SSD**

## **Why HDD invented & What problems exist before?**
### **Problems:**
1. Before HDD, there are serveral storage technologies like Punch cards, Paper tape, Magnetic tape. They had several problems like sequential access, damage easily, slow retrevial, low storage capacity, etc.
2. In early 1950s, the businesses need databases, banking systems, airline reservations, etc. These required random access which magnetic tapes could not provide efficiently.
### **Solution:**
1. So, HDD was invented to solve the fundamental problem that is allowing the computers to access any record without scanning all previuos records.
2. HDD allows to access a record by direct sector addressing which is in milliseconds but before it takes minutes.


## **Why SSD invented & What problems exist before?**
### **Problems:**
1. In 1980-2000s, the CPU speed increased dramatically like CPU is performing the operations in nanoseconds but HDD accesses the records in milliseconds.
2. There is a lot of speed gap between the CPU & HDD because to access a record the HDD should move the heads to correct sector & track which it creates the mechanical latency.
### **Solution:**
1. The goal of SSD is to eliminate the mechanical movement entirely. Researchers discovered a new technology that could store data without heads, tracks and platters which is called **Flash Memory**.
2. Now, the SSD removed the mechanical latency and it made the accessing time of a record to ~100 microseconds with high IOPS and also it consumes low power.


## **What would happen if HDD & SSD did not exist?**
1. If we have only CPUs & RAMs then when we power off the computer all apps disappears, os disappears, data disappears. Every boot requires reloading the entire data from another medium.
2. Instead of HDDs & SSDs, magnetic tapes may used for storage but accessing the records would be sequential and takes more time to provide it to Memory.
3. Without SSDs/HDDs the databases becomes extremely slow and most of the computing may be in batch processing like submit the job, wait and get results later.
4. The internet may be doesn't exists because a web server needs to store HTML, Images, Videos, DBs & Logs which would be difficult to store in magnetic tapes.


## **Components in HDD**
1. Where can billions of bits are stored permanently in HDD?
-  Using ``Magnetic Platter`` a rotating disk coated with magnetic material. Each magnetic region stores 0 as magnetic orientation A and 1 as magnetic orientation B.
- Without platters no large capacity storage medium exists and these magnetic orientations remains even after power is removed.

2. How can every location on the platter pass under the read/write head?
- By rotating the platter continously by the ``Spindle Motor``.
- Without the spindle motor most platter locations could never reach the head.

3. How can billions of bits are organized?
- The platter surfaces are divided into circles which are called ``Tracks``.
- Without tracks data locations become impossible to organize and addressing is difficult.
- For Each track it is again divided into ``Sectors``.
- CPU access the specific data blocks using sectors.

4. How can magnetic bits be read and write?
- Using an electro-magnetic sensor called ``Read/Write Head``.
- When it is reading it detects the magnetic orientation.
- When it is writing it generate magnetic fields and changes orientation.
- And the head never touches the platter it flies a few nanometers above it.

5. How can the head reach different tracks?
- There should be a mechanical arm that should move the head from center to edge of platter. 
- It is called ``Acutator Arm``.
- Without actuator only one arm could be accessed.

6. Who coordinates everything?
- An embedded controller which is responsible for head movement, error correction, sector mapping, etc it is called as HDD Controller.
- Without a controller components cannot coordinate.


## **Internal working of HDD**
```
1. CPU requests sector
          ↓
2. HDD Controller receives request
          ↓
3. Actuator moves head
          ↓
4. Spindle rotates platter
          ↓
5. Servo data verifies position
          ↓
6. Head reads magnetic patterns
          ↓
7. Read channel converts signals
          ↓
8. ECC verifies data
          ↓
9. Cache stores data
          ↓
10. Data sent to RAM
```

## **Components in SSD**
1. Where does the SSD stores the bits?
- Using NAND Flash memory cells the SSD stores the bits.
- The bits are stored as electric charges in it.
- For SSDs NAND plays same role as platter in HDDs.

2. How can bits are stored permanently?
- The electrons are trapped inside an insulated structure.
- A flash cell contains information as charge.

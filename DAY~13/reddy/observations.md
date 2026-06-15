# My Approach to Solving the Problem

## Initial Thought Process

1. Create a file (`ledger.txt`) to store all restaurant order records.
2. Test the logic with a single customer first.
3. Verify that everything works correctly.
4. Once the basic functionality is stable, introduce multithreading.

## Step-by-Step Implementation

* First, I created a file named `restaurantCore.py`.
* I implemented a `createLedger()` function that creates `ledger.txt` only if it does not already exist.
* Then, I created a `writeOrder()` function that accepts three arguments:

  1. Customer Name
  2. Item
  3. Price
* Initially, I did not implement any file-writing logic. I simply printed a success message to verify that the function was being called correctly.
* In the `main()` function, I first called `createLedger()` and verified that the ledger file was created successfully.
* I used predefined sample data to simulate customer orders.
* After confirming the flow, I implemented the file-writing logic using Python's normal file `write()` operation.
* I tested it to ensure that the records were correctly written to `ledger.txt`.
* Once that was working, I replaced the normal write logic with `mmap`-based file writing. At that stage, I still had some doubts about `mmap`, but I decided to understand it in more detail later.
* I tested the program again and confirmed that the `mmap` implementation worked correctly.
* Next, I started implementing multithreading.
* I first created a single thread for one customer and verified that it worked as expected.
* Then, I created multiple threads, with each thread representing a different customer placing an order.
* During testing, I noticed that the data written to the file was becoming inconsistent because multiple threads were trying to access the shared file simultaneously.
* After analyzing the issue, I realized that only one thread should be allowed to access the shared resource at a time.
* To solve this race condition, I introduced a `threading.Lock`.
* The lock ensured that only one thread could write to the ledger file at any given time while the others waited.
* After implementing the lock, I tested the program again, and the data was written correctly without any corruption.



# Understanding of `mmap` 

## 1. Problem Without `mmap`

* File data must be copied from disk → RAM
* Program works on RAM copy
* Changes must be written back 

---


## 2. What `mmap` changes

`mmap` removes the need for explicit copying.

Instead:

* The file is linked directly to virtual memory
* The program works with that memory region
* The OS handles loading and saving automatically

---

## 3. What memory mapping means

* Virtual memory addresses represent file data
* The file is not directly loaded into RAM at the start
* The OS decides when data is actually loaded

Memory mapping is:

> A mechanism where the operating system connects a file to a region of a process virtual memory.
---

## 4. Why `mmap` exists

* Avoid manually reading and writing file data
* Allow direct access to file contents
* Let the operating system handle data movement efficiently

 `mmap allows a program to access file data using memory-style operations instead of manual read/write.`

---

## 5. What `mmap.mmap()` does

```python
mmap.mmap(f.fileno(), 0)
```

This tells the OS:

* Use the file identified by the file descriptor
* Map the entire file (`0` means full file)
* Create a memory-mapped region for it

The result is a memory-mapped object.

---

## 6. What `f.fileno()` means

`f.fileno()` returns a file descriptor.

A file descriptor is:

* An integer assigned by the OS
* Used to identify an open file
* Used internally for system-level operations

---

## 7. What virtual memory is doing here

Each process has its own virtual memory space.

When `mmap` is used:

* A region of virtual memory is assigned to represent the file
* Each virtual address corresponds to a file byte offset
* The OS manages this mapping

---

## 8. Important clarification: no immediate copying

When `mmap` is created:

* File data is NOT fully loaded into RAM
* Only the mapping is created
* Data is loaded only when accessed

This is called demand-based loading.

---

## 9. What the `mmap` object is

The returned object (`mm`) is:

* A byte-level interface to the mapped memory region
* A view of the file through virtual memory
* Not a file, not a string, not a normal byte array

It allows:

* Reading bytes using indexing
* Writing bytes using slicing

---

## 10. What happens when you access `mm[i]`

When you write:

```python
value = mm[10]
```

The operating system does the following:

### Step 1: Receive memory access request

The program requests a byte at a virtual memory address.

### Step 2: Identify mapping

The OS checks which file is mapped to that memory region.

### Step 3: Convert memory address to file offset

It translates:

* Virtual memory position → file position

### Step 4: Load data if needed

* If data is not in RAM, it is loaded from disk
* If already in RAM, it is reused

### Step 5: Return result

The byte is returned to the program.

---

## 11. What happens when you write `mm[i] = value`

When modifying:

* Change is written to memory first
* OS marks that memory page as modified (dirty)
* Data is written back to disk

---

## 12. What `flush()` does

`mm.flush()`:

* modified memory pages to be written back to the file on disk
* Ensures file and memory are synchronized

---

## simplified definition

> `mmap` is an operating system mechanism that maps a file into a process’s virtual memory so that file data can be accessed and modified as if it were memory, while the OS handles loading and saving automatically.

---

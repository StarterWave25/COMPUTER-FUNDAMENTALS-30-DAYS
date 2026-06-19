# PATNAM PRUDVINATH - OBSERVATION ON FILE SYSTEMS

## Part - 1 [History & Purpose of File Systems]

```
Initially Storage Devices existed.

Examples:
- Punch Cards
- Magnetic Tapes
- Drums
- Disks

Problem Solved:
- Data can survive after Power OFF.
```

```
New Problem:

Storage can store Data.

But,

How do we find that Data later?
```

```
Early Storage only contained:

Block 0
Block 1
Block 2
Block 3
...

Just Raw Storage.
```

```
Programmers needed to remember:

Employee Data -> Block 17
Payroll Data -> Block 43
Program A -> Block 98

Everything was managed manually.
```

```
Problems:

- Easy to lose data.
- Easy to overwrite data.
- Difficult to locate data.
- Impossible to manage large systems.
```

```
As computers became larger:

- More Programs
- More Users
- More Data

appeared.

Raw Blocks were no longer practical.
```

```
Solution Proposed:

Files
```

```
Instead of:

Data starts at Block 153

Users can say:

employee.txt
report.txt
image.jpg
```

```
New Problem:

Soon systems contained:

100 Files
1000 Files
10000 Files

How do we organize them?
```

```
Solution Proposed:

Directories (Folders)
```

```
Documents/
Photos/
Programs/
Projects/
```

```
New Problem:

Many users now share the same computer.

Question:

Who can access which files?
```

```
Solution Proposed:

Permissions

- Read
- Write
- Execute
- Ownership
```

```
Modern File Systems manage:

- File Names
- Directories
- Permissions
- Storage Allocation
- Metadata
- Recovery
- Large Disks
- Multiple Users
```

```
Fundamental Problem Solved:

Storage devices can store data,

but there must be a way to:

- Organize it
- Locate it
- Protect it
- Manage it
- Retrieve it efficiently
```

---

## Part - 2 [Data Flow, Components, Internal Working]

### Data Here

```
File Names
File Data
Directories
Permissions
Metadata
Disk Block Numbers
Read Requests
Write Requests
```

---

### Components

```
User Program
↓

System Call
↓

Kernel File System Layer
↓

File System
(NTFS / EXT4 / FAT32 etc.)

↓

Storage Driver

↓

Disk / SSD
```

---

### Complete Flow Of Reading A File

```
Program

open("data.txt")

↓

System Call

↓

Kernel

↓

File System

[Searches File Metadata]

↓

Directory Structure

[Finds data.txt]

↓

File Metadata

[Finds Disk Blocks]

↓

Disk / SSD

[Reads Actual Data]

↓

Kernel Buffer

[Stores Retrieved Data]

↓

System Call Returns

↓

Program Receives Data
```

---

### Complete Flow Of Writing A File

```
Program

write("Hello")

↓

System Call

↓

Kernel

↓

File System

[Find Free Space]

↓

Metadata Updated

↓

Disk / SSD

[Stores Data]

↓

Kernel

[Confirms Write]

↓

Program Continues
```

---

## Questions To Know Internal Working

```
1. How does the OS find a file?
2. Where is file information stored?
3. How does reading happen?
4. How does writing happen?
5. How are free spaces tracked?
6. How are permissions enforced?
```

---

### First Answer

```
How Does OS Find A File?

Directory
↓
File Metadata
↓
Disk Blocks
↓
Actual Data
```

---

### Second Answer

```
File Information is stored in:

Metadata Structures

Examples:

- Inodes (Linux)
- MFT Entries (Windows NTFS)

Stored on Disk.
```

---

### Third Answer

```
Read Process

Program Requests File
↓
Kernel Receives Request
↓
File System Finds Metadata
↓
Locate Disk Blocks
↓
Read Data From SSD
↓
Return Data To Program
```

---

### Fourth Answer

```
Write Process

Program Sends Data
↓
Kernel Receives Data
↓
File System Finds Free Blocks
↓
Store Data On Disk
↓
Update Metadata
↓
Return Success
```

---

### Fifth Answer

```
File System Maintains:

Free Space Information

Which Blocks Are:

- Used
- Free

This prevents files from overwriting each other.
```

---

### Sixth Answer

```
Program Requests File
↓
Kernel Checks Permissions
↓
Allow / Deny
↓
Continue
```

---

### Interesting Observation

```
Applications never know:

- Exact Disk Location
- Exact Sector Number
- Exact Physical Address

Applications only know:

data.txt

The File System hides all storage complexity.
```

## Part - 3 [In-Depth Internal Working Process of FS]

```
Superblock          - Stores filesystem-wide info (size, block size, free counts)

Inode               - Stores file metadata (permissions, size, timestamps, block pointers)

Directory Entry     - Maps File Name to Inode Number

Direct Pointer      - Inode pointer that points straight to a Data Block

Indirect Pointer    - Inode pointer that points to a block full of more pointers

Extent              - A (start block, length) pair describing a contiguous range

Bitmap              - Tracks which blocks are Used (1) or Free (0)

Free List           - Linked list chaining together all free blocks

Journal             - Write-ahead log recording changes before they happen

Page Cache          - RAM area holding recently read/written data for speed

Data Block          - Actual raw storage where file content lives
```
```
Program

write("Hello", "data.txt")

↓
[ System Call Triggered — Program asks Kernel to perform the write ]

↓
[ Kernel Receives Request — Hands off control to the File System layer ]

↓
[ File System Checks Directory — Looks up "data.txt" to find its Inode Number ]

↓
[ Inode Located — Inode metadata is read into memory ]

↓
[ Free Space Check — Bitmap / Free List / B-Tree is scanned to find free Data Blocks ]

↓
[ Journal Entry Written — Filesystem logs "intent": which blocks, which inode, which bitmap will change ]

↓
[ Journal Entry Flushed — Intent log is confirmed safely on disk before any real change happens ]

↓
[ Data Written to Block — Actual "Hello" content is written into the chosen free Data Block(s) ]

↓
[ Inode Updated — Inode's pointer (Direct / Indirect / Extent) now references the new Data Block ]

↓
[ Bitmap Updated — Block(s) just used are marked from Free (0) to Used (1) ]

↓
[ Directory Entry Updated — If new file, (Name, Inode Number) pair is added to parent directory ]

↓
[ Journal Marked Complete — Logged intent is marked committed, so it won't be replayed again ]

↓
[ Kernel Buffer Updated — Page Cache holds the new data for fast future access ]

↓
[ System Call Returns — Program is told the write succeeded ]

↓
Program Continues

```
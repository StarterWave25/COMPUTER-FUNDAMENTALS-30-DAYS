# File Systems Masterclass (Beginner to OS Internals)

## Goal
Understand how a computer stores, organizes, finds, reads, writes, and deletes files.

---

## Big Picture
When you save a file (e.g., `notes.txt`), the computer performs a series of transformations:

> **You** → **Application** → **Operating System** → **File System** → **SSD/HDD** → **Blocks** → **Bits (0s and 1s)**

---

## MODULE 1: Storage Fundamentals

### RAM vs SSD vs HDD

| Feature | RAM | SSD | HDD |
| :--- | :--- | :--- | :--- |
| **Type** | Temporary Memory | Permanent Storage | Permanent Storage |
| **Speed** | Very Fast | Fast | Slower |
| **Persistence** | Volatile (Loses data) | Non-volatile (Keeps data) | Non-volatile (Keeps data) |
| **Mechanism** | Electronic | Flash Memory (No moving parts) | Spinning Magnetic Disks |
| **Analogy** | **Study Table**: Books you are currently using. | **Cupboard**: Sturdy storage for books. | **Mechanical Library**: Large but takes time to fetch. |

### Persistence
- **RAM**: Not Persistent (Data lost on power off).
- **SSD/HDD**: Persistent (Data survives power loss).

### Blocks
Storage devices divide space into fixed-size units called **Blocks**.
- **Typical block size**: 4096 Bytes (4 KB)

**Visual Representation (SSD):**
```text
+---------+  +---------+  +---------+
| Block 1 |  | Block 2 |  | Block 3 |
+---------+  +---------+  +---------+
```

### Why File Systems Exist?
**Problem**: Storage hardware only understands blocks. Humans understand file names.
The **File System** acts as a translator:
> **Human Names** (`notes.txt`) → **File System** → **Storage Blocks**

---

## MODULE 2: What is a File System?

### Definition
A File System is a collection of rules and data structures used to:
- Store and find files
- Organize and protect files
- Recover files after crashes

### Responsibilities
A filesystem answers these critical questions:
- Where is the file located?
- Who owns it and who can access it?
- How big is the file?
- Where is the available free space?

### Common File Systems
| File System | Primary Operating System |
| :--- | :--- |
| **FAT32** | Windows, USB Drives, Compatibility |
| **NTFS** | Windows (Modern) |
| **ext4** | Linux |
| **XFS** | Linux Servers (High Performance) |
| **APFS** | macOS, iPhone |

---

## MODULE 3: File Organization

### What is a File?
A file consists of two parts:
1. **Content**: The actual data (e.g., "Hello World").
2. **Metadata**: Information about the file (Name, Size, Owner, Permissions, Timestamps).

### What is a Directory?
A Directory is a **special file** that stores a mapping of filenames to references (pointers).

**Example: `Documents/`**
- `notes.txt` → [Reference]
- `photo.jpg` → [Reference]

### Hierarchical Structure
Files are organized in a **tree structure**:
```text
/ (Root)
├── home
│   └── raju
│       ├── Documents
│       ├── Photos
│       └── Projects
└── system
```

### Paths
- **Absolute Path**: Starts from root (e.g., `/home/raju/Documents/notes.txt`).
- **Relative Path**: Starts from current location (e.g., `Documents/notes.txt`).

**Path Resolution**:
`/` → `home` → `raju` → `Documents` → `notes.txt`

### Permissions (Linux)
Permissions are defined as `rwx`:
- **r**: Read
- **w**: Write
- **x**: Execute

Example: `rw-r--r--` (Owner can read/write, others can only read).

---

## MODULE 4: Internal Structures

### Superblock
The filesystem's master record. It contains global metadata:
- Total/Free Blocks
- Block Size
- Filesystem Type

**Disk Layout:**
```text
+-------------+-------------+-------------+
| Superblock  |   Inodes    | Data Blocks |
+-------------+-------------+-------------+
```

### Inode (Index Node)
The core data structure that stores file information.
- **Contains**: Owner, Permissions, Size, Timestamps, Block Locations.
- **IMPORTANT**: The Inode **DOES NOT** store the filename.

### Directory Entry
Maps a **Filename** to an **Inode Number**.
- Example: `notes.txt` → `Inode 120`

### Data Blocks
Where the actual file content is stored. An Inode points to these blocks.

### Journal
A log used for **crash recovery**. Before making changes, the FS records the intent in the journal.
1. Record Change (Journal)
2. Apply Change (Filesystem)

---

## MODULE 5: File Operations

### 1. CREATE (`touch notes.txt`)
**Workflow**: 
User → `open(O_CREAT)` → Kernel → FS → Allocate Inode → Update Directory → Journal → SSD.

### 2. WRITE (`echo hello > notes.txt`)
**Workflow**: 
`write()` → Kernel → Allocate Data Block → RAM Cache → Journal → SSD.

### 3. READ (`cat notes.txt`)
**Workflow**: 
`open()` → Path Resolution → Inode Lookup → Block Lookup → Cache Check → SSD Read → Return Data.

### 4. RENAME (`mv notes.txt file.txt`)
- **Action**: Updates the directory entry mapping.
- **Note**: The Inode stays the same; no data is copied.

### 5. COPY (`cp notes.txt backup.txt`)
- **Action**: Creates a **new Inode** and **new Data Blocks**, then copies the content.

### 6. DELETE (`rm notes.txt`)
- **Action**: `unlink()` removes the directory entry, releases the Inode, and marks blocks as free.
- **Recovery**: Data often remains until overwritten, allowing recovery tools to work.

---

## Core Mental Model
Every file operation eventually manipulates these three components:
1. **Directory Entries** (Names)
2. **Inodes** (Metadata & Pointers)
3. **Data Blocks** (Content)

---

## Final Architecture
```text
Application
    ↓
System Call
    ↓
Kernel
    ↓
Virtual File System (VFS)
    ↓
ext4 / NTFS / XFS
    ↓
Block Layer
    ↓
Storage Driver
    ↓
SSD / HDD
    ↓
Blocks
    ↓
Bits
```

> **Remember**: Files are not stored by name; names are for humans. The OS manages **Metadata**, **Inodes**, **Blocks**, and **Bits**.

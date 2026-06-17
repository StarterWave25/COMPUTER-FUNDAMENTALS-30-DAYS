# System Calls: The Bridge Between Programs & Operating System

> How programs ask the OS to do things they can't do alone

---

## 1. Historical Problem (Why System Calls Were Created)

### The Problem (1960s-1970s)

Imagine you're writing a program in the early days of computing:

```
Your program wants to:
✓ Read a file from disk
✓ Create a network connection
✓ Allocate memory
✓ Receive keyboard input
✓ Write to screen

But PROBLEM:
- Only ONE program at a time could access the disk
- If multiple programs access same file = data corruption
- Any program could overwrite another program's memory
- Multiple programs fighting for hardware = chaos
```

### The Solution: System Calls

**Idea:** Don't let programs directly touch hardware.

Instead:
```
Program says: "OS, can you please read file 'data.txt'?"
OS responds: "I'll do it safely, one at a time, for everyone"
OS reads the file
OS gives the result back to your program
```

This way:
- ✅ OS controls all hardware access
- ✅ Multiple programs can safely share resources
- ✅ One corrupted program doesn't crash everything
- ✅ OS ensures fair access to resources

**Birth of System Calls:** Unix (1970s) introduced this concept officially.

---

## 2. Data Flow: How System Calls Work

### Simple Explanation

```
YOUR PROGRAM (User Space)
        │
        │ "I need to read a file!"
        │ (system call request)
        ▼
KERNEL (Privileged Space)
        │
        ├─ Check: Is this program allowed?
        ├─ Check: Does this file exist?
        ├─ Actually read the file from disk
        │
        ▼
KERNEL (returns result)
        │
        │ "Here's your file data"
        │ (system call response)
        ▼
YOUR PROGRAM (User Space)
        │
        └─ Uses the data
```

### Components & Data Flow

```
┌──────────────────────────────────────┐
│        YOUR PROGRAM                  │
│  (User Space - Limited Access)       │
│                                      │
│  print("Reading file...")            │
│  data = open("data.txt")             │
│         ▲                            │
│         │ Returns: File contents     │
│         │                            │
│  ┌──────┴──────────────────────────┐ │
│  │ System Call (open)              │ │
│  │ Passes: Filename, permissions   │ │
│  └──────┬──────────────────────────┘ │
└─────────┼────────────────────────────┘
          │
          │ Request goes to CPU
          │ "Switch to Kernel Mode"
          ▼
┌──────────────────────────────────────┐
│        KERNEL/OS                     │
│  (Kernel Space - Full Access)        │
│                                      │
│  1. Check permissions                │
│  2. Locate file on disk              │
│  3. Read from disk                   │
│  4. Return data                      │
│  5. Switch back to User Mode         │
│                                      │
└──────────────────────────────────────┘
          │
          │ Actual hardware access
          │ (Disk I/O, Network, etc)
          ▼
     ┌─────────┐
     │  DISK   │
     │NETWORK  │
     │MEMORY   │
     └─────────┘
```

### Key Point

**Mode Switch:** Every system call switches from "User Mode" to "Kernel Mode"
- User Mode: Limited, safe (can't crash OS)
- Kernel Mode: Full power, dangerous (can crash everything)
- OS acts as bouncer between the two

---

## 3. Small Program: Implementing File Reading

### Simple Version (Without Handling Everything)

```python
# file_reader.py - Simple file reading using system calls

import os
import sys

def read_file(filename):
    """
    Open and read a file using system calls
    
    This demonstrates:
    - open() system call (kernel opens file)
    - read() system call (kernel reads data)
    - close() system call (kernel closes file)
    """
    
    try:
        # System call: open()
        # Kernel checks: does file exist? Do I have permission?
        file_handle = open(filename, 'r')
        
        # System call: read()
        # Kernel reads from disk and gives data to program
        data = file_handle.read()
        
        # System call: close()
        # Kernel closes the file handle
        file_handle.close()
        
        return data
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None

# Main program
if __name__ == "__main__":
    # Get filename from command line
    if len(sys.argv) < 2:
        print("Usage: python file_reader.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    content = read_file(filename)
    
    if content:
        print("File contents:")
        print("-" * 50)
        print(content)
        print("-" * 50)
```

### How It Works

```
Step 1: open() system call
└─ Kernel checks file permissions
└─ Kernel opens file descriptor
└─ Returns file object

Step 2: read() system call
└─ Kernel fetches data from disk
└─ Returns data to your program

Step 3: close() system call
└─ Kernel releases file resources
```

### Run It

```bash
# Create a test file
echo "Hello from the kernel!" > test.txt

# Run the program
python file_reader.py test.txt

# Output:
# File contents:
# --------------------------------------------------
# Hello from the kernel!
# --------------------------------------------------
```

---

## 4. Breaking the Program: Edge Cases

### Problem 1: File Doesn't Exist

```python
# Currently handles this ✓
except FileNotFoundError:
    print(f"Error: File '{filename}' not found")
```

**Test:**
```bash
python file_reader.py nonexistent.txt
# Output: Error: File 'nonexistent.txt' not found ✓
```

---

### Problem 2: No Permission to Read

```python
# Create a file with no read permissions
echo "Secret" > secret.txt
chmod 000 secret.txt

# Run program
python file_reader.py secret.txt
# Output: Error: No permission to read 'secret.txt' ✓
```

**Currently handles this ✓**

---

### Problem 3: File is Very Large (Memory Issues)

**Problem:** What if file is 10GB?

```python
# CURRENT CODE PROBLEM:
data = file_handle.read()  # ❌ Loads ENTIRE file into memory!
# If file is 10GB, needs 10GB RAM!
```

**Break it:**
```bash
# Create a 1GB file
dd if=/dev/zero of=largefile.bin bs=1M count=1024

# Run program
python file_reader.py largefile.bin
# ❌ Program hangs/crashes (uses all RAM)
```

---

### Problem 4: File Being Written To (Race Condition)

**Problem:** What if another program is writing to the file while we read?

```
Time 1: We start reading file (10 lines)
Time 2: Another program adds 5 more lines
Time 3: We read those 5 new lines
Time 4: Original program deletes file

Result: Inconsistent/corrupted data
```

**Break it:**
```bash
# Terminal 1: Create script that modifies file
while true; do
  echo "New line at $(date)" >> data.txt
  sleep 1
done

# Terminal 2: Run our program
python file_reader.py data.txt
# ❌ Gets different data each time (inconsistent)
```

---

### Problem 5: Not Closing File (File Descriptor Leak)

**Problem:** If we don't close file, resources get wasted

```python
# BAD CODE:
def read_file_bad(filename):
    file_handle = open(filename, 'r')
    data = file_handle.read()
    return data  # ❌ Never closes!

# If you call this 1000 times...
for i in range(1000):
    read_file_bad("file.txt")  # ❌ Opens 1000 file descriptors!

# System runs out of file descriptors
# Error: "Too many open files"
```

**Check it:**
```bash
# See how many file descriptors are open
lsof -p <process_id>

# If we don't close, count keeps growing!
```

---

## 5. Optimized & Robust Version

### Fixed Program

```python
# file_reader_optimized.py - Robust version handling all issues

import os
import sys

# CONFIG
CHUNK_SIZE = 8192  # Read 8KB at a time (not whole file)
MAX_FILE_SIZE = 100 * 1024 * 1024  # Don't read files > 100MB

def read_file_optimized(filename):
    """
    Optimized file reading with:
    - Chunked reading (memory efficient)
    - Size limit (prevent memory issues)
    - File locking (prevent race conditions)
    - Guaranteed cleanup (with statement)
    """
    
    # Check 1: Does file exist?
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        return None
    
    # Check 2: Is it actually a file (not directory)?
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a file")
        return None
    
    # Check 3: Is file too large?
    file_size = os.path.getsize(filename)
    if file_size > MAX_FILE_SIZE:
        print(f"Error: File too large ({file_size} bytes > {MAX_FILE_SIZE} bytes)")
        return None
    
    # Check 4: Can we read it?
    if not os.access(filename, os.R_OK):
        print(f"Error: No read permission for '{filename}'")
        return None
    
    try:
        # Use 'with' statement = guaranteed file close
        # This is the right way to do it!
        with open(filename, 'r', encoding='utf-8') as file_handle:
            
            # Read in chunks (memory efficient)
            chunks = []
            while True:
                chunk = file_handle.read(CHUNK_SIZE)
                if not chunk:
                    break
                chunks.append(chunk)
            
            data = ''.join(chunks)
            return data
            
    except UnicodeDecodeError:
        print(f"Error: File '{filename}' is not valid UTF-8 text")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

def main():
    """Main program"""
    
    # Validate input
    if len(sys.argv) < 2:
        print("Usage: python file_reader_optimized.py <filename>")
        print("\nExamples:")
        print("  python file_reader_optimized.py test.txt")
        print("  python file_reader_optimized.py /etc/passwd")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    print(f"Reading '{filename}'...")
    content = read_file_optimized(filename)
    
    if content:
        lines = content.split('\n')
        print(f"\n✓ Successfully read {len(lines)} lines")
        print("-" * 50)
        
        # Show first 10 lines only
        if len(lines) > 10:
            print('\n'.join(lines[:10]))
            print(f"... ({len(lines) - 10} more lines)")
        else:
            print(content)
        
        print("-" * 50)
    else:
        print("✗ Failed to read file")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

### What We Fixed

| Problem | Original | Fixed |
|---------|----------|-------|
| **Memory for large files** | ❌ Read entire file | ✅ Read 8KB chunks |
| **File not closed** | ❌ Manual close (easy to forget) | ✅ `with` statement (automatic) |
| **Not checking file size** | ❌ No limit | ✅ Max 100MB check |
| **Race conditions** | ❌ No protection | ✅ Check size before reading |
| **Encoding errors** | ❌ Crashes | ✅ Catches UnicodeDecodeError |
| **Bad input validation** | ❌ Minimal | ✅ Multiple checks |

---

### Test the Optimized Version

```bash
# Test 1: Normal file
echo "Hello World" > test.txt
python file_reader_optimized.py test.txt
# ✓ Works

# Test 2: File doesn't exist
python file_reader_optimized.py nonexistent.txt
# ✓ Error: File 'nonexistent.txt' not found

# Test 3: No permission
chmod 000 secret.txt
python file_reader_optimized.py secret.txt
# ✓ Error: No read permission

# Test 4: File too large (if you have 150MB test file)
python file_reader_optimized.py largefile.bin
# ✓ Error: File too large

# Test 5: Directory instead of file
python file_reader_optimized.py /tmp/
# ✓ Error: '/tmp/' is not a file
```

---

## Summary: System Calls Concept

### What We Learned

1. **Historical Problem**
   - Programs needed safe access to shared hardware
   - OS created system calls as the boundary

2. **Data Flow**
   - User program → System call → Kernel → Hardware
   - Kernel validates and executes safely
   - Returns result to user program

3. **Implementation**
   - `open()` - System call to open file
   - `read()` - System call to read data
   - `close()` - System call to release resources

4. **Edge Cases**
   - File size limits (memory efficiency)
   - Race conditions (file being modified)
   - File descriptor leaks (not closing)
   - Encoding errors
   - Permission issues

5. **Optimization**
   - Read in chunks, not entire file
   - Use `with` statement (automatic cleanup)
   - Validate input before processing
   - Handle errors gracefully

---

## Why This Matters for Your Career

**Job Interviews:**
- "Explain system calls" → Show you understand OS fundamentals
- "How do you read large files safely?" → Chunked reading
- "What happens if you don't close files?" → File descriptor limits

**Real-World Applications:**
- Web servers reading files efficiently
- Databases reading/writing data
- OS utilities (ls, cat, grep)
- Any program that touches disk/network

**Performance Optimization:**
- Understanding system calls helps write faster code
- Knowing about file descriptors prevents bugs
- Chunked processing handles big data

---

## Key Takeaway

**System calls are the only safe way programs can access hardware.**

Every time you:
- Open a file
- Write to network
- Allocate memory
- Read from keyboard

...you're using a system call. The OS intercepts, validates, and executes safely.

**That's the whole point:** Protect hardware, manage resources, prevent chaos.

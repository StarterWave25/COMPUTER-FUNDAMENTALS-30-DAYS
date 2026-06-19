# File System Commands - See What's Really Happening

A hands-on guide to understanding file systems by running actual commands.

---

## 🎯 Before You Start

Open your terminal and follow along. These commands work on:
- **Linux** ✅ (Ubuntu, Debian, Fedora, etc.)
- **macOS** ✅ (mostly the same)
- **Windows WSL** ✅ (Windows Subsystem for Linux)

---

## Part 1️⃣: Basic File Operations

### Create a File
```bash
touch myfile.txt
```
**What happens:** File created with zero size, current timestamp recorded.

```bash
echo "Hello World" > myfile.txt
```
**What happens:** Content written to file, size becomes 11 bytes.

### View File Content
```bash
cat myfile.txt
```
**Output:**
```
Hello World
```

### List Files (See Metadata)
```bash
ls -l myfile.txt
```
**Output:**
```
-rw-r--r-- 1 jack users 11 Jun 19 10:30 myfile.txt
```

**Breaking it down:**
```
-rw-r--r--     = Permissions (owner: read+write, group: read, others: read)
1              = Number of hard links
jack           = Owner username
users          = Group name
11             = File size in bytes
Jun 19 10:30   = Last modification time
myfile.txt     = Filename
```

---

## Part 2️⃣: Understanding Inodes (File Metadata)

### View Inode Information
```bash
stat myfile.txt
```

**Output:**
```
  File: myfile.txt
  Size: 11          Blocks: 8          IO Block: 4096   regular file
Device: 10302h/66306d  Inode: 1234567   Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/  jack)   Gid: ( 1000/  users)
Access: 2024-06-19 10:30:45.123456789 +0530
Modify: 2024-06-19 10:30:45.123456789 +0530
Change: 2024-06-19 10:30:45.123456789 +0530
 Birth: -
```

**Key observations:**
- **Inode: 1234567** → This is the file's unique ID on disk
- **Size: 11** → Actual data is 11 bytes
- **Blocks: 8** → But file system allocates 8 blocks (4096 bytes) for storage! 💡
- **Links: 1** → File exists in one directory
- **Access/Modify/Change times** → All tracked by file system

### List Files with Inode Numbers
```bash
ls -i
```

**Output:**
```
1234567 myfile.txt    1234568 documents    1234569 image.jpg
```

**What it shows:** Each file/folder has a unique inode number. This is how the kernel tracks files internally.

---

## Part 3️⃣: Permissions in Action

### Check Current Permissions
```bash
ls -l myfile.txt
```

**Output:**
```
-rw-r--r-- 1 jack users 11 Jun 19 10:30 myfile.txt
```

**Reading permissions:**
```
-rw-r--r--
│
├─ First char: '-' = Regular file (d = directory, l = link, etc)
│
├─ Next 3 chars: 'rw-' = Owner can read + write, NOT execute
├─ Next 3 chars: 'r--' = Group can read ONLY
└─ Next 3 chars: 'r--' = Others can read ONLY
```

### Change Permissions
```bash
chmod 755 myfile.txt
```

**What changed:**
```
Before: -rw-r--r-- (644)
After:  -rwxr-xr-x (755)

Now: Owner can read+write+execute, Group can read+execute, Others can read+execute
```

**Explanation:**
- **7** = read(4) + write(2) + execute(1) = 7
- **5** = read(4) + execute(1) = 5
- **5** = read(4) + execute(1) = 5

### Make File Read-Only
```bash
chmod 444 myfile.txt
```

**Try to write:**
```bash
echo "New content" > myfile.txt
```

**Error:**
```
bash: myfile.txt: Permission denied
```

**Why?** File system checked permissions. Owner doesn't have write access. ✅ Security working!

### Restore Write Permission
```bash
chmod 644 myfile.txt
```

---

## Part 4️⃣: Disk Space & Storage

### Check Overall Disk Usage
```bash
df -h
```

**Output:**
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G  45G  55G   45%  /
/dev/sda2       200G  120G 80G   60%  /home
tmpfs           16G  2.1G 14G   13%  /dev/shm
```

**What it shows:**
- **Filesystem** → Device name (sda1 = disk A, partition 1)
- **Size** → Total capacity (100G)
- **Used** → Already used (45G)
- **Avail** → Free space (55G)
- **Use%** → Percentage used
- **Mounted on** → Where it's accessible in file system

### Check Specific Directory Size
```bash
du -sh /home/jack/
```

**Output:**
```
12G     /home/jack/
```

**What it shows:** Jack's home directory uses 12GB.

### See Size of Each Subdirectory
```bash
du -h /home/jack/ | sort -h
```

**Output:**
```
250M    /home/jack/Downloads
2.5G    /home/jack/Documents
4.8G    /home/jack/Videos
1.2G    /home/jack/.cache
```

**Insight:** Videos folder is taking the most space. Delete or compress it to free up space.

---

## Part 5️⃣: File System Structure

### View Directory Tree
```bash
tree /home/jack -L 2
```

**Output:**
```
/home/jack/
├── Documents
│   ├── resume.pdf
│   ├── certificate.pdf
│   └── projects
├── Downloads
│   ├── installer.exe
│   └── setup.sh
├── Pictures
│   ├── photo1.jpg
│   └── photo2.jpg
└── .config
    ├── nginx
    └── docker
```

**What it shows:** Hierarchical directory structure. Folders can contain folders (nested).

### List with Detailed Info
```bash
ls -lR /home/jack
```

**Output:**
```
/home/jack/:
total 48
drwxr-xr-x  5 jack users 4096 Jun 19 12:00 Documents
drwxr-xr-x  3 jack users 4096 Jun 18 10:30 Downloads

/home/jack/Documents:
total 250
-rw-r--r-- 1 jack users 245000 Jun 15 14:22 resume.pdf
-rw-r--r-- 1 jack users  50000 Jun 10 09:15 certificate.pdf
```

---

## Part 6️⃣: Finding Files

### Find File by Name
```bash
find /home/jack -name "*.txt"
```

**Output:**
```
/home/jack/Documents/notes.txt
/home/jack/Downloads/list.txt
/home/jack/todo.txt
```

**What it does:** Searches entire `/home/jack` directory tree for files ending in `.txt`.

### Find Files Larger Than 100MB
```bash
find /home/jack -size +100M
```

**Output:**
```
/home/jack/Videos/movie.mp4 (750M)
/home/jack/Downloads/iso_file.iso (1.2G)
```

### Find Recently Modified Files
```bash
find /home/jack -type f -mtime -7
```

**Output:**
```
/home/jack/Documents/project.txt (modified 2 days ago)
/home/jack/resume.pdf (modified 1 day ago)
```

**What it means:** `-mtime -7` = modified in last 7 days.

---

## Part 7️⃣: File Operations at Scale

### Copy File (Creates New Inode)
```bash
cp myfile.txt myfile_copy.txt
```

**Check inodes:**
```bash
ls -i myfile*
```

**Output:**
```
1234567 myfile.txt
1234570 myfile_copy.txt
```

**Key insight:** Different inodes! Two separate files, even though content is identical.

### Create Hard Link (Same Inode)
```bash
ln myfile.txt myfile_hardlink.txt
```

**Check inodes:**
```bash
ls -i myfile*
```

**Output:**
```
1234567 myfile.txt
1234567 myfile_hardlink.txt        ← SAME INODE!
1234570 myfile_copy.txt
```

**What happened:**
- Hard link points to **same inode** as original
- Both filenames refer to same data
- If you modify one, both change
- Delete one? Other still works (data not deleted)

### Create Symbolic Link (Different Inode, Points to File)
```bash
ln -s myfile.txt myfile_symlink.txt
```

**Check inodes:**
```bash
ls -i myfile*
```

**Output:**
```
1234567 myfile.txt
1234567 myfile_hardlink.txt
1234570 myfile_copy.txt
1234571 myfile_symlink.txt         ← NEW INODE (points to myfile.txt)
```

**What it is:** Symbolic link is like a shortcut. Separate file that says "go read myfile.txt".

---

## Part 8️⃣: Ownership & Access Control

### Check File Owner
```bash
ls -l myfile.txt
```

**Output:**
```
-rw-r--r-- 1 jack users 11 Jun 19 10:30 myfile.txt
           │ │    │
           │ │    └─ Group: users
           │ └──── Owner: jack
           └─────── Link count
```

### Change Owner
```bash
sudo chown alice myfile.txt
```

**Check result:**
```bash
ls -l myfile.txt
```

**Output:**
```
-rw-r--r-- 1 alice users 11 Jun 19 10:30 myfile.txt
```

**Now alice is the owner.** Only alice (or root) can modify it.

### Change Group
```bash
sudo chgrp developers myfile.txt
```

**Check result:**
```bash
ls -l myfile.txt
```

**Output:**
```
-rw-r--r-- 1 alice developers 11 Jun 19 10:30 myfile.txt
```

---

## Part 9️⃣: Watching File System Changes in Real-Time

### Monitor File System Activity
```bash
watch -n 1 'ls -lh /home/jack/Downloads/'
```

**What it does:** Refreshes the directory listing every 1 second. See files appear/disappear in real-time as you download.

### Track File Modifications
```bash
inotifywait -m /home/jack/Documents
```

**Output (as you create/modify files):**
```
Setting up watches.
/home/jack/Documents/ CREATE notes.txt
/home/jack/Documents/ MODIFY notes.txt
/home/jack/Documents/ DELETE notes.txt
```

**See events happening live!**

---

## Part 🔟: Disk/Partition Details

### View Disk Partitions
```bash
lsblk
```

**Output:**
```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0  500G  0 disk
├─sda1   8:1    0  100G  0 part /
├─sda2   8:2    0  200G  0 part /home
└─sda3   8:3    0  200G  0 part /var
sdb      8:16   0 1000G  0 disk
└─sdb1   8:17   0 1000G  0 part /backup
```

**What it shows:**
- **sda** = First disk (500GB total)
  - sda1 = Partition 1 (100GB, mounted at `/`)
  - sda2 = Partition 2 (200GB, mounted at `/home`)
- **sdb** = Second disk (1TB, used for backup)

### View File System Type
```bash
df -T
```

**Output:**
```
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4   100G  45G  55G   45%  /
/dev/sda2      ext4   200G  120G 80G   60%  /home
tmpfs          tmpfs  16G  2.1G 14G   13%  /dev/shm
```

**What it shows:** File system type:
- **ext4** = Linux native (fast, reliable)
- **tmpfs** = RAM-based (fast, temporary)

---

## Part 1️⃣1️⃣: Advanced: Tracing System Calls

### See What File Operations Program Does
```bash
strace -e openat,read,write cat myfile.txt
```

**Output:**
```
openat(AT_FDCWD, "myfile.txt", O_RDONLY) = 3      ← Open file, get file descriptor 3
read(3, "Hello World", 4096)                       ← Read from file descriptor 3
write(1, "Hello World\n", 12)                      ← Write to stdout
close(3)                                           ← Close file descriptor
```

**What it shows:** Exactly what system calls the program makes to interact with the file system!

---

## Part 1️⃣2️⃣: Practical Exercises

### Exercise 1: Find Your Largest Files
```bash
find ~ -type f -exec ls -lh {} \; | sort -k5 -h | tail -20
```

**See:** Top 20 largest files in your home directory.

### Exercise 2: Find Files Not Accessed in 30 Days
```bash
find ~ -type f -atime +30
```

**Use case:** Clean up unused files to free disk space.

### Exercise 3: Check Inode Usage (Not Just Disk Space)
```bash
df -i
```

**Output:**
```
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1       6553600 2345600 4208000  36%  /
/dev/sda2      13107200 5432100 7675100  41%  /home
```

**Why it matters:** You can run out of inodes even if disk space is free! (Many small files = many inodes used)

### Exercise 4: Compare File Sizes (Apparent vs Actual)
```bash
ls -lh myfile.txt        # Apparent size
du -h myfile.txt         # Actual disk usage
```

**Output:**
```
-rw-r--r-- 1 jack users 11 Jun 19 10:30 myfile.txt    ← Apparent: 11 bytes
4.0K    myfile.txt                                      ← Actual: 4KB block allocation
```

---

## 🎓 Key Takeaways

| Command | What It Shows |
|---------|---------------|
| `ls -l` | Permissions, owner, size, timestamp |
| `stat` | Everything about a file (inode, blocks, times) |
| `df -h` | Disk space usage per partition |
| `du -h` | Directory size (recursive) |
| `find` | Locate files by name, size, date |
| `chmod` | Change permissions in action |
| `chown` | Change ownership |
| `ls -i` | See inode numbers |
| `ln` | Create hard/symbolic links |
| `strace` | See actual system calls |

---

## 💡 What You Learned by Running These Commands

1. **Permissions work** → `chmod 444` → Can't write → File system enforces it! ✅

2. **Inodes are real** → Each file has unique ID → Hard links share inode

3. **Disk blocks are allocated** → 11-byte file uses 4KB block → Space is wasted but that's okay

4. **Metadata is stored** → Modification times, ownership, permissions all kept by file system

5. **File system is hierarchical** → Folders contain folders → Tree structure not flat

6. **Multiple disks exist** → `/dev/sda`, `/dev/sdb` → You can have many storage devices

7. **System calls are the API** → Programs ask OS via `open()`, `read()`, `write()` to access files

---

## 🚀 Next Experiments

1. **Create your own folder structure** and explore with `du`, `find`
2. **Monitor a download** with `watch` command - see file grow in real-time
3. **Create hard/symbolic links** and modify them - see what happens
4. **Compare** two file systems (ext4 vs others) using `df -T`
5. **Find your old files** using `find -mtime +90` and clean up
# **File System**

## **Why file system was invented & what problem it solve in the history?**
### **Problem:**
1. The early computers stored the data only in RAM. The data can live upto the power is supplied to computer. If power went of then the data will be erased. For to solve the problem punch cards, magnetic tapes, disks are invented to store the data permanently. But they created another problem how does the disk actually organize the millions of bits of data.
2. To know where a specific program lives in the disk, humans need to remember the sectors like sector 45 - 60. But humans cannot easily remember the numbers they need names.

### **Solution:**
1. For to keep the names for the files, the file system ws introduced. This is the major purpose for file system. Number of files were increased finding them became difficult. So, to group related files we got to introduced to Directories.
2. Next deleting a file from the disk frees the memory but it cannot track them to use the free space for another files to solve that file systems introduced allocation tables, bitmaps, metadata structures to track used & unused blocks.


## **Components & Flow**
!['Path'](images/2.jpeg)
!['Inodes'](images/1.jpeg)
!['Drivers'](images/3.jpeg)
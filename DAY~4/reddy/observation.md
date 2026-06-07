# Investigation 1 - Understanding My Current Location

## Objective

Understand:

* How to identify my current location
* What information the terminal provides
* How the operating system represents locations

---

## Observation

When I opened Command Prompt, I saw:

![currect location](./screenshots/)

Before typing any command, the terminal displayed a location.
 
---

## Question

In my brain it rises a question what is this.

The terminal is an application that provides a text-based interface to the operating system.

The terminal is not the operating system.

The terminal is a normal process created by the operating system.

The terminal allows users to issue commands.

The terminal performs the following actions:

Receives user input.
Interprets commands.
Sends requests to the operating system.
Receives results.
Displays output.

The terminal itself does not manage files, memory, or hardware.

The operating system performs those operations.

The terminal only provides an interface through which users interact with operating system services.

How does the terminal know where I am?
by using the path it know  where i am 

Why does it display this location?
by the using the commed cd it display the corrent location(path).

## Observation

When I execute:

```cmd
cd
```

the terminal immediately displays:

```text
C:\Users\Reddy
```

or the directory where the terminal is currently operating.

The result appears instantly without searching through files and directories.

---

## Question

How does the terminal know its current location?

Where is this information stored?

---

## Reasoning

The terminal is a running process.

Every process contains information that describes its current state.

One piece of information maintained by the operating system is the Current Working Directory (CWD).

When the terminal starts, the operating system assigns an initial working directory to the terminal process.

Example:

```text
Current Working Directory
=
C:\Users\Reddy
```

This information becomes part of the process state.

The process state is stored in memory while the process is running.

---

## What Happens When `cd Downloads` Executes?

Before execution:

```text
Current Working Directory
=
C:\Users\Reddy
```

The command:

```cmd
cd Downloads
```

requests that the operating system change the terminal's current working directory.

The operating system verifies that the directory exists.

If the directory exists, the operating system updates the current working directory value.

After execution:

```text
Current Working Directory
=
C:\Users\Reddy\Downloads
```

No files are moved.

No directories are created.

Only the current working directory value changes.

---

## What Happens When `cd` Executes?

When the command:

```cmd
cd
```

is executed, the terminal requests the current working directory from the operating system.

The operating system returns the value stored for that process.

The terminal displays the value on the screen.

The command does not search the SSD.

The command does not scan directories.

The information already exists in memory as part of the process state.

---

## Where Is The Current Working Directory Stored?

The current working directory is stored as part of the terminal process state.

Because the terminal is a running process, its state exists in RAM.

Therefore:

```text
Terminal Process
↓
Process State
↓
Current Working Directory
↓
Stored In RAM
```

The CPU does not permanently store this information.

The SSD does not need to be searched every time the `cd` command is executed.

The operating system keeps the value available in memory while the process is running.

---

## Why Is `cd` Fast?

The command executes quickly because the operating system does not need to search the filesystem.

The current working directory is already stored in memory.

The terminal simply requests the value and displays it.

This makes the operation extremely fast.

---

## Key Discoveries

1. The terminal is a process.
2. Every process has a current working directory.
3. The current working directory is part of the process state.
4. Process state is stored in RAM while the process is running.
5. `cd Downloads` changes the current working directory.
6. `cd` displays the current working directory.
7. The terminal does not search the SSD to determine its location.
8. The operating system maintains the current working directory information.

---

## Final Mental Model

```text
Terminal Process
↓
Current Working Directory Stored In Process State
↓
Process State Stored In RAM
↓
cd Reads Current Working Directory
↓
Terminal Displays Location
```

The `cd` command works because the operating system continuously maintains the current working directory for every running terminal process.


---

## Experiment



---

---

## What Information Does The Terminal Provide?

The terminal provides:

### 1. Current Working Directory

Example:

```text
C:\Users\Reddy Sekhar Reddy
```

This is the location where commands are executed.

---

### 2. Current Drive

Example:

```text
C:
```

This tells me which storage drive I am currently using.

---

### 3. Prompt Indicator

Example:

```text
C:\Users\Reddy Sekhar Reddy>
```

The `>` symbol indicates that the terminal is waiting for my next command.

---

## How Does The Operating System Represent Locations?

The operating system represents locations using paths.

Example:

```text
C:\Users\Reddy Sekhar Reddy
```

Breaking it down:

```text
C:
│
└── Users
     │
     └── Reddy Sekhar Reddy
```

Each folder is separated using:

```text
\
```

which means:

```text
inside
```

So:

```text
C:\Users\Reddy Sekhar Reddy
```

means:

```text
Drive C
↓
Inside Users
↓
Inside Reddy Sekhar Reddy
```

---

## Mental Model

Think of a postal address:

```text
Country
↓
State
↓
City
↓
Street
↓
House
```

Similarly:

```text
Drive
↓
Folder
↓
Subfolder
↓
File
```

A path is simply the address of a location inside the filesystem.

---

## What I Learned

The terminal always has a current location called the Current Working Directory.

The operating system represents locations using paths.

Paths act like addresses that help the operating system find files and directories.

Without paths, the operating system would not know where information is stored.

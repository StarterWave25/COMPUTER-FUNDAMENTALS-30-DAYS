# Day ~ 9 [Observations - PATNAM PRUDVINATH]

## Part - 1 [Why Was Secondary Storage Invented?]

### My Assumption:

---

Initially, I thought Hard Disks and SSDs were invented simply to save files.

So I assumed:

> Storage devices exist because users need a place to save photos, videos, and documents.

### My Research:

---

After researching, I found that saving files is only part of the answer.

The deeper reason is that computers need a way to remember information even after power is removed.

I already learned that:

* Registers lose data without power.
* Cache loses data without power.
* RAM loses data without power.

These components are called volatile memory.

If a computer only had volatile memory, everything would disappear whenever the system shut down.

Computers could calculate things, but they could not remember anything.

---

### The Problem Before Secondary Storage

Imagine a computer contains:

CPU <br>
↓ <br>
Registers <br>
↓ <br>
Cache <br>
↓ <br>
RAM <br>

But no permanent storage.

Now suppose I create:

* A Word document
* A Photo
* A Program
* An Operating System installation

Everything would exist only while power is available.

Flow:

Power ON <br>
↓ <br>
Use Computer <br>
↓ <br>
Power OFF <br>
↓ <br>
Everything Lost <br>

This makes computers impractical for everyday use.

---

### What Secondary Storage Solves

---

Secondary storage provides:

* Permanent Data Storage
* Long-Term Data Retention
* Operating System Storage
* Application Storage
* User File Storage

Flow:

Data Created <br>
↓ <br>
Stored In HDD / SSD <br>
↓ <br>
Power Removed <br>
↓ <br>
Data Remains Stored <br>

This allows computers to remember information across reboots.

---

### Interesting Observation

At first, I thought:

> HDDs and SSDs exist because RAM is small.

After researching, I realized that size is not the main reason.

The real reason is:

> RAM forgets. Secondary storage remembers.

---

### What Would Happen If Secondary Storage Did Not Exist?

---

Without secondary storage:

* Files could not be permanently saved.
* Applications would disappear after shutdown.
* Operating systems could not be permanently installed.
* Every boot would behave like a completely new computer.
* Users would lose all work whenever power is removed.

---

## Final Understanding

Secondary storage was invented because computers need permanent memory.

Registers, Cache, and RAM are designed for speed.

Secondary storage is designed for persistence.

The biggest thing I learned is:

> Secondary storage allows computers to remember information even when electricity disappears.

---

# Part - 2 [Important Components Inside An HDD]

### My Assumption:

---

Initially, I thought an HDD was simply a storage box that keeps files.

### My Research:

---

After researching, I found that an HDD is actually a collection of specialized mechanical and electronic components working together.

Each component has a specific responsibility.

---

### 1. Platters

---

Platters are circular disks inside the HDD.

They are coated with magnetic material.

This is where data physically lives.

The platter surface contains billions of tiny magnetic regions.

These regions store binary information using magnetic orientation.

Without platters:

> No data can be stored.

---

### 2. Spindle Motor

---

The spindle motor rotates the platters.

Typical speeds:

* 5400 RPM
* 7200 RPM
* 10000 RPM

The rotating platter allows the read/write head to access different data locations.

Without the motor:

> The storage surface cannot move beneath the head.

---

### 3. Read/Write Head

---

The read/write head performs two jobs:

* Writing magnetic data
* Reading magnetic data

It flies extremely close to the platter surface without touching it.

Without the head:

> Data cannot be written or read.

---

### 4. Actuator Arm

---

The actuator arm moves the read/write head.

Flow:

Outer Tracks <br>
↕ <br>
Inner Tracks <br>

Without the actuator arm:

> The head could only access one location on the platter.

---

### 5. Controller Board

---

The controller board acts as the HDD's brain.

Responsibilities:

* Receive commands
* Position the head
* Control the motor
* Translate addresses
* Perform error checking

Without the controller:

> The HDD components could not coordinate with each other.

---

# Part - 3 [Internal Working Of HDD]

### Step 1 - Data Request

---

Suppose the operating system wants to store:

```text
1010
```

The request is sent to the HDD controller.

---

### Step 2 - Locate Storage Area

---

The controller chooses a location on the platter.

Example:

```text
Track 120
Sector 8
```

---

### Step 3 - Move The Head

---

The actuator arm moves the read/write head to the correct track.

Flow:

Controller <br>
↓ <br>
Actuator Arm <br>
↓ <br>
Correct Track <br>

---

### Step 4 - Rotate The Platter

---

The spindle motor rotates the platter until the desired sector reaches the head.

Flow:

Track Found <br>
↓ <br>
Wait For Sector <br>
↓ <br>
Ready To Write <br>

---

### Step 5 - Writing Data

---

Electric current flows through the write head.

This creates a magnetic field.

The magnetic field aligns magnetic regions on the platter.

Example:

```text
→ → → → = 1

← ← ← ← = 0
```

The magnetic orientation becomes the stored bit.

---

### Step 6 - Reading Data

---

When data is requested:

Controller <br>
↓ <br>
Move Head <br>
↓ <br>
Locate Track & Sector <br>
↓ <br>
Read Magnetic Regions <br>

The read head senses magnetic changes.

Those changes become electrical signals.

The signals are converted into binary data.

Example:

```text
Magnetic Orientation
↓
Electrical Signal
↓
1010
```

---

### Complete HDD Flow

```text
CPU / Operating System
↓
HDD Controller
↓
Actuator Arm Moves
↓
Spindle Rotates Platter
↓
Head Reaches Target Location
↓
Write / Read Magnetic Data
↓
Convert To Binary
↓
Return Data
```

---

## Final Understanding

An HDD is not simply a place where files are stored.

It is a complete storage system made of mechanical and electronic components.

The platter stores data as magnetic orientations.

The motor rotates the platter.

The actuator positions the head.

The head reads and writes magnetic data.

The controller coordinates everything.

The biggest thing I learned is:

> An HDD does not store files directly. It stores magnetic orientations, which eventually become bits, bytes, files, applications, and operating systems.

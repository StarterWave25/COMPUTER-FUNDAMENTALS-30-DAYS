# How Data Is Actually Stored in Cache and Registers

## Short Answer

Both **registers** and **cache** store data as electrical states inside billions of transistors.

A bit is ultimately represented by:

```text
0 = Low Voltage
1 = High Voltage
```

However, registers and cache maintain those states differently.

---

## 1. How Data Is Stored in a Register

Registers are built from circuits called **flip-flops**.

A flip-flop is a small electronic circuit made from transistors that can remember one bit.

### One Bit

```text
State A = 0
State B = 1
```

Once set, the state remains until it is changed.

### Multiple Bits

A register is simply many flip-flops grouped together.

Example:

```text
8-bit Register

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0
 1    0    1    1    0    0    1    0
```

Each bit is stored by its own flip-flop.

### Example

Decimal 13:

```text
00001101
```

Each digit is stored in a separate flip-flop.

### Why Registers Are Fast

- Located inside the CPU core
- Extremely close to the ALU
- No searching required
- Directly addressed by instructions

Example:

```text
ADD R1, R2
```

The CPU immediately knows where R1 and R2 are.

---

## 2. How Data Is Stored in Cache

Caches are usually built using **SRAM (Static RAM)**.

### SRAM Cell

A typical SRAM cell uses:

```text
6 transistors
```

These transistors form a self-reinforcing circuit that maintains either:

```text
0
```

or

```text
1
```

as long as power is supplied.

### Physical View

```text
Transistor Network
      ↓
Electrical State
      ↓
Represents 0 or 1
```

Unlike DRAM, SRAM does not require periodic refreshing.

---

## Register vs Cache Storage

| Feature | Register | Cache |
|----------|----------|---------|
| Built From | Flip-Flops | SRAM Cells |
| Speed | Fastest | Very Fast |
| Size | Very Small | Larger |
| Location | Inside CPU Core | Near CPU Core |
| Access Time | ~1 Cycle | Few Cycles |

---

## 3. How an Entire Cache Is Organized

Cache stores data in blocks called **cache lines**.

Example:

```text
64-byte cache line
```

Instead of loading a single byte, the cache loads a block of nearby memory.

### Cache Structure

```text
Cache
│
├── Line 0
├── Line 1
├── Line 2
└── ...
```

Each line contains:

```text
Tag
Data
Status Bits
```

### Example

RAM:

```text
Address   Data
1000      A
1001      B
1002      C
1003      D
```

Cache stores:

```text
Tag = 1000

Data:
A B C D
```

---

## 4. How the CPU Finds Data in Cache

When the CPU requests an address:

```text
Need Address 1002
```

The cache controller:

1. Calculates the cache location
2. Reads the tag
3. Compares addresses

### Cache Hit

```text
Tag Matches
```

Data is returned immediately.

### Cache Miss

```text
Tag Does Not Match
```

Data must be fetched from RAM.

---

## 5. What Happens When Power Is Removed?

Registers:

```text
Power Off
↓
State Lost
```

Cache:

```text
Power Off
↓
State Lost
```

Both are **volatile memory**.

---

## Engineer's Mental Model

```text
SSD      = Filing Cabinet
RAM      = Desk
Cache    = Open Notebook
Register = Numbers in Your Head
ALU      = Calculator
```

Registers hold the values currently being used by the CPU.

Cache attempts to keep future data nearby before the CPU needs it.

The storage mechanism itself is relatively straightforward; the difficult engineering problem is deciding **which data should be kept in cache at any moment**.

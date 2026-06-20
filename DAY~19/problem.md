### Problem: The Memory Array

You are given an array of integers.

For **every element**, find the distance to the **nearest occurrence of the same value**.

If the value appears only once in the entire array, return `-1` for that position.

---

### Example

Input:

```text
[5, 2, 8, 2, 7, 5]
```

Output:

```text
[5, 2, -1, 2, -1, 5]
```

---

### Explanation

#### Index 0 → Value = 5

Another `5` exists at index `5`.

Distance:

```text
|5 - 0| = 5
```

Output:

```text
5
```

---

#### Index 1 → Value = 2

Another `2` exists at index `3`.

Distance:

```text
|3 - 1| = 2
```

Output:

```text
2
```

---

#### Index 2 → Value = 8

No other `8` exists.

Output:

```text
-1
```

---

#### Index 3 → Value = 2

Nearest `2` is at index `1`.

Distance:

```text
|3 - 1| = 2
```

Output:

```text
2
```

---

#### Index 4 → Value = 7

No other `7`.

Output:

```text
-1
```

---

#### Index 5 → Value = 5

Nearest `5` is at index `0`.

Distance:

```text
|5 - 0| = 5
```

Output:

```text
5
```

---

### More Interesting Example

Input:

```text
[1, 3, 1, 1, 4]
```

---

For index 0:

```text
1, 3, 1, 1, 4
^     ^
```

Distance = 2

---

For index 2:

There are two matching `1`s:

```text
index 0 → distance 2
index 3 → distance 1
```

Take the nearest.

Output = 1

---

For index 3:

Nearest matching `1` is at index 2.

Output = 1

---

Final Output:

```text
[2, -1, 1, 1, -1]
```

---

### What You Need To Build

Create a function:

```text
memoryArray(arr)
```

Input:

```text
[1, 3, 1, 1, 4]
```

Output:

```text
[2, -1, 1, 1, -1]
```

---

### Team Discussion (Before Coding)

Don't discuss algorithms first.

Discuss:

> Can we avoid checking every element against every other element?

> What information is missing at each position?

That's where the solution starts.
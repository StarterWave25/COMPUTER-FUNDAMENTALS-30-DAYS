# Problem: The Influence Array

You are given an integer array.

Each element has an "influence score".

The influence score of an element is:

> Number of elements to its left that are smaller than it
>
> minus
>
> Number of elements to its right that are larger than it

For every element, calculate its influence score.

---

## Example

Array:

```text
[4, 2, 7, 1, 5]
```

For 4:

Left smaller:

```text
none
```

Count = 0

Right larger:

```text
7, 5
```

Count = 2

Influence:

```text
0 - 2 = -2
```

---

For 2:

Left smaller:

```text
none
```

Count = 0

Right larger:

```text
7, 5
```

Count = 2

Influence:

```text
-2
```

---

For 7:

Left smaller:

```text
4,2
```

Count = 2

Right larger:

```text
none
```

Count = 0

Influence:

```text
2
```

---

Output:

```text
[-2, -2, 2, -4, 3]
```

(Verify the remaining values yourself.)

---

# Team Discussion Questions

Before coding:

### 1

How would a human solve this manually?

---

### 2

What information is missing at every index?

---

### 3

If the array has 1 million elements, what becomes expensive?

---

### 4

Can we compute left information separately from right information?

---

### 5

What if duplicate numbers exist?

---

# Extension Challenge

After solving it:

Define:

```text
Power Score =
Influence Score × Array Value
```

Find the element with maximum power score.

Now discuss:

* Does your previous solution still work?
* What extra information is needed?
* What changes?

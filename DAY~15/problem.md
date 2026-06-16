# Array Compression Cost

You are given an array of positive integers.

In one operation, you may choose any **contiguous subarray** and replace the entire subarray with a single element equal to the maximum value inside that subarray.

## Objective

Reduce the entire array into a single number.

The cost of each operation is:

```text
(length of chosen subarray) × (maximum value in that subarray)
```

Your goal is to minimize the total cost.

---

## Example

Array:

```text
[2, 5, 1]
```

Option 1:

Compress:

```text
[2, 5]
```

Cost:

```text
2 × 5 = 10
```

Array becomes:

```text
[5, 1]
```

Compress:

```text
[5, 1]
```

Cost:

```text
2 × 5 = 10
```

Total:

```text
20
```

But is this optimal?

---

# Input Constraints

```text
1 ≤ n ≤ 200
1 ≤ arr[i] ≤ 10^6
```

---

# What Makes This Interesting

If someone immediately asks:

> "Is this DP?"

They're already thinking wrong.

First ask:

* What changes after each operation?
* What information survives?
* What information disappears?
* Does operation order matter?
* Can greedy fail?
* Can local optimal choices destroy global optimality?

---

# Team Discussion Questions

Before coding, debate:

### 1

For:

```text
[1,2,3,4,5]
```

What is the optimal strategy?

---

### 2

For:

```text
[5,4,3,2,1]
```

Does the strategy change?

---

### 3

If all values are equal:

```text
[7,7,7,7,7]
```

What should happen?

---

### 4

Can you create a case where choosing the largest subarray first is terrible?

---

### 5

What information must be tracked to make a decision?

---

# The Real Goal

Don't solve this immediately.

Spend 30-45 minutes doing only:

```text
Small examples
↓
Observe patterns
↓
Generate hypotheses
↓
Try to break them
```

The skill you're training is:

> Constructing a solution from first principles instead of matching a known pattern.

That's much closer to real engineering problem solving.
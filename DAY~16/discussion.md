Since your team is learning **web development, Node.js, Express, databases, processes, OS fundamentals, and system design**, don't ask:

> "What is a system call?"

That's a memory question.

Ask questions that force everyone to discover system calls hiding inside software they already know.

---

# Challenge 1: The Invisible Factory

Imagine you build:

```text
React
  ↓
Express API
  ↓
MySQL
```

A user clicks:

```text
"Upload Resume"
```

and uploads a PDF.

### Question

**List every component that might get involved from the moment the user clicks Upload until the file is stored on disk.**

Rules:

* Do NOT skip layers.
* Keep asking:

  * Who receives it?
  * How does it move?
  * Who talks to whom?
  * What system calls are likely happening?

Then ask:

> At which points does user space stop and kernel space begin?

---

# Challenge 2: The Billion-Dollar Bug

Suppose Node.js gets a new feature:

```js
fs.readFileDirectDisk()
```

which bypasses the kernel completely.

### Question

Would you use it?

Why did operating systems spend decades creating kernels if applications could simply read disks directly?

This question usually changes how people think about kernels.

---

# Challenge 3: Who Actually Creates the File?

You execute:

```js
fs.writeFileSync("hello.txt", "Hi");
```

### Question

Who REALLY created the file?

Possible answers:

```text
Node.js
V8
Express
Kernel
SSD
```

Make everyone defend their answer.

Then keep asking:

> If Node creates it, why can't Node create a file when no OS exists?

---

# Ultimate Team Discussion

Give everyone this one:

> **A user clicks "Submit" on our website. Trace every important thing that happens until the data is stored in MySQL. For every step, identify:**
>
> * User Space or Kernel Space?
> * Which resource is being used?
> * Which system call might be involved?
> * What would break if the kernel disappeared?

If your team can answer that deeply, they won't just know system calls—they'll start seeing them hidden underneath every web application they build.
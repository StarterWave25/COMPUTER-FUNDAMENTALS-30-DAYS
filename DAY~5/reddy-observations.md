#  1. How Editing Works (Text Editor)

```
Keyboard Input
      ↓
RAM (Editor Process)
      ↓
Screen Display
```

### Save Operation

```
Ctrl + S
   ↓
RAM → SSD / HDD
```

 Git only reads files from **disk (SSD/HDD)**  
 Unsaved changes in RAM are NOT visible to Git

---

#  2. Undo / Redo System

```
UNDO STACK                REDO STACK
┌────────────┐          ┌────────────┐
│ Action 3   │          │ Action 2   │
│ Action 2   │          │ Action 3   │
│ Action 1   │          └────────────┘
└────────────┘
```

### Undo (Ctrl + Z)

```
Remove last action from Undo Stack
        ↓
Apply reverse change
        ↓
Push to Redo Stack
```

### Redo (Ctrl + Y)

```
Take from Redo Stack
        ↓
Apply again
        ↓
Move back to Undo Stack
```

 Editors store **changes in RAM**

---

# 3. Git Purpose

Git is a **version control system**

- Tracks project history
- Allows rollback to previous versions
- Works on saved files (disk)

---

#  4. Git Workflow

```
WORKING DIRECTORY → STAGING AREA → COMMIT (HISTORY)
```

### Flow

```
Edit file
   ↓
git add
   ↓
Staging Area
   ↓
git commit
   ↓
.git database
```

---

# 5. Git Objects Model

```
Commit → Tree → Blob
```

---

# Blob (File Content)

- Stores ONLY file content

Example:
```
Hello World
```

✔ No filename  
✔ No folder info  

---

# Tree (Structure)

- Stores files + folders mapping

Example:
```
project/
 └── file.txt → Blob
```

---

# Commit (Version Snapshot)

- Points to a Tree
- Represents a full project version

```
Commit
  ↓
Tree
  ↓
Blobs
```

---

# 6. Git Objects Are Immutable

```
Once created → never changed
```

Instead:

- New changes create new objects
- Old objects remain forever

---

# 7. Reuse & Efficiency

### Unchanged file:
```
Reuse existing Blob
```

### Changed file:
```
Create new Blob
```

✔ Saves storage  
✔ Preserves history  

---

# 8. Staging Area Important Concept

```
git add = snapshot taken
```

⚠ If you modify file AFTER git add:

- Commit still uses OLD snapshot

---

# 9. Complete Mental Model

```
Typing
  ↓
RAM
  ↓
Save (Ctrl+S)
  ↓
SSD/HDD
  ↓
git add
  ↓
Staging Area
  ↓
git commit
  ↓
Commit Object
  ↓
Tree
  ↓
Blob
  ↓
Stored in .git
```

---

#  10. Key Takeaways

1. Undo/Redo uses stacks in RAM  
2. Editor changes exist first in RAM  
3. Git tracks only saved files (disk)  
4. git add = staging snapshot  
5. git commit = permanent history  
6. Git uses Blob, Tree, Commit objects  
7. Objects are immutable  
8. New changes = new objects  
9. Unchanged files are reused  
10. `.git` stores full history database  

---

# Multi-Developer Collaboration in Git

## Overview

Git helps multiple developers work on the same project safely.

---

# Should two developers work on the same version?

No.

If both edit the same files:

* Changes can be overwritten
* Work can be lost
* History becomes confusing

Instead, each developer works on their own branch.

---

# Problems Without Git

## ❌ Overwriting Changes

```text
Dev A: Hello A
Dev B: Hello B
```

One change may replace the other.

## ❌ No History

* Hard to see who changed what
* Hard to undo mistakes

## ❌ Lost Work

Changes may be deleted or overwritten.

---

# How Git Helps

## Branches

Each developer gets their own workspace.

```text
Main
 ├── Dev A
 └── Dev B
```

They work independently and later combine changes.

---

# Working Together

1. Create/use a branch
2. Make changes
3. Commit changes
4. Merge into the main project

```bash
git merge
```

---

# Common Risks

## ⚠️ Merge Conflicts

If both change the same line:

```text
Dev A: Hello A
Dev B: Hello B
```

Git asks you to choose or combine the changes.

## ⚠️ Outdated Code

Working on old code can cause bugs when merging.

---

# Benefits of Git

* Safe teamwork
* No accidental overwrites
* Version history
* Easy rollback
* Controlled merging

---

# Summary

* Developers should use separate branches.
* Git helps combine changes safely.
* Main risks are merge conflicts and outdated code.
* Git makes team collaboration easier.

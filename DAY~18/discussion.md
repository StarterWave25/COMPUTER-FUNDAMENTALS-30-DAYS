# Mini File System Challenge

Implement a mini file system in JavaScript.

### Given

```js
const blocks = Array(20).fill(null);
```

* Each block can store **4 characters only**.
* Files can span multiple blocks.

---

### Functions to Implement

```js
createFile(filename, content)
openFile(filename)
deleteFile(filename)
listFiles()
diskUsage()
```

---

### Requirements

#### createFile(filename, content)

* Split content into chunks of 4 characters.
* Find enough free blocks.
* Store chunks in those blocks.
* Save metadata so the file can be reconstructed later.
* If the file already exists, throw an error.
* If there isn't enough space, throw an error.

#### openFile(filename)

* Return the original content by reading the blocks associated with the file.

#### deleteFile(filename)

* Remove the file metadata.
* Mark all occupied blocks as free.

#### listFiles()

* Return all filenames.

#### diskUsage()

Return:

```js
{
  usedBlocks: X,
  freeBlocks: Y
}
```

---

### Example

```js
createFile("report.txt", "HelloWorld");
```

Storage:

```text
Block 0 -> Hell
Block 1 -> oWor
Block 2 -> ld
```

```js
openFile("report.txt");
```

Output:

```text
HelloWorld
```

---

### Bonus (if completed early)

Implement:

```js
renameFile(oldName, newName)
```

without moving the actual file data.
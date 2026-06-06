# Day ~ 5 [GIT]
# Observations - Patnam Prudvinath

### After Reading the Instructions, i went to goggle & gemini and searched for [How git developed internally] and told i want to learn & know about it but not just commands but system design & internal achitecure. After learning Like this for sometime i will try it map it instructions.

### So they suggested me 2 resources 
### 1. Interactive & Visually Learning (Gamified) -> [Learn Git Branching]
### 2. A article -> [Git from the Inside Out] By mary rose.

---

And i started with **"Learning Git Branching"**.

They started with commits, so got a doubt -> **How commit internally works.**

### My  Assumption:
---
I didn't think about it for long time, i didn't get thoughts about it.
### Actual one:
---
So, git consists somehting like **"blob"** which will consist of contents of a single file in hashed version,<br>
[So if we have 1000 files, git will create 1000 blobs for every commit?]<br>
Ans: May be, cause if git found any idetical content in files, then it will use the reference doesn't create a new blob.<br><br>
And, it has a object **"tree"** that represents directory structure & it group blobs & sub-trees.<br><br>
Finally, **"commit"** another object that points to the root tree(means specific reference of that commit) and author, timestap, message along with references to its parent commits. 
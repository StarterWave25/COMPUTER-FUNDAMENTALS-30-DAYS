## Day 5 mission 
1st i created a folder

## investigation 1 why does history matter
i created a file and made changes in it but now i cant get 1st version 
i got only the last version of the file 
![alt text](image.png)
so,You can't get v1 or v2 back. Multiply this across 10,000 files and a team of 10 devs — disaster.
Conclusion: You need a system that remembers every version of every file, forever.

## Investigation 2 — What does Git actually track?
# Goal: See what git init actually creates.
how the git acutaly works or after initializing git repo what happens 
before initilazing this folder did not conatin any thing even hidden folders also 
# Git stores everything inside the .git/ folder. we will get this folder after init commands used.if u Delete that folder = lose all history. That folder IS the repository.
![alt text](image-1.png)

## Investigation 3 — What is a commit?
How hit maitains history how it works
# Goal: Understand what Git remembers when you commit.
When you run git commit, Git does not just record a list of line-by-line changes (diffs); it stores a complete snapshot of your entire project alongside critical context metadata
![alt text](image-2.png)

Did Git save the whole file both times, or just the difference? (Answer: Git saves snapshots, but internally uses diffs. Run git show HEAD to inspect what it stored.)

TO SEE commits what we saved 
![alt text](image-3.png)

## Investigation 4 — Can time move backwards?
Goal: Travel back to an old version.
when we want to go backwards means we need our last version 

1.first get the hash values : $ git log --oneline

a9185e9 (HEAD -> master) updated feature A
ef1f986 add feature A - first version

2.git checkout <first-hash> ~ ef1f986
3.cat feature.txt if u see the content it is now first version
![alt text](image-4.png)
# Also comparing:
![alt text](image-5.png)

Git doesn't actually "move in time" — it just swaps which snapshot your files reflect. Your history is always safe.

## Investigation 5 — Why do branches exist?
# Goal: Simulate two developers working in parallel.

one user in main branch and developing the app
and made commit 

another user also developing app in a seperate branch 
and commited 

![alt text](image-6.png)

the changes may not applieed until u merge them 
Admin@JACK-SCREEN MINGW64 /d/jack/CF-30/git-day5-mission/git-repo (new-feature)
$ git checkout master
Switched to branch 'master'

Admin@JACK-SCREEN MINGW64 /d/jack/CF-30/git-day5-mission/git-repo (master)
$ cat app.txt
main app - stable


## Investigation 6 — What happens during a merge?
# Goal: Bring branch work back into main.

# You're on main — merge the feature branch in
git merge new-feature

merge the branch using command
![alt text](image-7.png)


## Create two branches that change the SAME line
![alt text](image-8.png)

# Create two branches that change the SAME line
git checkout -b branch-a
echo "Line changed by A" > conflict.txt
git add conflict.txt && git commit -m "Branch A changes"

git checkout main
echo "Line changed by MAIN" > conflict.txt
git add conflict.txt && git commit -m "Main changes same line"

git merge branch-a   # CONFLICT!
cat conflict.txt     # See the conflict markers <<<< ==== >>>>
![alt text](image-9.png)

## Investigation 7 — Break Git (learn by recovery)

means if u develop in a out dated version it is also remembered by git it is main thing here 

# Create multiple commits, then detach HEAD
git log --oneline
git checkout HEAD~2   # Detached HEAD state — you're "floating"
# Make a commit here — it'll be orphaned
echo "orphan work" > orphan.txt
git add orphan.txt && git commit -m "Orphan commit"

# Recover: git checkout main brings you back
git checkout main
# The orphan commit still exists in reflog:
git reflog   # Git never truly forgets anything

![alt text](image-10.png)

## Investigation 8 — What problem does each concept solve?
(don't look it up — answer from memory after the experiments):
ConceptProblem it solves
Repository Where does Git store the full history?
CommitHow do we save a snapshot in time?
BranchHow do two people work without breaking each other?
MergeHow do separate workstreams come back together?
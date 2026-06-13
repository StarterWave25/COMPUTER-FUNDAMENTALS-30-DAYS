Problem: Collaborative Whiteboard Autosave

Your team is building a simple online whiteboard.

Requirements:

Users can continuously draw on the canvas.
Every 5 seconds, the current whiteboard state must be automatically saved to disk.
A user should never experience lag while drawing.
Saving to disk may sometimes take 2-3 seconds.
Only one whiteboard document exists.
Question

Design the application architecture.

Specifically discuss:

How many threads should exist?
What responsibility does each thread have?
How will drawing and saving interact?
What shared resources exist?
What problems can occur if multiple threads access the shared resources simultaneously?
Would a single-threaded design satisfy all requirements?

Do not write code.

Draw the process, threads, and shared memory structure and justify your design choices.
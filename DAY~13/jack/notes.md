## PART 0: Understanding Threading (The Foundation)
# Process = A restaurant branch (separate building, separate resources)
Thread = A worker in the same restaurant (same kitchen, shared ingredients)

orders = []  # Shared resource
# Thread 1: Add order "Biryani"
orders.append("Biryani")  # Takes 3 steps internally
# Thread 2: Add order "Dosa" (WHILE Thread 1 is still adding!)
orders.append("Dosa")  
# Result: Sometimes orders disappear or get corrupted!
Why? Because .append() is NOT atomic (doesn't happen all at once). While Thread 1 is adding, Thread 2 jumps in and corrupts the data.
## Solution: Use a Lock (like a door lock) — only one thread can access the shared resource at a time.
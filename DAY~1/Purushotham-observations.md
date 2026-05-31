Part 1: Task Manager Observations:-

System Information:-

1.What are your CPU, RAM, and Storage specifications?
A:- Intel core i5 12500H, 16GB ddr4 ram, 512GB NVME gen4 ssd.

2.How much RAM is available when the computer is idle?
A:- 8.4 GB.

How many background processes are running?
A:- 116.

Chrome, VS Code, Whatsapp Analysis:-

Which application used the most RAM?
A:- Whatsapp (at 625.4MB).

Which application used the most CPU?
A:- Whatsapp and VS Code (at their max : 3-4% when using.)

Which application launched the fastest?
A:- VS Code

Which application consumed the most power?
A:- VS Code and whatsapp.

Did any application create multiple processes?
A:- All created Multiple processes :
VS Code : 12 processes
Chrome : 13 processes
Whatsapp : 9 Processes

Why does Chrome show multiple processes instead of one?
A:- Chrome uses multi-process architecture, i.e., it runs each application in it's dedicated CPU process.

What happened to RAM usage after closing an application?
A:- The RAM usage decreased because that application has been removed from the RAM.

Experiment Questions:-

What happens when you open 10 more Chrome tabs?
A:- Chrome's RAM usage has spiked up! and no.of chrome's processes has increased.

Does minimizing an application reduce RAM usage?
A:- No, it doesn't reduce RAM usage.

Which application remained active even after closing its window?
A:- Whatsapp remained as a active background process even after closing its window.

What did you learn from Task Manager that you didn't know before?
A:- That i can actively monitor Usage of cpu, gpu, ram, etc and list and even kill the processes.

Part 2: Chrome Tabs & Infinite Loop Experiment:-

Before Experiment:-

Initial RAM usage of Chrome?
A:- 450.5 MB.
Initial CPU usage of Chrome?
A:- Under 1%.

After Opening 20 Tabs:-

How much did RAM increase?
A:- It has increased up to 2.9GB.

Did CPU usage increase significantly?
A:- Increased up to 3% at some times and averagely 0.1-1.5%.

Which tab consumed the most memory?
A:- Google docs, up to 300MB.

Infinite Loop Experiment:-

Run in Chrome Console:

while(true){console.log("HI");}

What happened to CPU usage?
A:- CPU usage spiked up to 26-34%.

Did the browser become unresponsive?
A:- Yes, somewhat!

Did the fan speed increase?
A:- Yes after reaching a sustained CPU usage of 30% on average and RAM usage of 8-9GB.

What happened to other applications?
A:- Other applications memory usage is decreasing.

Why does an infinite loop consume CPU continuously?
A:- Yes continuously above 24-32% on average.

After Closing Tabs
Did RAM usage immediately decrease?
A:- Yes, immediately decreased from the peak of 9GB to 364.9MB.

Did CPU usage return to normal?
A:- Yes, from peak 34% to 0-1%.

Why doesn't RAM always return exactly to the previous value?
A:- Because applications maintain cache.

Part 3: CPU Deep Understanding
What is a CPU?
What does CPU stand for?
What are CPU cores?
What is a thread?
Why do modern CPUs have multiple cores?
What happens when CPU usage reaches 100%?
Why does a game need more CPU power than a text editor?
What is clock speed (GHz)?
Why is CPU called the "brain" of the computer?
What tasks are CPU-intensive?
Part 4: RAM Deep Understanding
What is RAM?
What does RAM stand for?
Why is RAM called temporary memory?
What happens to RAM data after shutdown?
Why do applications need RAM?
What happens when RAM becomes full?
What is memory allocation?
Why does Chrome consume a lot of RAM?
How is RAM different from Storage?
What tasks are RAM-intensive?
Part 5: Storage Deep Understanding
What is storage?
Difference between SSD and HDD?
Why is SSD faster than HDD?
Where are files stored permanently?
What happens when you save a file?
Why does storage keep data after shutdown?
What is read speed?
What is write speed?
How does storage affect application startup time?
Part 6: Operating System Deep Understanding
What is an Operating System?
Why is Windows/Linux/macOS called an OS?
What happens when a program is opened?
How does the OS manage RAM?
How does the OS manage CPU scheduling?
What is a process?
What is a thread?
What would happen if there was no OS?
Why can't two programs directly control hardware?
Part 7: Real Engineer Thinking Questions
Why does a computer slow down when many applications are open?
Why does adding more RAM improve performance?
Why can a fast CPU still feel slow with an HDD?
Why do browsers consume more resources than Notepad?
If RAM is temporary, why don't applications constantly read from storage?
What bottleneck did you observe in your machine: CPU, RAM, or Storage?
If you had ₹10,000 to upgrade your PC, would you choose CPU, RAM, or SSD? Why?
Which experiment surprised you the most?
Explain CPU, RAM, Storage, and OS to a 10-year-old child.

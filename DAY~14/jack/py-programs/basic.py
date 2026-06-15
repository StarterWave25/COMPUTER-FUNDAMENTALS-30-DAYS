#!/usr/bin/env python3
"""
BASIC CPU SCHEDULER - Round Robin Implementation
Educational code showing how operating systems schedule processes

This demonstrates:
1. Process queue management
2. Fair time allocation (Round Robin)
3. Context switching
4. Performance metrics
"""

from collections import deque
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Process:
    """Represents a process (program) in the system"""
    pid: int                  # Process ID
    arrival_time: int        # When process arrives (ms)
    burst_time: int          # Total CPU time needed (ms)
    remaining_time: int = None  # Time still needed
    
    def __post_init__(self):
        if self.remaining_time is None:
            self.remaining_time = self.burst_time


class RoundRobinScheduler:
    """
    Round Robin CPU Scheduler
    
    Algorithm:
    1. Each process gets a fixed time slice (time_quantum)
    2. If process doesn't finish, goes to back of queue
    3. Next process gets a turn
    4. Fair allocation!
    
    Time Complexity: O(n) where n = number of processes
    Space Complexity: O(n) for queue
    """
    
    def __init__(self, time_quantum: int = 5):
        self.time_quantum = time_quantum
        self.ready_queue = deque()
        self.completed = []
        self.current_time = 0
        self.context_switches = 0
    
    def add_process(self, process: Process):
        """Add process to ready queue"""
        self.ready_queue.append(process)
        print(f"[{self.current_time:3d}ms] ➕ Process P{process.pid} arrives (needs {process.burst_time}ms)")
    
    def schedule(self, processes: List[Process]):
        """
        Main scheduling loop
        
        Steps:
        1. Pick next process from queue
        2. Execute for time quantum
        3. Check if done
        4. If not, go back to queue
        """
        # Sort by arrival time
        processes.sort(key=lambda p: p.arrival_time)
        
        # Add processes as they arrive
        process_idx = 0
        self.ready_queue.append(processes[0])
        process_idx = 1
        
        print(f"\n{'='*70}")
        print(f"🖥️  ROUND ROBIN CPU SCHEDULER")
        print(f"Time Quantum: {self.time_quantum}ms")
        print(f"{'='*70}\n")
        
        print(f"Process P{processes[0].pid} arrives at {processes[0].arrival_time}ms\n")
        
        while self.ready_queue:
            # Add any processes that have arrived
            while (process_idx < len(processes) and 
                   processes[process_idx].arrival_time <= self.current_time):
                self.ready_queue.append(processes[process_idx])
                print(f"[{self.current_time:3d}ms] ➕ Process P{processes[process_idx].pid} arrives")
                process_idx += 1
            
            # Pick next process
            current_process = self.ready_queue.popleft()
            self.context_switches += 1
            
            # Allocate time (can't exceed quantum or remaining time)
            execution_time = min(self.time_quantum, current_process.remaining_time)
            
            print(f"[{self.current_time:3d}ms] ▶️  EXECUTE P{current_process.pid} "
                  f"({execution_time}ms) | Remaining: {current_process.remaining_time - execution_time}ms")
            
            # Execute process
            self.current_time += execution_time
            current_process.remaining_time -= execution_time
            
            # Check if process completed
            if current_process.remaining_time == 0:
                print(f"[{self.current_time:3d}ms] ✅ COMPLETED P{current_process.pid}\n")
                self.completed.append({
                    'pid': current_process.pid,
                    'completion_time': self.current_time,
                    'arrival_time': current_process.arrival_time,
                    'burst_time': current_process.burst_time
                })
            else:
                # Process still needs time, back to queue
                print(f"[{self.current_time:3d}ms] ⏸️  PAUSED P{current_process.pid}, back to queue\n")
                self.ready_queue.append(current_process)
    
    def print_statistics(self):
        """Calculate and display scheduling statistics"""
        print(f"\n{'='*70}")
        print(f"📊 SCHEDULING STATISTICS")
        print(f"{'='*70}\n")
        
        if not self.completed:
            print("No processes completed!")
            return
        
        # Calculate metrics
        turnaround_times = []
        wait_times = []
        
        for p in self.completed:
            turnaround = p['completion_time'] - p['arrival_time']
            wait = turnaround - p['burst_time']
            turnaround_times.append(turnaround)
            wait_times.append(wait)
        
        avg_turnaround = sum(turnaround_times) / len(turnaround_times)
        avg_wait = sum(wait_times) / len(wait_times)
        
        print(f"Total Time (Makespan): {self.current_time}ms")
        print(f"Processes Completed: {len(self.completed)}")
        print(f"Context Switches: {self.context_switches}")
        
        print(f"\n📈 AVERAGES:")
        print(f"   Average Turnaround Time: {avg_turnaround:.1f}ms")
        print(f"   Average Wait Time: {avg_wait:.1f}ms")
        print(f"   (Lower is better!)\n")
        
        print(f"📋 DETAILS:")
        print(f"   {'PID':<5} {'Arrival':<8} {'Burst':<8} {'Complete':<10} {'Turnaround':<12} {'Wait':<8}")
        print(f"   {'-'*60}")
        
        for i, p in enumerate(self.completed):
            turnaround = turnaround_times[i]
            wait = wait_times[i]
            print(f"   P{p['pid']:<4} {p['arrival_time']:<8} {p['burst_time']:<8} "
                  f"{p['completion_time']:<10} {turnaround:<12} {wait:<8}")


# ============ DEMONSTRATION ============

def example_1_simple():
    """Simple example: All processes arrive together"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Simple Case (All arrive together)")
    print("="*70)
    
    scheduler = RoundRobinScheduler(time_quantum=5)
    
    processes = [
        Process(pid=1, arrival_time=0, burst_time=12),
        Process(pid=2, arrival_time=0, burst_time=8),
        Process(pid=3, arrival_time=0, burst_time=6),
        Process(pid=4, arrival_time=0, burst_time=10),
    ]
    
    scheduler.schedule(processes)
    scheduler.print_statistics()


def example_2_staggered():
    """Example: Processes arrive at different times"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Staggered Arrivals")
    print("="*70)
    
    scheduler = RoundRobinScheduler(time_quantum=5)
    
    processes = [
        Process(pid=1, arrival_time=0, burst_time=12),
        Process(pid=2, arrival_time=2, burst_time=8),
        Process(pid=3, arrival_time=4, burst_time=6),
        Process(pid=4, arrival_time=6, burst_time=10),
    ]
    
    scheduler.schedule(processes)
    scheduler.print_statistics()


def example_3_compare_quantum():
    """Compare different time quantum values"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Comparing Different Time Quantum Values")
    print("="*70)
    
    processes = [
        Process(pid=1, arrival_time=0, burst_time=10),
        Process(pid=2, arrival_time=1, burst_time=10),
        Process(pid=3, arrival_time=2, burst_time=10),
    ]
    
    for quantum in [2, 5, 10]:
        print(f"\n🔍 Testing with time_quantum = {quantum}ms")
        print("-" * 50)
        
        scheduler = RoundRobinScheduler(time_quantum=quantum)
        scheduler.schedule(processes)
        
        turnaround_times = [
            p['completion_time'] - p['arrival_time'] 
            for p in scheduler.completed
        ]
        avg_turnaround = sum(turnaround_times) / len(turnaround_times)
        
        print(f"Result: Avg Turnaround = {avg_turnaround:.1f}ms, "
              f"Context Switches = {scheduler.context_switches}")


# ============ MAIN ============

if __name__ == "__main__":
    print("\n" + "🎓 ROUND ROBIN CPU SCHEDULER - EDUCATIONAL DEMONSTRATION" + "\n")
    
    # Run examples
    example_1_simple()
    example_2_staggered()
    example_3_compare_quantum()
    
    # Key insights
    print("\n" + "="*70)
    print("🎯 KEY INSIGHTS")
    print("="*70)
    print("""
1. ROUND ROBIN FAIRNESS:
   Each process gets equal CPU time (time quantum)
   No process can monopolize the CPU
   
2. TIME QUANTUM TRADE-OFF:
   Small quantum (2ms):
   ✓ Very fair, responsive
   ✗ Lots of context switches (overhead)
   
   Large quantum (20ms):
   ✓ Few context switches (efficient)
   ✗ Less fair, poor responsiveness
   
   Typical: 5-20ms for general purpose OS
   
3. STAGGERED ARRIVALS:
   Scheduler handles processes arriving at different times
   New arrivals join queue and wait their turn
   
4. CONTEXT SWITCH COST:
   Every switch has overhead (save/restore state)
   Too many switches = CPU time wasted
   Too few = Poor responsiveness
   
NEXT: Add priority scheduling to improve fairness!
""")
    print("="*70 + "\n")
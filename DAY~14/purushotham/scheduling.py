from collections import deque
import time

time_slice = 2
context_switch_cost = 0.1
stats = {
    "cpu_busy_time": 0,
    "total_time": 0,
    "context_switch_count": 0,
    "context_cost_total": 0,
}

processes = [
    {
        "pid": 1,
        "name": "Chrome",
        "remaining_time": 5,
        "state": "READY",
        "waiting_time": 0,
        "arrival_time": time.time(),
        "completion_time": None,
        "first_run_time": None,
        "registers": {"IP": 0, "SP": 1000, "ACC": 0},
    },
    {
        "pid": 2,
        "name": "Music",
        "remaining_time": 3,
        "state": "READY",
        "waiting_time": 0,
        "arrival_time": time.time(),
        "completion_time": None,
        "first_run_time": None,
        "registers": {"IP": 0, "SP": 2000, "ACC": 0},
    },
    {
        "pid": 3,
        "name": "TS Compiler",
        "remaining_time": 8,
        "state": "READY",
        "waiting_time": 0,
        "arrival_time": time.time(),
        "completion_time": None,
        "first_run_time": None,
        "registers": {"IP": 0, "SP": 3000, "ACC": 0},
    },
]

ready_queue = deque()

for process in processes:
    ready_queue.append(process)


def update_waiting_time(queue, time_slice):
    for process in queue:
        process["waiting_time"] += time_slice


def save_state(process):
    print("\nSaving state: ", process["name"])
    process["registers"]["IP"] += 10
    process["registers"]["ACC"] += 1


def restore_state(process):
    print("\nRestoring state: ", process["name"])
    print("\n", process["registers"])


def context_switch(old, new):
    # print("Switching from ", old["name"], " to ", new["name"])
    print("\n === Context Switch ===")
    if old:
        save_state(old)
    stats["context_switch_count"] += 1
    time.sleep(context_switch_cost)
    restore_state(new)
    print("============================")


def execute(process, time_slice):
    if process["remaining_time"] < 0:
        return
    process["state"] = "RUNNING"
    if process["first_run_time"] is None:
        process["first_run_time"] = time.time()
    print("\nRunning", process["name"])
    actual_time = min(process["remaining_time"], time_slice)
    time.sleep(actual_time)
    process["remaining_time"] -= actual_time
    stats["cpu_busy_time"] += actual_time
    if process["remaining_time"] > 0:
        process["state"] = "READY"


def round_robin(queue, time_slice):
    if not queue:
        print("No processes")
        return
    previous_process = None
    while queue:
        process = queue.popleft()
        if previous_process and previous_process != process:
            context_switch(previous_process, process)
        update_waiting_time(queue, time_slice)
        execute(process, time_slice)
        if process["remaining_time"] > 0:
            previous_process = process
        else:
            previous_process = None

        if process["remaining_time"] > 0:
            queue.append(process)
        else:
            process["state"] = "TERMINATED"
            process["completion_time"] = time.time()
            print("\nTerminated", process["name"])


start_time = time.time()
round_robin(ready_queue, time_slice)
end_time = time.time()

stats["total_time"] = end_time - start_time
utilization = (stats["cpu_busy_time"] / stats["total_time"]) * 100

print("\n========== CPU STATISTICS ==========")
print("CPU Busy Time:", stats["cpu_busy_time"])
print("Total System Time:", stats["total_time"])
print("CPU Utilization:", utilization, "%")
print("Context Switches:", stats["context_switch_count"])

for process in processes:
    response_time = process["first_run_time"] - process["arrival_time"]
    turnaround_time = process["completion_time"] - process["arrival_time"]
    print("\nProcess:", process["name"])
    print("Waiting Time:", process["waiting_time"])
    print("Response Time:", response_time)
    print("Turnaround Time:", turnaround_time)


# def execute(process):
#     if process["remaining_time"] < 0:
#         return
#     process["state"] = "RUNNING"
#     print("Running", process["name"])
#     time.sleep(process["remaining_time"])
#     process["state"] = "TERMINATED"
#     print("Terminated", process["name"])


# def fcfs(queue):
#     if not queue:
#         print("No processes")
#     while queue:
#         process = queue.popleft()
#         execute(process)


# fcfs(ready_queue)

import os, time

os.system('cls')

processes = [
  {"process": "chrome", "brust": 5}, 
  {"process": "vs-code", "brust": 3}, 
  {"process": "spotify", "brust": 3}
]


def CPU(process):
  current_process_brust = 0
  
  index = -1
  for i in range(len(processes)):
    c_process = processes[i]["process"]
    brust = processes[i]["brust"]
    if(c_process == process):
      current_process_brust = brust
      index = i
      break
    
  if(current_process_brust < 2):
    print(f"Running '{process}' for 1 second.")
    time.sleep(1)
    processes.pop(index)
    print(f"'{process}' Execution completed & Removed.")
    return 0
  else:
    print(f"Running {process} for 2 second.")
    time.sleep(2)
    current_process_brust -= 2
    processes[i]["brust"] = processes[i]["brust"] - 2
    if(current_process_brust == 0):
      processes.pop(index)
      print(f"'{process}' Execution completed & Removed.")
      return 0
    print(f"'{process}' Executed for 2 seconds, And it will continued Again.")
  return 1

while(processes):
  for i in range(len(processes)):
    val = CPU(processes[i]["process"])
    if val == 0:
      break
  
print("Program Execution Completed!")
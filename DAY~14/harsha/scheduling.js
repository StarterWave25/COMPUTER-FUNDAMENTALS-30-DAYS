const processes = [
    {
        pid: 1,
        name: 'Chrome',
        priority: 3,
        burst: 5
    },
    {
        pid: 2,
        name: 'WhatsApp',
        priority: 1,
        burst: 7
    },
    {
        pid: 3,
        name: 'VS Code',
        priority: 4,
        burst: 3
    },
    {
        pid: 4,
        name: 'CMD',
        priority: 2,
        burst: 4
    }
];

const noOfProcesses = processes.length;

// Rechanging the order of processes in the queue to execute according to priority
processes.sort((p1, p2) => p1.priority - p2.priority);

// Executing the processes
console.log('\n===== Processes are executing =====');
for (let i = 0; i < noOfProcesses; i++) {
    console.log(processes.shift());
}
console.log('===== Processes executing completed =====\n');

// No processes left
console.log('No Processes left: ');
console.log(processes);
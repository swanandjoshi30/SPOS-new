def fcfs(processes):
    # Initialize total waiting time and total turnaround time for calculating averages
    total_waiting = 0
    total_turnaround = 0
    # Initialize waiting time for the first process
    waiting_time = 0

    # Loop through each process in the order they are received (FCFS)
    for i in range(len(processes)):
        # Extract the process name and burst time for each process
        process_name, burst_time = processes[i]

        # The first process has no waiting time (starts execution immediately)
        if i == 0:
            waiting_time = 0
        else:
            # For subsequent processes, waiting time accumulates the burst time of the previous process
            waiting_time += processes[i - 1][1]

        # Turnaround time for each process is waiting time + its own burst time
        turnaround_time = waiting_time + burst_time

        # Add the waiting and turnaround times of this process to the totals
        total_waiting += waiting_time
        total_turnaround += turnaround_time

        # Print waiting time and turnaround time for the current process
        print(f"Process {process_name}: Waiting Time = {waiting_time}, Turnaround Time = {turnaround_time}")

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = total_waiting / len(processes)
    avg_turnaround_time = total_turnaround / len(processes)

    # Print the average waiting time and average turnaround time
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example list of processes with (Process Name, Burst Time)
processes = [('p1', 10), ('p2', 5), ('p3', 5)]

# Run the FCFS scheduling function on the example processes
fcfs(processes)

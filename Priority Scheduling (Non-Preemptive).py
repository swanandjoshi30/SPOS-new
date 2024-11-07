def priority_scheduling():
    # Get the number of processes from the user
    n = int(input("Enter the number of processes: "))

    # Initialize a list to hold each process as a tuple (name, priority, burst_time)
    processes = []
    for i in range(n):
        process_name = f"P{i + 1}"  # Auto-generate process names (P1, P2, ...)
        burst_time = int(input(f"Enter burst time for {process_name}: "))
        priority = int(input(f"Enter priority for {process_name} (lower number = higher priority): "))
        processes.append((process_name, priority, burst_time))

    # Sort by priority (the lower the number, the higher the priority)
    processes.sort(key=lambda x: x[1])

    # Initialize total waiting and turnaround time
    total_waiting_time = 0
    total_turnaround_time = 0
    waiting_time = 0

    print("\nPriority (Non-Preemptive) Scheduling:")

    # Scheduling and calculating waiting and turnaround times
    for i in range(len(processes)):
        process_name, priority, burst_time = processes[i]

        if i == 0:
            waiting_time = 0
        else:
            waiting_time += processes[i - 1][2]  # Add previous process's burst time

        turnaround_time = waiting_time + burst_time

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print(f"Process {process_name}: Waiting Time = {waiting_time}, Turnaround Time = {turnaround_time}")

    # Calculate averages
    avg_waiting = total_waiting_time / len(processes)
    avg_turnaround = total_turnaround_time / len(processes)

    print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround:.2f}")

# Run the function to take input from the user
priority_scheduling()

def round_robin(processes, time_quantum):
    remaining_time = [burst_time for _, burst_time in processes]
    current_time = 0
    waiting_time = [0] * len(processes)
    execution_order = []  # To track the Gantt chart execution order

    print("Round Robin (Preemptive) Scheduling:")

    while True:
        done = True

        for i in range(len(processes)):
            if remaining_time[i] > 0:
                done = False  # There are still processes to execute

                if remaining_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_time[i] -= time_quantum
                    execution_order.append((processes[i][0], time_quantum))  # Record this execution slice
                else:
                    # Process completes in this time slice
                    current_time += remaining_time[i]
                    execution_order.append((processes[i][0], remaining_time[i]))  # Record remaining time slice
                    waiting_time[i] = current_time - processes[i][1]
                    remaining_time[i] = 0

        if done:
            break  # All processes are complete

    # Calculate average waiting time
    avg_waiting_time = sum(waiting_time) / len(processes)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

    # Print Gantt Chart
    print("\nGantt Chart:")
    for process, duration in execution_order:
        print(f"| {process} ", end="")
    print("|")

    time_marker = 0
    for _, duration in execution_order:
        print(f"{time_marker:<5}", end="")
        time_marker += duration
    print(f"{time_marker}")

# Sample processes (name, burst_time)
processes = [("P1", 10), ("P2", 5), ("P3", 8)]
time_quantum = 4
round_robin(processes, time_quantum)

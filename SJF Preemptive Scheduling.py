# SJF Preemptive Scheduling
def sjf_preemptive(processes):
    n = len(processes)
    remaining_time = [burst_time for _, burst_time in processes]  # Copy burst times
    waiting_time = [0] * n
    current_time = 0
    completed = 0

    print("SJF (Preemptive) Scheduling:")
    
    while completed < n:
        # Find the process with the shortest remaining time
        min_time = float('inf')
        shortest = -1

        for i in range(n):
            if remaining_time[i] > 0 and remaining_time[i] < min_time:
                min_time = remaining_time[i]
                shortest = i

        # If no process is ready, increase the current time
        if shortest == -1:
            current_time += 1
            continue

        # Process the shortest job
        remaining_time[shortest] -= 1
        current_time += 1

        # If the process is finished
        if remaining_time[shortest] == 0:
            completed += 1
            finish_time = current_time
            waiting_time[shortest] = finish_time - processes[shortest][1]
    
    # Calculate average waiting time
    total_waiting_time = sum(waiting_time)
    avg_waiting_time = total_waiting_time / n

    # Display results
    for i in range(n):
        process_name, burst_time = processes[i]
        print(f"Process {process_name}: Waiting Time = {waiting_time[i]}")

    print(f"Average Waiting Time: {avg_waiting_time}")


# Sample processes (name, burst_time)
processes = [("P1", 8), ("P2", 4), ("P3", 9), ("P4", 5)]
sjf_preemptive(processes)

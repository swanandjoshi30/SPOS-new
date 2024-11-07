def best_fit(memory_blocks, processes):
    print("\nBest Fit Allocation:")
    for process in processes:
        best_index = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= process:
                if best_index == -1 or memory_blocks[i] < memory_blocks[best_index]:
                    best_index = i
        if best_index != -1:
            print(f"Process {process}KB allocated to block of {memory_blocks[best_index]}KB")
            memory_blocks[best_index] -= process
        else:
            print(f"Process {process}KB could not be allocated")

memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
best_fit(memory_blocks.copy(), processes)

def worst_fit(memory_blocks, processes):
    print("\nWorst Fit Allocation:\n" + "=" * 30)
    for process in processes:
        allocated = False
        # Find the index of the largest memory block that can fit the process
        max_index = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= process:
                if max_index == -1 or memory_blocks[i] > memory_blocks[max_index]:
                    max_index = i

        if max_index != -1:
            print(f"Process {process}KB allocated to block of {memory_blocks[max_index]}KB")
            memory_blocks[max_index] -= process
            allocated = True
        if not allocated:
            print(f"Process {process}KB could not be allocated")

    print("\nUpdated Memory Blocks:", memory_blocks)


memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
worst_fit(memory_blocks.copy(), processes)

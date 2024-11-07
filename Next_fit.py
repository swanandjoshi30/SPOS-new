def next_fit(memory_blocks, processes):
    print("\nNext Fit Allocation:")
    last_allocated_index = 0
    for process in processes:
        allocated = False
        n = len(memory_blocks)
        for i in range(n):
            index = (last_allocated_index + i) % n
            if memory_blocks[index] >= process:
                print(f"Process {process}KB allocated to block of {memory_blocks[index]}KB")
                memory_blocks[index] -= process
                last_allocated_index = index
                allocated = True
                break
        if not allocated:
            print(f"Process {process}KB could not be allocated")


# Example usage
memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
next_fit(memory_blocks.copy(), processes)

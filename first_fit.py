def first_fit(memory_blocks, processes):
    print("\nFirst Fit Allocation:")
    for process in processes:
        allocated = False
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= process:
                print(f"Process {process}KB allocated to block of {memory_blocks[i]}KB")
                memory_blocks[i] -= process
                allocated = True
                break
        if not allocated:
            print(f"Process {process}KB could not be allocated")


memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
first_fit(memory_blocks.copy(), processes)
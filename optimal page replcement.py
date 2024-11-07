def optimal_page_replacement(pages, frame_size):
    # Initialize frames and counters
    frames = []
    page_faults = 0

    for i in range(len(pages)):
        # Check if the page is already in frame
        if pages[i] not in frames:
            # If frames have space, simply add the page
            if len(frames) < frame_size:
                frames.append(pages[i])
            else:
                # Find the page that will not be used for the longest period of time
                farthest = i + 1
                page_to_remove = -1
                for frame in frames:
                    if frame not in pages[i + 1:]:
                        page_to_remove = frame
                        break
                    else:
                        # Find the farthest usage of the page in future
                        index = pages[i + 1:].index(frame) + (i + 1)
                        if index > farthest:
                            farthest = index
                            page_to_remove = frame
                # Replace the page
                frames[frames.index(page_to_remove)] = pages[i]

            # Increment page faults counter
            page_faults += 1

        # Print the current status of frames
        print(f"Step {i + 1}: Page {pages[i]} -> Frames: {frames}")

    print("\nTotal Page Faults:", page_faults)


# Test with a sample page reference string and frame size
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3
optimal_page_replacement(pages, frame_size)

import time
import matplotlib.pyplot as plt


# Function to analyze pop time for larger indices
def analyze_pop():
    list_lengths = [1000, 10000, 100000, 1000000, 10000000]  # Various list sizes
    indices = [0, 10, 100, 1000, 10000, -1]  # Larger indices to test (including -1 for last element)
    results = []

    for length in list_lengths:
        for index in indices:
            if index >= length:  # Skip if the index is out of range
                continue
            # Create a list of the given size
            lst = list(range(length))

            # Measure the time to pop an element at the given index
            start = time.time()
            lst.pop(index)
            end = time.time()

            # Record the results
            results.append((length, index, end - start))

    return results


# Perform the analysis
results = analyze_pop()

# Organize results for plotting
list_lengths = sorted(set(r[0] for r in results))
indices = sorted(set(r[1] for r in results if r[1] < max(list_lengths)))  # Ensure valid indices

# Visualization of the results
plt.figure(figsize=(10, 6))
for index in indices:
    times = [r[2] for r in results if r[1] == index]
    lengths = [r[0] for r in results if r[1] == index]
    plt.plot(lengths, times, label=f'Index {index}', marker='o')

plt.xlabel('List Length')
plt.ylabel('Time (s)')
plt.title('Time to pop element from list at larger indices')
plt.legend()
plt.grid()
plt.show()


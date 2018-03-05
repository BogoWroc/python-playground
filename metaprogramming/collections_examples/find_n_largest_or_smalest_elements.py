import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Display [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Display [-4, 1, 2]

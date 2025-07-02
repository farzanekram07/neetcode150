# quicksort output TLE
# work some extent with random pivot

# merge sort work but extra memory usage


# counting sort outperform - time O(n + k)|space O(n + k)
def sortArray(arr):
    min_number = min(arr)
    max_number = max(arr)

    range_of_elements = (max_number - min_number) + 1
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_number] += 1

    sorted_list = []
    for num, freq in enumerate(count):
        sorted_list.extend([num + min_number] * count[num])
    return sorted_list


nums = [5,1,1,2,0,0]
print(sortArray(nums))

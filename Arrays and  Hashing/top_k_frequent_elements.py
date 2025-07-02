from typing import List
from collections import Counter

# solution 1
def topKFrequent1(arr: List[int], k: int) -> List[int]:
        min_value = min(arr)
        max_value = max(arr)

        range_of_element = (max_value - min_value) + 1
        count = [0] * range_of_element

        for num in arr:
            count[num - min_value] += 1

        freq_num_pairs = []
        for idx, freq in enumerate(count):
            num = idx + min_value
            freq_num_pairs.append((freq, num))

        freq_num_pairs.sort(reverse=True)  # highest frequency first
        result = [num for freq, num in freq_num_pairs[:k]]
        return result

# solution 2
def topKFrequent2(arr: List[int], k: int) -> List[int]:
        count = Counter(arr)
        return [item for item, freq in count.most_common(k)]

nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent1(nums, k))
print(topKFrequent2(nums, k))


# this code return return all elements with frequency >= k
'''def topKFrequent(arr, k):
    min_value = min(arr)
    max_value = max(arr)

    range_of_element = (max_value - min_value) + 2
    count = [0] * range_of_element

    for num in arr:
        count[num] += 1

    k_freq_element = []
    for num, freq in enumerate(count):
        if freq >= k:
            k_freq_element.append(num)
    return k_freq_element

nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums, k))'''
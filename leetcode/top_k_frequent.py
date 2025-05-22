from typing import List, Dict
import unittest

"""
LeetCode Problem: Top K Frequent Elements
Difficulty: Medium
Category: Array, Hash Table, Sorting, Heap (Priority Queue), Bucket Sort
Companies: Amazon, Microsoft, Bloomberg, Apple, Google

Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

"""
# 1,1,1,3,3,5,5
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if len(nums) == 1:
        return nums
    freq:List[int, List[int]] = [[] for i in range(len(nums)+1)]
    counts = {}
    
    for num in nums:
        counts[num] = 1 +  counts.get(num,0)
    for val, count in counts.items():
        freq[count].append(val)
    
    res: List[int] = []
    
    for i in range(len(freq)-1,0,-1):
        while len(freq[i])>0:
            res.append(freq[i].pop())
            if len(res) == k:
                return res
    
    return []

class TestTopKFrequent(unittest.TestCase):
    def test_example1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        expected = [1,2]
        result = topKFrequent(nums, k)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example7(self):
        nums = [1,1,1,1,1]
        k = 1
        expected = [1]
        result = topKFrequent(nums, k)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example2(self):
        nums = [1]
        k = 1
        expected = [1]
        result = topKFrequent(nums, k)
        self.assertEqual(sorted(result), sorted(expected))

    def test_multiple_frequencies(self):
        nums = [1,1,1,2,2,2,3,3,4]
        k = 2
        expected = [1,2]
        result = topKFrequent(nums, k)
        self.assertEqual(sorted(result), sorted(expected))

    def test_all_same_frequency(self):
        nums = [1,2,3,4]
        k = 2
        expected = [1,2]  # Any two numbers are valid since all have same frequency
        result = topKFrequent(nums, k)
        self.assertEqual(len(result), k)

if __name__ == '__main__':
    unittest.main() 
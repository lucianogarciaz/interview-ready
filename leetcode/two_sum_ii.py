from typing import List
import unittest

def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    
    Args:
        numbers: A 1-indexed array of integers sorted in non-decreasing order
        target: The target sum to find
        
    Returns:
        A list of two integers [index1, index2] where 1 <= index1 < index2 <= numbers.length
    """
    l = 0
    n = numbers
    r = len(n)-1
    while l<r:
        cSum = n[l]+n[r]
        if cSum == target:
            return [l+1, r+1]
        if cSum>target:
            r-=1
        if cSum<target:
            l+=1
    
    return []


def twoSumHash(numbers: List[int], target: int) -> List[int]:
    hash = {target-v:i+1 for i,v in enumerate(numbers)}

    for i in range(len(numbers)):
        if numbers[i] in hash:
            return [i+1, hash[numbers[i]]]
    
    return []
    


class TestTwoSumII(unittest.TestCase):
    def test_example1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]  # numbers[0] + numbers[1] = 2 + 7 = 9
        result = twoSum(numbers, target)
        self.assertEqual(result, expected)
        result = twoSumHash(numbers, target)
        self.assertEqual(result, expected)

    def test_example2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]  # numbers[0] + numbers[2] = 2 + 4 = 6
        result = twoSum(numbers, target)
        self.assertEqual(result, expected)
        result = twoSumHash(numbers, target)
        self.assertEqual(result, expected)

    def test_example3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]  # numbers[0] + numbers[1] = -1 + 0 = -1
        result = twoSum(numbers, target)
        self.assertEqual(result, expected)
        result = twoSumHash(numbers, target)
        self.assertEqual(result, expected)


    def test_duplicate_numbers(self):
        numbers = [1, 1, 2, 3]
        target = 2
        expected = [1, 2]  # numbers[0] + numbers[1] = 1 + 1 = 2
        result = twoSum(numbers, target)
        self.assertEqual(result, expected)
        result = twoSumHash(numbers, target)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        numbers = [-3, -2, -1, 0]
        target = -5
        expected = [1, 2]  # numbers[0] + numbers[1] = -3 + -2 = -5
        result = twoSum(numbers, target)
        self.assertEqual(result, expected)
        result = twoSumHash(numbers, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 
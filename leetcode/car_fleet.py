from typing import List
import unittest

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int])->int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs = sorted(pairs)[::-1] # sorts it and the revers it. 

        stack:List[int]= []
        for p,s in pairs:
            v = (target-p)/s
            if not stack or stack[-1] < v:
                stack.append(v)
        return len(stack)

class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]
        expected = 3
        result = self.solution.carFleet(target, position, speed)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        target = 10
        position = [3]
        speed = [3]
        expected = 1
        result = self.solution.carFleet(target, position, speed)
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        target = 100
        position = [0,2,4]
        speed = [4,2,1]
        expected = 1
        result = self.solution.carFleet(target, position, speed)
        self.assertEqual(result, expected)

if __name__ == '__main__': 
    unittest.main()

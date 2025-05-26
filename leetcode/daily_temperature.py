
from typing import Tuple, List
import unittest
class Solution:
    def dailyTemperature(self, temperatures: List[int])->List[int]:
        res:List[int]=[0]*len(temperatures)
        stack:List[Tuple[int,int]]=[]
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                peak = stack.pop()
                res[peak[1]] = i-peak[0]
            stack.append((t,i))
        
        return res



    class TestDailyTemperature(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
        
        def test_example_1(self):
            temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
            expected = [1, 1, 4, 2, 1, 1, 0, 0]
            result = self.solution.dailyTemperature(temperatures)
            self.assertEqual(result, expected)
        
        def test_example_2(self):
            temperatures = [30, 40, 50, 60]
            expected = [1, 1, 1, 0]
            result = self.solution.dailyTemperature(temperatures)
            self.assertEqual(result, expected)
        
        def test_example_3(self):
            temperatures = [30, 60, 90]
            expected = [1, 1, 0]
            result = self.solution.dailyTemperature(temperatures)
            self.assertEqual(result, expected)
        
        def test_single_element(self):
            temperatures = [30]
            expected = [0]
            result = self.solution.dailyTemperature(temperatures)
            self.assertEqual(result, expected)
        
        def test_descending_temperatures(self):
            temperatures = [90, 80, 70, 60]
            expected = [0, 0, 0, 0]
            result = self.solution.dailyTemperature(temperatures)
            self.assertEqual(result, expected)

    if __name__ == '__main__':
        unittest.main()

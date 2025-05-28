from typing import List
import unittest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 1
        while r<=len(prices)-1:
            if prices[l]<prices[r]:
                prof = max(prices[r]-prices[l], prof)
            else:
                l = r
            r+=1
        return prof

class TestMaxProfit(unittest.TestCase):
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_single_price(self):
        prices = [1]
        expected = 0
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_two_prices_increasing(self):
        prices = [1, 2]
        expected = 1
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_two_prices_decreasing(self):
        prices = [2, 1]
        expected = 0
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

    def test_multiple_peaks(self):
        prices = [3, 2, 6, 5, 0, 3]
        expected = 4
        solution = Solution()
        result = solution.maxProfit(prices)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

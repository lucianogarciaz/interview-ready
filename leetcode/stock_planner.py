from typing import List, Tuple
import unittest

class StockPlanner:
    def __init__(self):
        self.stocks: List[Tuple[int, int]] = []
    
    def next(self, price: int) -> int:
        span = 1
        while self.stocks and self.stocks[-1][0] <= price:
            _,prev_span = self.stocks.pop()
            span += prev_span
        self.stocks.append((price, span))
        return span


class TestStockPlanner(unittest.TestCase):
    def test_basic_example(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(100), 1)
        self.assertEqual(sp.next(80), 1)
        self.assertEqual(sp.next(60), 1)
        self.assertEqual(sp.next(70), 2)
        self.assertEqual(sp.next(60), 1)
        self.assertEqual(sp.next(75), 4)
        self.assertEqual(sp.next(85), 6)

    def test_increasing_prices(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(10), 1)
        self.assertEqual(sp.next(20), 2)
        self.assertEqual(sp.next(30), 3)
        self.assertEqual(sp.next(40), 4)
        self.assertEqual(sp.next(50), 5)

    def test_decreasing_prices(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(50), 1)
        self.assertEqual(sp.next(40), 1)
        self.assertEqual(sp.next(30), 1)
        self.assertEqual(sp.next(20), 1)
        self.assertEqual(sp.next(10), 1)

    def test_all_equal_prices(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(50), 1)
        self.assertEqual(sp.next(50), 2)
        self.assertEqual(sp.next(50), 3)
        self.assertEqual(sp.next(50), 4)

    def test_single_price(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(100), 1)

    def test_zigzag_pattern(self):
        sp = StockPlanner()
        self.assertEqual(sp.next(31), 1)
        self.assertEqual(sp.next(41), 2)
        self.assertEqual(sp.next(48), 3)
        self.assertEqual(sp.next(59), 4)
        self.assertEqual(sp.next(79), 5)
        self.assertEqual(sp.next(20), 1)
        self.assertEqual(sp.next(30), 2)
        self.assertEqual(sp.next(100), 8)


if __name__ == '__main__':
    unittest.main()
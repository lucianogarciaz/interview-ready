import unittest

# t(0) = 0
# t(1) = 1 (1)
# t(2) = 2  (1,1) (2)
# t(3) = (1,1,1) (1,2) (2,1) (3)
# t(4) = (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2) (1,3) (3,1)
class Solution:
    def tripleStep(self, n:int)->int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n ==2:
            return 2
        if n == 3:
            return 4
        
        return self.tripleStep(n-3)+self.tripleStep(n-2)+self.tripleStep(n-1)


class TestTripleStep(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_base_cases(self):
        self.assertEqual(self.s.tripleStep(0), 0)
        self.assertEqual(self.s.tripleStep(1), 1)
        self.assertEqual(self.s.tripleStep(2), 2)
        self.assertEqual(self.s.tripleStep(3), 4)

    def test_n_equals_4(self):
        self.assertEqual(self.s.tripleStep(4), 7)

    def test_sequence_up_to_10(self):
        expected = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
        for n, val in enumerate(expected):
            self.assertEqual(self.s.tripleStep(n), val)


if __name__ == '__main__':
    unittest.main()
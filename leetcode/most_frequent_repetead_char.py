import unittest

class Solution:
    def characterReplacement(self, s: str, k:int)->int:
        if len(s) == 0:
            return 0
        res = 1
        l = 0
        r = 1
        mostFreq = 0
        count = {s[l]: 1}
        while r<len(s):
            st = s[r]
            count[st] = 1 + count.get(st, 0)
            mostFreq = max(mostFreq, count[st])
            while (r-l+1)-mostFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        
        return res
class TestCharacterReplacement(unittest.TestCase):
    def test_example1(self):
        s = "ABAB"
        k = 2
        expected = 4  # Replace both 'A's with 'B's or vice versa
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "AABABBA"
        k = 1
        expected = 4  # Replace one 'B' with 'A' to get "AAAABBA"
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        k = 1
        expected = 0
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "A"
        k = 1
        expected = 1
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_all_same_characters(self):
        s = "AAAA"
        k = 2
        expected = 4
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_no_replacements_needed(self):
        s = "ABCD"
        k = 0
        expected = 1
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

    def test_k_larger_than_string(self):
        s = "AB"
        k = 3
        expected = 2
        solution = Solution()
        result = solution.characterReplacement(s, k)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

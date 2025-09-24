import unittest

class Solution:
    def palindromePermutation(self, s:str)->bool:
        s = s.replace(" ", "")
        
        s = s.lower()
        isOdd = True if len(s)%2==1 else False
        myDict = {}
        for i,val in enumerate(s):
            if val not in myDict:
                myDict[val] = 1
            else: 
                myDict[val] += 1
        nrOfEven = 0
        for key,times in myDict.items():
            if times%2 !=0:
                if not isOdd:
                    return False
                if nrOfEven > 1:
                    return False
                else:
                    nrOfEven +=1
        return True


class TestPalindromePermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_true(self):
        self.assertTrue(self.solution.palindromePermutation("tact coa"))  # "taco cat", "atco cta", etc.

    def test_basic_false(self):
        self.assertFalse(self.solution.palindromePermutation("hello"))

    def test_empty_string(self):
        self.assertTrue(self.solution.palindromePermutation(""))

    def test_single_character(self):
        self.assertTrue(self.solution.palindromePermutation("a"))

    def test_two_same_characters(self):
        self.assertTrue(self.solution.palindromePermutation("aa"))

    def test_two_different_characters(self):
        self.assertFalse(self.solution.palindromePermutation("ab"))

    def test_even_length_true(self):
        self.assertTrue(self.solution.palindromePermutation("aabb"))

    def test_even_length_false(self):
        self.assertFalse(self.solution.palindromePermutation("aabc"))

    def test_odd_length_true(self):
        self.assertTrue(self.solution.palindromePermutation("aabbc"))

    def test_odd_length_false(self):
        self.assertFalse(self.solution.palindromePermutation("aabbcd"))

    def test_with_spaces_and_case(self):
        self.assertTrue(self.solution.palindromePermutation("Tact Coa"))  # "taco cat"

    def test_with_special_characters(self):
        self.assertTrue(self.solution.palindromePermutation("!a!"))
        self.assertFalse(self.solution.palindromePermutation("!ab!"))

if __name__ == "__main__":
    unittest.main()

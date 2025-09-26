from typing import List
import unittest

class Solution:
    # s = abc  goal = cab
    def stringRotation(self, s:str, goal:str)->bool:
        n = len(s)
        if n == 0 and len(goal) == 0:
            return True
        for i in range(n):
            if s == goal:
                return True
            p = s[-1] #peak
            s = s[:-1] #pop
            s = p + s # append
        return False

    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0:
            return 
        coordinates: List[Tuples(int, int)] = []
        n = len(matrix)
        m = len(matrix[0])
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    coordinates.append((row,col))
        
        for x,y in coordinates:
            for row in range(n):
                matrix[row][y] = 0
            for col in range(m):
                matrix[x][col] = 0

            
    def rotateMatrix(self, matrix:List[List[int]])->List[List[int]]:
        # change row by colms
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1,n):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp
        # calculate new col
        for row in range(n):
            for col in range(n//2):
                tmp = matrix[row][col]
                newCol = n - 1 - col
                matrix[row][col] = matrix[row][newCol]
                matrix[row][newCol] = tmp

        return matrix

    def stringCompression(self, s:str)->str:
        n = len(s)
        s = s.lower()
        res = ""
        l = 0
        f = 1
        prev = s[l]
        count = 1
        while f <n:
            if s[l] == s[f]:
                f+=1
                count +=1
                continue
            res += f'{s[l]}{count}'
            count = 1
            l=f
            f+=1
        res += f'{s[l]}{count}'
        return res if len(res)<len(s) else s


    def isOneAway(self, s1:str, s2:str)->bool:
        n = len(s1)
        m = len(s2)
        if abs(n-m) > 1:
            return False
        l = 0
        r = 0
        count = 0
        while l<n and r<m:
            if s1[l]!=s2[r]:
                count +=1
                if n > m:
                    l+=1
                if n < m:
                    r+=1
                if n == m:
                    l+=1
                    r+=1
                continue
            else:
                l+=1
                r+=1
        
        return False if count > 1 else True

        #         s = "race a car"
    def isPalindrome(self, s:str)->bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l +=1
            r-=1
        return True

    # " " "%20"
    def urlify2(self, s: str)->str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == " ":
                s[i] = "%20"
        return "".join(s)

    def urlify(self, s:str)->str:
        res = ""
        for i in range(len(s)):
            tmp = s[i]
            if s[i] == " ":
                tmp = "%20"
            res += tmp
        return res
    # mainly count letters
    def checkPermutation(self, s1:str, s2:str)-> bool:
        if len(s1) != len(s2):
            return False
        
        myDict ={}
        for  val in s1:
            if val not in myDict:
                myDict[val] = 0
            myDict[val] += 1
        
        for val in s2:
            if val not in myDict:
                return False
            myDict[val] -=1
        
        return True



class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_2x2(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expected = [
            [3, 1],
            [4, 2]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_single_element(self):
        matrix = [[1]]
        expected = [[1]]
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        result = self.solution.rotateMatrix([row[:] for row in matrix])
        self.assertEqual(result, expected)



class TestStringCompression(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.stringCompression("aaabbc"), "aaabbc")
        # self.assertEqual(self.solution.stringCompression("aabcccccaaa"), "a2b1c5a3")
        # self.assertEqual(self.solution.stringCompression("abc"), "abc")
        # self.assertEqual(self.solution.stringCompression("a"), "a")
        # self.assertEqual(self.solution.stringCompression(""), "")

    def test_single_character(self):
        self.assertEqual(self.solution.stringCompression("z"), "z")
        self.assertEqual(self.solution.stringCompression("zzzz"), "z4")

    def test_mixed_case(self):
        self.assertEqual(self.solution.stringCompression("AAAbbCC"), "a3b2c2")
        self.assertEqual(self.solution.stringCompression("aAaA"), "a4")

    def test_all_unique(self):
        self.assertEqual(self.solution.stringCompression("abcdef"), "abcdef")

    def test_all_same(self):
        self.assertEqual(self.solution.stringCompression("bbbbbb"), "b6")

    def test_edge_cases(self):
        self.assertEqual(self.solution.stringCompression("aabbaa"), "aabbaa")
        self.assertEqual(self.solution.stringCompression("aaabbccdd"), "a3b2c2d2")
        self.assertEqual(self.solution.stringCompression("a"*100), "a100")


class TestIsOneAway(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insert(self):
        self.assertTrue(self.solution.isOneAway("ab", "aba"))
        self.assertTrue(self.solution.isOneAway("abc", "ab"))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))

    def test_remove(self):
        self.assertTrue(self.solution.isOneAway("aba", "aa"))
        self.assertTrue(self.solution.isOneAway("abc", "ac"))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))

    def test_edit(self):
        self.assertTrue(self.solution.isOneAway("aba", "cba"))
        self.assertTrue(self.solution.isOneAway("pale", "bale"))
        self.assertTrue(self.solution.isOneAway("pale", "pate"))
        self.assertTrue(self.solution.isOneAway("pale", "pale"))

    def test_false_cases(self):
        self.assertFalse(self.solution.isOneAway("saba", "casa"))
        self.assertFalse(self.solution.isOneAway("abc", "def"))
        self.assertFalse(self.solution.isOneAway("abc", "abcdde"))
        self.assertFalse(self.solution.isOneAway("abc", "a"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isOneAway("", ""))
        self.assertTrue(self.solution.isOneAway("a", ""))
        self.assertTrue(self.solution.isOneAway("", "a"))
        self.assertFalse(self.solution.isOneAway("ab", ""))

    def test_long_strings(self):
        self.assertTrue(self.solution.isOneAway("abcdef", "abcdeg"))
        self.assertTrue(self.solution.isOneAway("abcdef", "abcdf"))
        self.assertFalse(self.solution.isOneAway("abcdef", "abqxyz"))


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_example1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = "race a car"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = " "
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_numbers_and_special_chars(self):
        s = "0P"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_palindrome_with_numbers(self):
        s = "12321"
        expected = True
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)

    def test_non_palindrome_with_numbers(self):
        s = "12345"
        expected = False
        result = self.solution.isPalindrome(s)
        self.assertEqual(result, expected)


class TestUrlify(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        self.assertEqual(self.solution.urlify("Mr John Smith"), "Mr%20John%20Smith")
        self.assertEqual(self.solution.urlify("Hello World"), "Hello%20World")
        self.assertEqual(self.solution.urlify("a b c"), "a%20b%20c")

    def test_no_spaces(self):
        self.assertEqual(self.solution.urlify("HelloWorld"), "HelloWorld")
        self.assertEqual(self.solution.urlify("abc"), "abc")

    def test_all_spaces(self):
        self.assertEqual(self.solution.urlify("   "), "%20%20%20")
        self.assertEqual(self.solution.urlify(" "), "%20")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.solution.urlify("  leading"), "%20%20leading")
        self.assertEqual(self.solution.urlify("trailing  "), "trailing%20%20")
        self.assertEqual(self.solution.urlify("  both  "), "%20%20both%20%20")

    def test_empty_string(self):
        self.assertEqual(self.solution.urlify(""), "")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(self.solution.urlify("a  b"), "a%20%20b")
        self.assertEqual(self.solution.urlify("a   b"), "a%20%20%20b")


class TestCheckPermutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permutations(self):
        self.assertTrue(self.solution.checkPermutation("abc", "bca"))
        self.assertTrue(self.solution.checkPermutation("aabbcc", "abcabc"))
        self.assertTrue(self.solution.checkPermutation("", ""))
        self.assertTrue(self.solution.checkPermutation("a", "a"))
        self.assertTrue(self.solution.checkPermutation("123", "321"))

    def test_not_permutations(self):
        self.assertFalse(self.solution.checkPermutation("abc", "ab"))
        self.assertFalse(self.solution.checkPermutation("abc", "abd"))
        self.assertFalse(self.solution.checkPermutation("aabbcc", "aabbc"))
        self.assertFalse(self.solution.checkPermutation("abc", "def"))
        self.assertFalse(self.solution.checkPermutation("a", "b"))

    def test_case_sensitivity(self):
        self.assertFalse(self.solution.checkPermutation("abc", "Abc"))
        self.assertFalse(self.solution.checkPermutation("aBc", "abc"))

    def test_special_characters(self):
        self.assertTrue(self.solution.checkPermutation("!@#", "#!@"))

class TestSetZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_3x3_with_one_zero(self):
        matrix = [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_no_zeros(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_all_zeros(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_zero(self):
        matrix = [
            [0]
        ]
        expected = [
            [0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_nonzero(self):
        matrix = [
            [5]
        ]
        expected = [
            [5]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_with_zero(self):
        matrix = [
            [1, 0],
            [3, 4]
        ]
        expected = [
            [0, 0],
            [3, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_all_zeros(self):
        matrix = [
            [0, 0],
            [0, 0]
        ]
        expected = [
            [0, 0],
            [0, 0]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_2x3_with_multiple_zeros(self):
        matrix = [
            [1, 0, 3],
            [4, 5, 6]
        ]
        expected = [
            [0, 0, 0],
            [4, 0, 6]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_3x2_with_multiple_zeros(self):
        matrix = [
            [1, 2],
            [0, 4],
            [5, 6]
        ]
        expected = [
            [0, 2],
            [0, 0],
            [0, 6]
        ]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, expected)

class TestStringRotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_rotation(self):
        s = "abcde"
        goal = "cdeab"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_no_rotation(self):
        s = "abcde"
        goal = "abced"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_same_string(self):
        s = "abcde"
        goal = "abcde"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_empty_strings(self):
        s = ""
        goal = ""
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_different_lengths(self):
        s = "abc"
        goal = "abcd"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_single_character(self):
        s = "a"
        goal = "a"
        self.assertTrue(self.solution.stringRotation(s, goal))

    def test_single_character_false(self):
        s = "a"
        goal = "b"
        self.assertFalse(self.solution.stringRotation(s, goal))

    def test_rotation_full_cycle(self):
        s = "waterbottle"
        goal = "erbottlewat"
        self.assertTrue(self.solution.stringRotation(s, goal))

if __name__ == "__main__":
    unittest.main()



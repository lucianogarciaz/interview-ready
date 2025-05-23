from typing import List
import unittest

"""
LeetCode Problem: Encode and Decode Strings
Difficulty: Medium
Category: String, Design

Problem Description:
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode.

Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;::;yes"
"""

def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s))+"#"+s
    
    return res

def decode(s: str) -> List[str]:
    res = []
    j=0
    i=0
    
    while i<len(s):
        while s[j] != "#":
            j +=1

        l = int(s[i:j])
        j +=1 # move it to the right because the first element in the [i:j] i is inclusive, j is exclusive
        i = j+l
        res.append(s[j:i])
        j = i
    
    return res


class TestEncodeDecodeStrings(unittest.TestCase):
    def test_example1(self):
        input_strs = ["lint","code","love","you"]
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

    def test_example2(self):
        input_strs = ["we", "say", ":", "yes"]
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

    def test_empty_list(self):
        input_strs = []
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

    def test_single_empty_string(self):
        input_strs = [""]
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

    def test_multiple_empty_strings(self):
        input_strs = ["", "", ""]
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

    def test_special_characters(self):
        input_strs = ["hello:world", "test;string", "multiple:;chars"]
        encoded = encode(input_strs)
        decoded = decode(encoded)
        self.assertEqual(decoded, input_strs)

if __name__ == '__main__':
    unittest.main() 
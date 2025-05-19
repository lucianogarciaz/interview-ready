package main

// Type: Dynamic Programming
// Difficulty: Medium
// Companies: This is LeetCode problem #5 "Longest Palindromic Substring". Frequently asked at
// companies like Amazon, Microsoft, and Google.

func longestPalindrome(s string) string {
	res := ""
	resLen := 0

	for i := range s {
		// for even
		l, r := i, i
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if resLen < r-l+1 {
				resLen = r - l + 1
				res = string(s[l : r+1])
			}
			l--
			r++
		}
		// for odd solutions
		l, r = i, i+1
		for l >= 0 && r < len(s) && s[r] == s[l] {
			if resLen < r-l+1 {
				resLen = r - l + 1
				res = string(s[l : r+1])
			}
			l--
			r++
		}
	}

	return res
}

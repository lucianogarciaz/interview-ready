package main

import "fmt"

// Type: Dynamic Programming
// Difficulty: Medium
// Companies: This is LeetCode problem #647 "Palindromic Substrings". Frequently asked at
// companies like Amazon, Microsoft, and Google.

func countSubstrings(s string) int {
	count := 0
	subs := []string{}
	// aaa: a a a aa aa aaa
	for i := range s {
		l, r := i, i
		for l >= 0 && r < len(s) && s[r] == s[l] {
			subs = append(subs, s[l:r+1])
			count++
			l--
			r++
		}
	}

	for i := range s {
		l, r := i, i+1
		for l >= 0 && r < len(s) && s[l] == s[r] {
			subs = append(subs, s[l:r+1])
			count++
			l--
			r++
		}
	}

	fmt.Println(subs)
	return count
}

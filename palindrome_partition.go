package main

import (
	"slices"
	"strings"
)

// Type: Backtracking / String Manipulation / Dynamic Programming
// Difficulty: Medium
// Companies: This is similar to LeetCode problem #131 "Palindrome Partitioning".
// Commonly asked at companies like Amazon, Google, Facebook, and Microsoft.
// Tests understanding of backtracking and palindrome detection algorithms.

func partitionPalindrome(s string) [][]string {
	current := []string{}
	output := [][]string{}
	var backtrack func(k int)
	backtrack = func(k int) {
		if len(s) == k && isPalindromePart(current) {
			tmp := slices.Clone(current)
			output = append(output, tmp)
		}
		for i := k; i < len(s); i++ {
			arr := strings.Split(s, "")
			val := strings.Join(arr[k:i+1], "")

			current = append(current, val)
			backtrack(i + 1)
			current = current[:len(current)-1]
		}
	}
	backtrack(0)
	return output
}

func isPalindromePart(current []string) bool {
	if len(current) == 0 {
		return false
	}
	for _, val := range current {
		arr := strings.Split(val, "")
		j := len(arr) - 1
		for i := 0; i < j; i++ {
			if arr[i] != arr[j] {
				return false
			}
			j--
		}
	}

	return true
}

package main

import "math"

// Type: Sliding Window / Hash Table
// Difficulty: Medium
// Companies: This is LeetCode problem #3 "Longest Substring Without Repeating Characters".
// Very frequently asked at Amazon, Facebook, Microsoft, Google, and Apple.
// A classic sliding window problem that tests understanding of string manipulation and
// efficient data structures.

func lengthOfLongestSubstring(str string) int {
	if len(str) <= 1 {
		return len(str)
	}

	l, r := 0, 1
	maxL := 1

	hash := map[string]bool{string(str[0]): true}
	queue := []string{string(str[0])}
	for r < len(str) {
		f, ok := hash[string(str[r])]
		if !ok || (ok && !f) {
			hash[string(str[r])] = true
			maxL = int(math.Max(float64(maxL), float64(len(queue)+1)))
		} else {
			count := 0
			for len(queue) > 0 {
				count++
				if queue[0] == string(str[r]) {
					queue = queue[1:]
					break
				}
				rem := queue[0]
				queue = queue[1:]
				hash[rem] = false
			}

			l = l + count
		}

		queue = append(queue, string(str[r]))
		r++
	}

	return maxL
}

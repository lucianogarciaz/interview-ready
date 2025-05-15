package main

// Type: Dynamic Programming / Recursion
// Difficulty: Easy to Medium
// Companies: This is similar to LeetCode problem #70 "Climbing Stairs" with a variation.
// Commonly asked at companies like Google, Amazon, and Apple. It's from "Cracking the Coding Interview"
// book (6.1 Triple Step).

func tripleStep(n int) int {
	if n <= 2 {
		return n
	}
	if n == 3 {
		return 4
	}

	return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)
}

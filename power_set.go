package main

import (
	"slices"
)

// Type: Backtracking / Recursion / Combinatorics
// Difficulty: Medium
// Companies: Similar to LeetCode problems #78 "Subsets" and #90 "Subsets II" (with duplicates).
// Commonly asked at companies like Google, Facebook, Amazon, and Microsoft.
// Tests understanding of backtracking, recursion, and combinatorial generation.

func powerSet(a []int) [][]int {
	if len(a) == 0 {
		return [][]int{{}}
	}
	if len(a) == 1 {
		return [][]int{{}, {a[0]}}
	}

	previous := powerSet(a[1:])
	output := previous
	for _, v := range previous {
		couple := append([]int{a[0]}, v...)
		output = append(output, couple)
	}

	return output
}

func powerSetBacktrack(a []int) [][]int {
	var res [][]int
	var current []int
	var backtrack func(start int)
	backtrack = func(s int) {
		tmp := slices.Clone(current)
		res = append(res, tmp)
		for i := s; i < len(a); i++ {
			current = append(current, a[i])

			backtrack(i + 1)

			current = current[:len(current)-1]
		}
	}
	backtrack(0)
	return res
}

func powerSetWithDuplicates(nums []int) [][]int {
	n := len(nums)
	slices.Sort(nums)
	output := make([][]int, 0, n)
	current := []int{}
	var backtrack func(s int)
	backtrack = func(s int) {
		tmp := slices.Clone(current)
		output = append(output, tmp)
		for i := s; i < n; i++ {
			if s != i && nums[i] == nums[i-1] {
				continue
			}

			current = append(current, nums[i])
			backtrack(i + 1)
			current = current[:len(current)-1]
		}
	}

	backtrack(0)
	return output
}

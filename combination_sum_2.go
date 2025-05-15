package main

import (
	"slices"
)

// Type: Backtracking / Combinatorics
// Difficulty: Medium
// Companies: This is LeetCode problem #40 "Combination Sum II".
// Commonly asked at companies like Amazon, Facebook, Google, and Microsoft.
// Tests understanding of backtracking with duplicate handling and pruning techniques.

func combinationSum2(candidates []int, target int) [][]int {
	if len(candidates) == 0 {
		return [][]int{}
	}
	slices.Sort(candidates)

	output := [][]int{}
	current := []int{}

	var backtrack func(s int)
	backtrack = func(s int) {
		sum, ok := isValidCombination(target, current)
		if ok {
			if sum == target {
				tmp := slices.Clone(current)
				output = append(output, tmp)
				return
			}
		}
		if !ok {
			return
		}

		for i := s; i < len(candidates); i++ {
			// Skip duplicates
			if i > s && candidates[i] == candidates[i-1] {
				continue
			}

			current = append(current, candidates[i])
			backtrack(i + 1)
			current = current[:len(current)-1]
		}
	}
	backtrack(0)
	return output
}

func isValidCombination(target int, current []int) (int, bool) {
	sum := 0
	for _, v := range current {
		sum += v
	}
	return sum, target-sum >= 0
}

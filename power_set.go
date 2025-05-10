package main

import (
	"slices"
)

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

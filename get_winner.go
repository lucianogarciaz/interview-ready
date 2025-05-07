package main

import "sort"

func getWinner(arr []int, k int) int {
	pivot := arr[0]
	winCount := 0

	for i := 1; i < len(arr); i++ {
		if winCount >= k {
			return pivot
		}
		if pivot > arr[i] {
			winCount++
			continue
		}
		winCount = 1
		pivot = arr[i]
	}

	return pivot
}

func getWinnerNotWorking(arr []int, k int) int {
	if len(arr) <= k {
		sort.Slice(arr, func(i, j int) bool {
			return arr[i] > arr[j]
		})
		return arr[0]
	}
	numRotated := 0
	for k > numRotated {
		if arr[1] > arr[0] {
			numRotated = 1
			tmp := arr[0]
			arr[0] = arr[1]
			copy(arr[1:], arr[2:])
			arr[len(arr)-1] = tmp
			continue
		}
		tmp := arr[1]
		copy(arr[1:], arr[2:])
		arr[len(arr)-1] = tmp
		numRotated++
	}

	return arr[0]
}

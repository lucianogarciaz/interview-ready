package main

import (
	"sort"
)

func factoriesEmission(arr []int) int {
	sum := float64(0)
	// sum - arr[i]+arr[i]/filters*2 < half
	for i := 0; i < len(arr); i++ {
		sum += float64(arr[i])
	}
	half := float64(sum / 2)
	sort.Ints(arr)
	filters := float64(0)
	// 5 3 0 :
	for i := len(arr) - 1; i >= 0; i-- {
		if arr[i] == 0 {
			break
		}
		appliedFilters := float64(1)

		for i != 0 && float64(sum-float64(arr[i])+(float64(arr[i])/(2*appliedFilters))) >= half && (float64(arr[i])/(appliedFilters*2)) > float64(arr[i-1]) {
			appliedFilters++
		}
		sum = sum - float64(arr[i]) + (float64(arr[i]) / (2 * appliedFilters))
		// hafl = 4 sum
		//           5
		filters += appliedFilters
		if half >= sum {
			i = -1
		}
	}

	return int(filters)
}

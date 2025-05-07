package main

import (
	"math"
)

// [2 5 3 9 5 3]
func minimumAverageDifference(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return 0
	}

	minAbs := -1
	index := 0
	sumEnd := 0
	sumFront := 0
	n := len(nums)
	for i := n - 1; i >= 0; i-- {
		sumEnd += nums[i]
	}

	for i, v := range nums {
		sumFront += v
		sumEnd -= v
		avg1 := sumFront / (i + 1)
		avg2 := 0
		if (n - i - 1) > 0 {
			avg2 = sumEnd / (n - i - 1)
		}
		abs := int(math.Abs(float64(avg1 - avg2)))
		if abs < minAbs || minAbs == -1 {
			index = i
			minAbs = abs
		}
	}

	return index
}

package main

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

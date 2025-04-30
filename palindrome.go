package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(n int) bool {
	number := fmt.Sprintf("%d", n)
	for i := 0; len(number)/2 > i; i++ {
		j := len(number) - i - 1
		if number[i] != number[j] {
			return false
		}
	}

	return true
}

func isPalindrome2(n int) bool {
	if n < 0 {
		return false
	}

	stringN := strconv.Itoa(n)
	right := len(stringN) - 1

	for left := 0; left < right; left++ {
		a := stringN[left]
		b := stringN[right]
		if a != b {
			return false
		}
		right--
	}

	return true
}

package main

import "math"

func characterReplacement(s string, k int) int {
	if len(s) <= 1 {
		return len(s)
	}
	l, r := 0, 1
	res := 0
	maxF := 0
	hash := map[string]int{string(s[0]): 1}

	for len(s) > r {
		_, ok := hash[string(s[r])]
		if !ok {
			hash[string(s[r])] = 0
		}
		hash[string(s[r])] = hash[string(s[r])] + 1
		maxF = int(math.Max(float64(maxF), float64(hash[string(s[r])]))) //either the max or the new count

		if ((r-l)+1)-maxF > k {
			hash[string(s[l])] = hash[string(s[l])] - 1
			l++
		}

		res = int(math.Max(float64(res), float64(((r - l) + 1))))
		r++
	}
	return res
}

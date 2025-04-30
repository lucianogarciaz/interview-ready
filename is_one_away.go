package main

import "strings"

func isOneAway(s1 string, s2 string) bool {
	count := 0
	i, j := 0, 0
	s1 = strings.ToLower(s1)
	s2 = strings.ToLower(s2)
	// palest
	// pale
	// i  j  vs1  vs2
	// 0  0    p   p
	// 1  1    a   a
	// 2  2    l   l
	// 3  3
	for i < len(s1) || j < len(s2) {
		if i == len(s1) {
			count++
			j++
			continue
		}
		if j == len(s2) {
			i++
			count++
			continue
		}

		vs1 := string(s1[i])
		vs2 := string(s2[j])
		if vs1 == vs2 {
			i++
			j++
			continue
		}

		count++

		if len(s2) > len(s1) {
			j++
			continue
		}
		if len(s1) > len(s2) {
			i++
			continue
		}

		i++
		j++
	}

	return count <= 1
}

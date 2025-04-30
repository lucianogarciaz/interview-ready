package main

import (
	"strings"
)

// watterbottl -> watterbottl
func stringRotation(s1 string, s2 string) bool {
	if s2 == "" {
		return true
	}
	// HANDLING STRINGS WHEN WE NEED TO UPDATE THE VALUES
	runes := []rune(s2)
	for i := 0; i < len(s2); i++ {
		if isSubstring(s1, string(runes)) {
			return true
		}

		tmp := runes[len(s2)-1]
		copy(runes[1:], runes[:len(s2)-1])
		runes[0] = tmp
	}

	return false
}

func isSubstring(s1 string, s2 string) bool {
	return strings.Contains(s1, s2)
}

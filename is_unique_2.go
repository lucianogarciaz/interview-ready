package main

// 1. *Is Unique*:

// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

// export default function isUnique(str: string): boolean {}
// hello -> false
// abcdefg -> true
func isUnique2(s string) bool {
	mapIsUnique := map[string]bool{}

	for _, v := range s {
		_, ok := mapIsUnique[string(v)]
		if !ok {
			mapIsUnique[string(v)] = true
		} else {
			return false
		}

	}

	return true
}

// This algoright doesn't use extra memomy
func isUnique3(s string) bool {
	if s == "" {
		return true
	}

	for i := 0; i < len(s)-1; i++ {
		prev := string(s[i])
		for j := i + 1; j < len(s); j++ {
			actual := string(s[j])
			if prev == actual {
				return false
			}
		}
	}

	return true
}

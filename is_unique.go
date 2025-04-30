package main

// 1. *Is Unique*:

// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

// export default function isUnique(str: string): boolean {}
// hello
func isUnique(s string) bool {
	for i := 0; i < len(s); i++ {
		l := string(s[i])
		for j := i + 1; j < len(s); j++ {
			r := string(s[j])
			if l == r {
				return false
			}
		}
	}

	return true
}

package main

import "sort"

func longestCommonPrefix(strs []string) string {
	// what I should do is have a string (prefix) with the first letter and start checking if all the words have it. if they don't we just return the prefix.
	//Input: strs = ["flower","flow","flight"]
	// Output: "fl"
	if len(strs) == 0 {
		return ""
	}

	sort.Slice(strs, func(i, j int) bool {
		return len(strs[i]) < len(strs[j])
	})

	if len(strs) == 1 {
		return strs[0]
	}

	prefix := ""
	firstWord := strs[0]

	for i := 0; i < len(firstWord); i++ {
		for j := 1; j < len(strs); j++ {
			prefixToCompare := firstWord[:i+1]
			stringWithPrefix := strs[j][:i+1]
			if prefixToCompare != stringWithPrefix {
				return prefix
			}
		}

		prefix = firstWord[:i+1]
	}

	return firstWord
}

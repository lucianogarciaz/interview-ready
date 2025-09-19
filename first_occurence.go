package main

func strStr(haystack string, needle string) int {
	if len(needle) > len(haystack) || haystack == "" || needle == "" {
		return -1
	}

	// "sadbutsad" //sad
	for i := 0; len(haystack) > i; i++ {
		if i+len(needle) > len(haystack) {
			return -1
		}
		// the last element in an go slice is not included when using :op // "sadbutsad" -> [0:3] = sad
		if haystack[i:i+len(needle)] == needle {
			return i
		}
	}

	return -1
}

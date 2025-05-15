package main

// Type: Hash Map / Frequency Counter
// Difficulty: Easy to Medium
// Companies: This type of frequency counting and string manipulation problem is common in interviews at
// companies like Google, Amazon, and Microsoft.
//
// [ hu  un  ng ga ar ry]
// [h:u:  u:n:  n:g:  g:a: a:r: r:y]
// find the first letter.
// create the hash set
// loop from the beginning until the end.

func findWords(str []string) string {
	findF := map[string]int{}
	for i := 0; i < len(str); i++ {
		f := string(str[i][0])
		_, ok := findF[f]
		if !ok {
			findF[f] = 0
		}
		findF[f] += 1
	}
	index := 0
	for i := 0; i < len(str); i++ {
		f := string(str[i][0])
		val := findF[f]
		if val == 1 {
			index = i
			break
		}
	}

	var word string
	for i := 0; i < len(str); i++ {
		ix := index + i
		if ix == len(str) {
			ix = 0
		}

		word = word + string(str[ix][0])
		if i+1 == len(str) {
			word = word + string(str[ix][2])
		}
	}

	return word
}

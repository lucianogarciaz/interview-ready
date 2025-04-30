package main

import "fmt"

// Implement a method to perform basic string compression using the counts of repeated characters.
// For example, the string aabcccccaaa would become a2blc5a3,
// If the "compressed" string would not become smaller than the original string,
// your method should return the original string.
// You can assume the string has only uppercase and lowercase letters (a - z).

// aabcccccaaa
// current!=previous count = 1, setNumber in Output
func stringConversion(str string) string {
	if len(str) < 2 {
		return str
	}

	count := 1
	p := string(str[0])
	output := p
	isGreaterThanOne := false
	// aabcccccaaa
	//  count  output  i  a  p
	//    1      a     0     a
	//    2      a     1  a  a
	//    1      a2b    2  b  a
	for i := 1; i < len(str); i++ {
		a := string(str[i])
		if a != p {
			output = fmt.Sprintf("%s%d%s", output, count, a)
			count = 1
			p = a
			continue
		}
		if count > 1 {
			isGreaterThanOne = true
		}

		count++
	}
	output = fmt.Sprintf("%s%d", output, count)

	if !isGreaterThanOne {
		return str
	}

	return output
}

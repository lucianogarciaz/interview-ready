package main

// Input: s = "   fly me   to   the moon  "

func lengthOfLastWord(s string) int {
	output := ""
	// i, val, output
	// 20, " ", ""
	// 19, " ", ""
	// 18, "n", "n"
	// 17, "o", "no"
	// 16, "o", "noo"
	// 15, "m", "noom",

	for i := len(s) - 1; i >= 0; i-- {
		val := string(s[i])
		if val == " " {
			if output != "" {
				break
			}

			continue
		}

		output = output + val

	}

	return len(output)
}
func lengthOfLastWord2(s string) int {
	output := ""
	newSpace := false
	for i := 0; i < len(s); i++ {
		val := string(s[i])
		if newSpace && val != " " {
			newSpace = false
			output = ""
		}

		if val != " " {
			output = output + val
			newSpace = false
		}

		if val == " " {
			newSpace = true
		}
	}

	return len(output)
}

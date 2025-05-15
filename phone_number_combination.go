package main

// Type: Backtracking / String Manipulation / Recursion
// Difficulty: Medium
// Companies: This is LeetCode problem #17 "Letter Combinations of a Phone Number".
// Frequently asked at companies like Amazon, Google, Microsoft, and Facebook.
// Tests understanding of backtracking patterns and string manipulation.

func letterCombinations(digits string) []string {
	if digits == "" {
		return []string{}
	}
	result := []string{}
	state := ""
	var backtrack func(s int)
	backtrack = func(s int) {
		if len(digits) == len(state) {
			result = append(result, state)
			return
		}
		for i := 0; i < 4; i++ {
			val, ok := getStringFromNumber(string(digits[s]), i)
			if !ok {
				return
			}

			state += val
			backtrack(s + 1)

			state = state[:len(state)-1]
		}
	}
	backtrack(0)
	return result
}

func getStringFromNumber(str string, i int) (string, bool) {
	if i > 2 && (str != "7" && str != "9") {
		return "", false
	}

	switch str {
	case "2":
		vals := []string{"a", "b", "c"}
		return vals[i], true
	case "3":
		vals := []string{"d", "e", "f"}
		return vals[i], true
	case "4":
		vals := []string{"g", "h", "i"}
		return vals[i], true
	case "5":
		vals := []string{"j", "k", "l"}
		return vals[i], true
	case "6":
		vals := []string{"m", "n", "o"}
		return vals[i], true
	case "7":
		vals := []string{"p", "q", "r", "s"}
		return vals[i], true
	case "8":
		vals := []string{"t", "u", "v"}
		return vals[i], true
	case "9":
		vals := []string{"w", "x", "y", "z"}
		return vals[i], true
	default:
		return "", false
	}
}

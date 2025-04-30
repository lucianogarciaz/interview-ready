package main

func romanToInt2(s string) int {
	//	{"III", 3},
	// {"LVIII", 58},
	// {"IV", 4},
	romanMap := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	sum := 0
	//  {"VIX", 59},
	// i, element, elementValue, followingElement, fElementValue, sum
	// 0, I, 1, V, 4, -1
	// 1,1,V, -,-,4
	for i := 0; i < len(s); i++ {
		element := string(s[i])
		elementValue := romanMap[element]

		// last element detected
		if i+1 == len(s) {
			sum += elementValue
			continue
		}

		followingElement := string(s[i+1])
		fElementValue := romanMap[followingElement]

		if fElementValue > elementValue {
			sum -= elementValue
			continue
		}

		sum += elementValue
	}

	return sum
}

func romanToInt(s string) int {
	// III = 3
	// XV = 15
	// IX = 9

	// we will need a map from roman to integer.
	romanMap := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	sum := 0
	// if the number on the left is smaller than the following one, it should substract, if not sum.
	for i := 0; i <= len(s)-1; i++ {
		if len(s)-1 != i && romanMap[string(s[i])] < romanMap[string(s[i+1])] {
			sum -= romanMap[string(s[i])]
			continue
		}

		sum += romanMap[string(s[i])]
	}

	return sum
}

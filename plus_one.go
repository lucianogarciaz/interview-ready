package main

// start from the left of the slice summing 1 until i don't have carry.

func plusOne(digits []int) []int {
	carry := true
	// [123]
	// carry, i, value, digits
	// true
	// false, 2, 3,  124
	// false, 1, 2, 124,
	// false, 0, 1, 124,
	for i := len(digits) - 1; i >= 0; i-- {
		value := digits[i]

		if value == 9 && carry {
			value = 0
			carry = true
			digits[i] = value
			continue
		}

		if carry {
			carry = false
			value += 1
			digits[i] = value
		}
	}
	if carry {
		digits = append([]int{1}, digits...)
	}

	return digits
}

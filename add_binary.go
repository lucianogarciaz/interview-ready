package main

func addBinary(a string, b string) string {
	carry := false
	result := ""

	if len(a) > len(b) {
		for len(a) > len(b) {
			b = "0" + b
		}
	}
	if len(a) < len(b) {
		for len(a) < len(b) {
			a = "0" + a
		}
	}
	// "1010"
	// "1011"
	// i, carry,valA,valB,previousValue, nextCarry, return
	// 3, false, 0, 1,      1,               false,    1
	// 2, false, 1, 1,      0,               true,     01
	// 1, true,  0, 0,      1,               false    101
	// 0  false  1  1       0                true     0101

	for i := len(a) - 1; i >= 0; i-- {
		//check carry for calculation
		valA := string(a[i])
		valB := string(b[i])
		previousValue, nextCarry := calculations(valA, valB)
		if carry {
			carry = false
			var potentialCarry bool
			previousValue, potentialCarry = calculations(previousValue, "1")
			if potentialCarry {
				nextCarry = potentialCarry
			}
		}

		if nextCarry {
			carry = true
		}
		result = previousValue + result
	}

	if carry {
		result = "1" + result
	}

	return result
}

func calculations(a, b string) (string, bool) {
	if a == "1" && b == "1" {
		return "0", true
	}

	if a == "1" || b == "1" {
		return "1", false
	}

	return "0", false
}

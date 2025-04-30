package main

// 4 -> 2
// 1, 2

// 8
// n  multiply
// 1  1
// 2  4
// 3  9

func mySqrt(x int) int {

	left := 0
	right := x
	if x == 1 {
		return 1
	}
	// 8
	//  left, right, pivot, r
	//  0 	    8      4    16
	//  0       4      2    4
	//  3       4      3    9
	//  3       3
	for left < right {
		pivot := (right + left) / 2

		r := pivot * pivot
		if r > x {
			right = pivot
			continue
		}
		if r == x {
			return pivot
		}

		if r < x {
			left = pivot + 1
		}
	}

	return left - 1
}

func mySqrt2(x int) int {
	if x == 0 || x == 1 {
		return x
	}

	n := 1
	for {
		multiply := n * n
		if multiply > x {
			n -= 1
			break
		}

		if multiply == x {
			break
		}

		n++
	}

	return n
}

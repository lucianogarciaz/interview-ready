package main

func climbStairs(n int) int {
	one := 1
	two := 1

	for i := 0; (n - 1) > i; i++ {
		temp := one
		one = one + two
		two = temp
	}

	return one
}

var someMap = map[int]int{1: 1, 2: 2}

func climbStairs2(n int) int {
	if n <= 2 {
		return n
	}

	n1, ok := someMap[n-1]
	if !ok {
		n1 = climbStairs(n - 1)
		someMap[n-1] = n1
	}

	n2, ok := someMap[n-2]
	if !ok {
		n2 = climbStairs(n - 2)
		someMap[n-2] = n2
	}

	return n1 + n2
}

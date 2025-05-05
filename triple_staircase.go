package main

func tripleStep(n int) int {
	if n <= 2 {
		return n
	}
	if n == 3 {
		return 4
	}

	return tripleStep(n-1) + tripleStep(n-2) + tripleStep(n-3)
}

package main

// very simple exercise of recursion
func reverseString(str string) string {
	if len(str) <= 1 {
		return str
	}
	// hello: takes the first letter h and set aside, then the same with ello
	return reverseString(str[1:]) + string(str[0])
}

func isPalindromeRecusively(str string) bool {
	if len(str) <= 1 {
		return true
	}

	if len(str) <= 2 {
		return str[0] == str[1]
	}

	return str[0] == str[len(str)-1] && isPalindromeRecusively(str[1:len(str)-1])
}

func printNumbersRecursive(n int) []int {
	if n == 0 {
		return []int{}
	}

	if n <= 1 {
		return []int{n}
	}

	element := []int{n}
	return append(element, printNumbersRecursive(n-1)...)
}

func sumArrayRecurs(arr []int) int {
	if len(arr) == 0 {
		return 0
	}

	if len(arr) <= 1 {
		return arr[0]
	}

	return arr[0] + sumArrayRecurs(arr[1:])
}

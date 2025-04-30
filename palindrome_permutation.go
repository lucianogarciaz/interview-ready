package main

import "strings"

// para permutation directamente usar hash maps y contar palabras.
func isPalindromePermutation(s1 string) bool {
	s1 = strings.ToLower(s1)
	s1 = strings.ReplaceAll(s1, " ", "")
	hash := map[string]int{}
	for i := 0; i < len(s1); i++ {
		val := string(s1[i])
		v, ok := hash[val]
		if !ok {
			hash[val] = 1
			continue
		}

		hash[val] = v + 1
	}

	stringLen := len(s1)
	count := 0
	for _, v := range hash {
		if v%2 != 0 { // chequeo si es no es PAR, puede tener MAXIMO una letra si es que es impar
			count++
		}
	}

	if count > 1 {
		return false
	}

	if stringLen%2 == 1 && count > 2 {
		return false
	}

	return true
}

// do no
func palindromPermutation2(str string) bool {
	if len(str) <= 2 {
		return true
	}
	str = strings.ToLower(str)
	str = strings.ReplaceAll(str, " ", "")
	mapCountPalindrome := map[string]int{}
	for _, v := range str {
		count, ok := mapCountPalindrome[string(v)]
		if !ok {
			mapCountPalindrome[string(v)] = 1
			continue
		}
		mapCountPalindrome[string(v)] += count
	}
	count := 0
	for _, v := range mapCountPalindrome {
		if v%2 != 0 {
			count++
		}
	}

	return count == 0 || (count == 1 && len(str)%2 == 1)

}

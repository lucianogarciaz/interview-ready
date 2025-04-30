package main

func isValid(s string) bool {
	if s == "" {
		return true
	}

	mapParenthesis := map[string]bool{
		"[": true,
		"{": true,
		"(": true,
		"]": false,
		"}": false,
		")": false,
	}

	validSymbol := map[string]string{
		"[": "]",
		"{": "}",
		"(": ")",
	}

	var parenthesisStack []string

	for i := 0; i < len(s); i++ {
		symbol := string(s[i])
		if mapParenthesis[symbol] {
			parenthesisStack = append(parenthesisStack, symbol)
			continue
		}
		if len(parenthesisStack) == 0 {
			return false
		}
		popElement := parenthesisStack[len(parenthesisStack)-1]
		extractedSymbol := validSymbol[popElement]
		if symbol != extractedSymbol {
			return false
		}

		// pop
		parenthesisStack = parenthesisStack[:len(parenthesisStack)-1]
	}

	return len(parenthesisStack) <= 0
}

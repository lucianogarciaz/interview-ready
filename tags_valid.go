package main

import (
	"strings"
)

// <app></app>
func countBrokenTags(strTags string) int {
	l := 0
	arr := strings.Split(strTags, "")
	stack := []bool{}

	for l < len(arr) {
		openTag := strings.Join(arr[l:l+5], "")
		if openTag == "<app>" {
			stack = append(stack, true)
			l = l + 5
			continue
		}

		closingTag := strings.Join(arr[l:l+6], "")
		if closingTag == "</app>" {
			if len(stack) == 0 {
				stack = append(stack, false)
			} else {
				peak := stack[len(stack)-1]
				if peak {
					stack = stack[:len(stack)-1]
				} else {
					stack = append(stack, false)
				}
			}
			l = l + 6
			continue
		}

		l++
	}

	return len(stack)
}

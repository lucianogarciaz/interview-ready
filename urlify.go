package main

func Urlify(s1 string) string {
	output := ""
	for i := 0; i < len(s1); i++ {
		val := string(s1[i])
		if val == " " {
			output += "%20"
			continue
		}
		output += val
	}
	return output
}

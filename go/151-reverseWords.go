package main

import (
	"strings"
)

func reverseWords(s string) string {

	words := strings.Split(strings.Trim(s, " "), " ")

	clean_words := make([]string, 0)

	for i := range words {
		if words[i] != "" {
			clean_words = append(clean_words, words[i])
		}
	}

	i := 0
	j := len(clean_words) - 1
	for i < j {
		temp := clean_words[i]
		clean_words[i] = clean_words[j]
		clean_words[j] = temp
		i++
		j--
	}

	return strings.Join(clean_words, " ")
}

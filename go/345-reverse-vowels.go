package main

func reverseVowels(s string) string {
	i := 0
	j := len(s) - 1

	vowels := make(map[byte]bool)
	vowels['u'] = true
	vowels['e'] = true
	vowels['o'] = true
	vowels['a'] = true
	vowels['i'] = true
	vowels['U'] = true
	vowels['E'] = true
	vowels['O'] = true
	vowels['A'] = true
	vowels['I'] = true

	arrS := make([]byte, len(s))
	for i := range s {
		arrS[i] = s[i]
	}

	for i < j {
		if !vowels[s[i]] {
			i++
		} else if !vowels[s[j]] {
			j--
		} else {
			temp := arrS[i]
			arrS[i] = arrS[j]
			arrS[j] = temp
			i++
			j--
		}
	}

	return string(arrS)
}
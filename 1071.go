package main

func gcdOfStrings(str1 string, str2 string) string {
	subLen := 1
	lenStr1 := len(str1)
	lenStr2 := len(str2)
	shorterLen := lenStr1
	if lenStr1 > lenStr2 {
		shorterLen = lenStr2
	}
	possible_outputs := []string{}
	for subLen <= shorterLen {
		if subLen > 1 {
			if lenStr1%subLen != 0 || lenStr2%subLen != 0 {
				subLen++
				continue
			}
		}
		if str1[0:subLen] != str2[0:subLen] {
			subLen++
			continue
		}
		isContinue := false
		for i := 0; i+2*subLen <= lenStr1; i = i + subLen {
			curSub := str1[i : i+subLen]
			nextSub := str1[i+subLen : i+2*subLen]
			if curSub != nextSub {
				subLen++
				isContinue = true
				break
			}
		}
		if isContinue {
			continue
		}
		for i := 0; i+2*subLen <= lenStr2; i = i + subLen {
			curSub := str2[i : i+subLen]
			nextSub := str2[i+subLen : i+2*subLen]
			if curSub != nextSub {
				subLen++
				isContinue = true
				break
			}
		}
		if isContinue {
			continue
		}
		possible_outputs = append(possible_outputs, str1[0:subLen])
		subLen++
	}
	if len(possible_outputs) > 0 {
		return possible_outputs[len(possible_outputs)-1]
	}
	return ""
}

func main() {
	print(gcdOfStrings("ABABABAB", "ABAB"))
}

package main

var kidsWithCandies = func(candies []int, extraCandies int) []bool {
	max := 0
	result := make([]bool, len(candies))
	for i := range candies {
		if candies[i] > max {
			max = candies[i]
		}
	}
	for i := range candies {
		if candies[i]+extraCandies >= max {
			result[i] = true
		} else {
			result[i] = false
		}
	}

	return result
}
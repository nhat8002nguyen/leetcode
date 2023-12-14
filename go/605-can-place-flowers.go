package main

var canPlaceFlowers = func(flowerbed []int, n int) bool {
	count := 0
	lenFlowerbed := len(flowerbed)
	for i := range flowerbed {
		if flowerbed[i] == 0 {
			if lenFlowerbed == 1 {
				count++
			}
			if i == 0 && i+1 < lenFlowerbed && flowerbed[i+1] == 0 {
				count++
				flowerbed[i] = 1
			} else if i > 0 {
				if flowerbed[i-1] != 1 && (i+1 == lenFlowerbed || flowerbed[i+1] != 1) {
					count++
					flowerbed[i] = 1
				}
			}
		}
	}
	if count >= n {
		return true
	}
	return false
}
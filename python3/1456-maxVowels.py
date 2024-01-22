class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["u", "e", "o", "a", "i"]
        max_vowels = 0
        for l in s[0:k]:
            if l in vowels:
                max_vowels += 1

        cur_count = max_vowels

        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                cur_count -= 1
            if s[i+k-1] in vowels:
                cur_count += 1
            if cur_count > max_vowels:
                max_vowels = cur_count

        return max_vowels

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            # If we encounter a zero, we increment the zero count
            if nums[right] == 0:
                zeros += 1

            # If our zero count exceeds k, move the left pointer up and
            # adjust the zero count as necessary
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # The current window size is right - left + 1, check if it's the biggest we've seen
            max_length = max(max_length, right - left + 1)

        return max_length


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1,
      1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(s.longestOnes([0, 0, 0, 1], 4))

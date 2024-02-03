from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max = 0
        support = 1
        start = 0
        if len(nums) == 1:
            return 0

        for i, value in enumerate(nums):
            if value == 0:
                if support == 1:
                    support -= 1
                elif support == 0:
                    while support == 0:
                        if nums[start] == 0:
                            support += 1
                        start += 1
                    support = 0
            else:
                if max == 0:
                    max = 1
                if support == 0:
                    count = i - start
                else:
                    count = i - start + 1
                if count > max:
                    max = count

        return max if max < len(nums) else max-1


s = Solution()
print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

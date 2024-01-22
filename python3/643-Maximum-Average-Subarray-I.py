from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[0:k])
        max_avg = cur_sum/k

        if k == len(nums):
            return max_avg

        for i in range(1, len(nums)-k+1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            avg = cur_sum/k
            if avg > max_avg:
                max_avg = avg

        return max_avg


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(s.findMaxAverage([5], 1))
print(s.findMaxAverage([0, 1, 1, 3, 3], 4))

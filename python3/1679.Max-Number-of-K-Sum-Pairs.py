from typing import List

class Solution:
    """
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.

    Example 1:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
    - Remove numbers 1 and 4, then nums = [2,3]
    - Remove numbers 2 and 3, then nums = []
    There are no more pairs that sum up to 5, hence a total of 2 operations.

    Example 2:
    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
    - Remove the first two 3's, then nums = [1,4,3]
    There are no more pairs that sum up to 6, hence a total of 1 operation.

    Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        value_count = {}
        operation = 0
        for num in nums:
            if k-num in value_count and value_count[k-num] > 0:
                operation += 1
                value_count[k-num] -= 1
            elif num not in value_count:
                value_count[num] = 1
            elif value_count[num] >= 0:
                value_count[num] += 1

        return operation

s = Solution()
print(s.maxOperations([1,2,3,4], 5))
print(s.maxOperations([3,1,3,4,3], 6))
print(s.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))

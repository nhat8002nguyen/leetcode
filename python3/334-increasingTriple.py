from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0]
        second = None
        temp_first = nums[0]
        temp_second = None
        
        nums_length = len(nums)
        if nums_length < 3:
            return False
        
        for i in range(1, len(nums)):
            if nums[i] > first and (second == None or nums[i] < second):
                second = nums[i]

            if nums[i] < first and nums[i] < temp_first:
                temp_first = nums[i]

            if nums[i] > temp_first and (temp_second == None or nums[i] < temp_second):
                temp_second = nums[i]

            if temp_first < first or (temp_second != None and second != None and temp_second < second):
                first = temp_first
                second = temp_second

            if nums[i] > first and second != None and  nums[i] > second:
                return True

        return False

s = Solution()
print(s.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
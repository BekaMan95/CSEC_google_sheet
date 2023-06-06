class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listed = {}
        for i, num in enumerate(nums):
            if target-num in listed:
                return([listed[target-num], i])
            elif num not in listed:
                listed[num] = i

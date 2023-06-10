class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        out = []
        nums.sort()
        for i in range(int(len(nums)/2)):
            if i == 0:
                out.append(nums[0]+nums[-1])
            else:
                out.append(nums[i] + nums[-i-1])

        out.sort()
        return out[-1]

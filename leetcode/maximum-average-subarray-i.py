class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = []
        avg = min(nums)
        for i in range(len(nums)-k+1):
            if not window:
                window = nums[i:i+k]
                s = sum(window)
            else:
                s = s - nums[i-1] + nums[i+k-1]
            if s/k > avg:
                avg = s/k
        return avg

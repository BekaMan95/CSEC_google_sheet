class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        counter = {}
        con = 1
        for i in range(len(nums)):
            if nums[i] not in counter:
                counter[nums[i]] = 1
            else:
                con = counter.get(nums[i])
                counter.update({nums[i]: con+1})

        res = sorted(counter.items(), key=lambda x: x[1],reverse=True)

        for i in range(k):
            out.append(res[i][0])

        return out

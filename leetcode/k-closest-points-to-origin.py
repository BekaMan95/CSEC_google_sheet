import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        out = []
        for i in range(len(points)):
            m = (points[i][0]*points[i][0]) + (points[i][1]*points[i][1])
            distance.append([math.sqrt(m),[points[i][0],points[i][1]]])
        distance.sort()

        for i in range(k):
            out.append(distance[i][1])

        return out

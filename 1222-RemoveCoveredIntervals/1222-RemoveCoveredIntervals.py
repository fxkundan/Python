# Last updated: 04/05/2026, 00:32:34
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        index = -1
        
        for i in range(len(intervals)):
            if i == 0: index = 0
            else:
                if intervals[index][0] == intervals[i][0] and intervals[index][1] < intervals[i][1]:
                    intervals[index][1] = intervals[i][1]
                elif not(intervals[index][1] >= intervals[i][0] and intervals[index][1] >= intervals[i][1]): 
                    index = i
                    count += 1
        return count + 1
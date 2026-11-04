class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        intervals = self.intervals
        # Find the insertion index using binary search on interval starts
        i = bisect.bisect_left(intervals, [val, val])
        
        left = i - 1
        right = i
        
        # Check if val can be merged with the left interval
        merged_left = left >= 0 and intervals[left][1] + 1 >= val
        # Check if val can be merged with the right interval
        merged_right = right < len(intervals) and intervals[right][0] - 1 <= val
        
        if merged_left and merged_right:
            # Bridge the gap between left and right intervals
            intervals[left][1] = intervals[right][1]
            intervals.pop(right)
        elif merged_left:
            # Extend the left interval
            intervals[left][1] = max(intervals[left][1], val)
        elif merged_right:
            # Extend the right interval
            intervals[right][0] = min(intervals[right][0], val)
        else:
            # Insert as a new standalone interval
            intervals.insert(i, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
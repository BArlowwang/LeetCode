# python 3
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        lst = []
        for i in intervals:
            if lst and lst[-1].end >= i.start:
                lst[-1].end = max(lst[-1].end, i.end)
            else:
                lst.append(i)
        return lst

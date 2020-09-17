# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        return_list = []
        intervals_list_length = len(intervals)
        new_return_interval = []

        # Case 1: If the given list is empty.
        if intervals_list_length == 0:
            return_list.append(newInterval)
            pass

        # Case 2: if new interval is entirely less than the numbers in the given list.
        elif newInterval[1] < intervals[0][0]:
            return_list.append(newInterval)
            for interval in intervals:
                return_list.append(interval)

        # Case 3: if new interval is entirely more than the numbers in the given list.
        elif newInterval[0] > intervals[intervals_list_length - 1][1]:
            for interval in intervals:
                return_list.append(interval)
            return_list.append(newInterval)

        # Case 4: if new interval is wider than the entire given list.
        elif newInterval[0] <= intervals[0][0] and newInterval[1] >= intervals[intervals_list_length - 1][1]:
            return_list.append(newInterval)

        # Case 5: if new interval starts before or within given list and ends within or beyond given list.
        else:
            # if new interval starts before given list.
            if newInterval[0] < intervals[0][0]:
                new_return_interval.append(newInterval[0])
            # iterate through intervals in list
            for i, interval in enumerate(intervals):
                if len(new_return_interval) == 0:
                    first_interval = self.new_first_interval(newInterval, i, interval, intervals)
                    if first_interval is not None:
                        if first_interval > interval[1]:
                            return_list.append(interval)
                        new_return_interval.append(first_interval)
                    # Otherwise, the new interval is not within the iterated interval
                    # and it should be added to the return list.
                    else:
                        return_list.append(interval)

                if len(new_return_interval) == 1:
                    last_interval = self.new_last_interval(newInterval, i, interval, intervals)
                    if last_interval:
                        new_return_interval.append(last_interval)
                        return_list.append(new_return_interval)
                        continue

                # Add any intervals after the end of new_return_interval to the end of the return list.
                if len(new_return_interval) == 2 and new_return_interval in return_list:
                    return_list.append(interval)

            # If the new interval ends beyond the scope of the given list.
            if len(new_return_interval) == 1:
                new_return_interval.append(newInterval[1])
                return_list.append(new_return_interval)

        return return_list

    def new_first_interval(self, newInterval, i, interval, intervals):
        new_first_interval = None
        # If new interval starts within the iterated interval,
        # return the min of the iterated interval as the start of the new return interval.
        if newInterval[0] in range(interval[0], interval[1] + 1):
            new_first_interval = interval[0]
        # If this is not the last iterated interval in the list and
        # the new interval starts between this iterated interval and the next,
        # return the min of the new interval as the start of the new return interval.
        elif i < len(intervals) - 1 and newInterval[0] in range(interval[1], intervals[i + 1][0]):
            new_first_interval = newInterval[0]

        return new_first_interval

    def new_last_interval(self, newInterval, i, interval, intervals):
        new_last_interval = False
        # If the new interval ends within the range of this iterated interval,
        # complete the new return interval with the end of this iterated interval.
        if newInterval[1] in range(interval[0], interval[1]):
            new_last_interval = interval[1]
        # If the new interval ends between the range of this iterated interval and the start of the next,
        # complete the new return interval with the end of the new interval.
        elif i < len(intervals) - 1 and newInterval[1] in range(interval[1], intervals[i + 1][0]):
            new_last_interval = newInterval[1]

        return new_last_interval


s = Solution()
s.insert([[0,5],[9,12]], [7,16])
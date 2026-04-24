# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] should return [[1,3],[4,5],[6,9]] because the new interval [4,5] does not overlap with the existing intervals. However, for intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] and newInterval = [4,8], the output should be [[1,2],[3,10],[12,16]] because the new interval [4,8] overlaps with the intervals [3,5] and [6,7] and [8,10].

## Approach
The algorithm iterates through the intervals and checks for overlap with the new interval. If an overlap is found, it merges the intervals. The algorithm uses a start and end pointer to track the position of the new interval in the list of intervals. The time complexity of this solution is O(n), where n is the number of intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> result;
    int i = 0;
    // Add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // Merge all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    // Add the new interval
    result.push_back(newInterval);
    // Add all remaining intervals
    while (i < intervals.size()) {
        result.push_back(intervals[i]);
        i++;
    }
    return result;
}
```

## Test Cases
```
Input: intervals = [[1,3],[6,9]], newInterval = [4,5]
Output: [[1,3],[4,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The algorithm has a time complexity of O(n), where n is the number of intervals.
- The algorithm uses a start and end pointer to track the position of the new interval in the list of intervals.
- The algorithm merges overlapping intervals by updating the start and end of the new interval.
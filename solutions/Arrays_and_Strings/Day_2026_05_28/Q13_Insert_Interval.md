# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] will result in [[1,3],[4,5],[6,9]]. If the new interval overlaps with any existing intervals, they should be merged. For instance, intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] and newInterval = [4,8] will result in [[1,2],[3,10],[12,16]]. The input intervals are non-overlapping and the start time is less than or equal to the end time.

## Approach
The algorithm iterates over the intervals to find the position where the new interval should be inserted. If the new interval overlaps with any existing intervals, they are merged. The algorithm uses a simple iterative approach to solve the problem in linear time complexity.

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
    // add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // merge all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    // add the new interval
    result.push_back(newInterval);
    // add all remaining intervals
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
- The algorithm iterates over the intervals to find the position where the new interval should be inserted.
- If the new interval overlaps with any existing intervals, they are merged by updating the start and end times of the new interval.
- The algorithm uses a simple iterative approach to solve the problem in linear time complexity.
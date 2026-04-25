# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]], and the new interval to be inserted is [2,5]. The output should be [[1,5],[6,9]]. If the new interval is [0,0], the output should be [[0,0],[1,3],[6,9]]. If the new interval is [10,12], the output should be [[1,3],[6,9],[10,12]]. The intervals array can contain up to 1000 intervals, and the new interval will always have a length of 2.

## Approach
The algorithm involves iterating through the existing intervals and merging the new interval if it overlaps with any of them. We use a two-pointer technique to track the current position in the intervals array and the new interval. If the new interval does not overlap with the current interval, we add the current interval to the result array.

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
        newInterval[0] = min(intervals[i][0], newInterval[0]);
        newInterval[1] = max(intervals[i][1], newInterval[1]);
        i++;
    }
    // add the merged interval
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
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- Use a two-pointer technique to track the current position in the intervals array and the new interval.
- Merge overlapping intervals by updating the start and end times of the new interval.
- Add non-overlapping intervals to the result array.
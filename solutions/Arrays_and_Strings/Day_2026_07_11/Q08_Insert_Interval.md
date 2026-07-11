# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] would result in [[1,3],[4,5],[6,9]], but newInterval = [2,6] would result in [[1,6],[9,10]] if the original list was [[1,3],[6,10]]. The intervals array is not guaranteed to be sorted after the insertion.

## Approach
We will iterate over the intervals array and add all intervals that come before the new interval. Then, we will merge the new interval with all overlapping intervals. Finally, we will add the merged interval and all remaining intervals to the result.

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
    // merge the new interval with all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
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
- Use a two-pointer technique to iterate over the intervals array.
- Merge overlapping intervals by updating the start and end times of the new interval.
- Add non-overlapping intervals to the result array.
# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as a collection of intervals where intervals[i] = [start, end]. The input interval is guaranteed to be non-empty. The intervals are non-overlapping, meaning that for any two intervals [a, b] and [c, d], either b < c or d < a. The start and end of the interval are integers.

## Approach
We iterate through the list of intervals and insert the new interval when we find the correct position. If the new interval overlaps with an existing interval, we merge them. The algorithm continues until all intervals have been processed.

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
    // Merge all overlapping intervals to the new interval
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
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The time complexity is linear because we process each interval once.
- We use a result vector to store the merged intervals, so the space complexity is also linear.
- The algorithm handles cases where the new interval does not overlap with any existing intervals, or where it overlaps with one or more existing intervals.
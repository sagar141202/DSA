# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of pairs of integers, where each pair represents an interval. The new interval to be inserted is also given as a pair of integers. The function should return a list of merged intervals. For example, given intervals = [[1,3],[6,9]] and newInterval = [2,5], the function should return [[1,5],[6,9]]. If the new interval is outside the existing intervals, it should be added to the result. If the new interval overlaps with one or more existing intervals, the overlapping intervals should be merged into a single interval.

## Approach
The algorithm involves iterating over the existing intervals and checking for overlap with the new interval. If an overlap is found, the new interval is merged with the overlapping interval. The algorithm uses a vector to store the merged intervals and returns the vector at the end. The time complexity is O(n), where n is the number of intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
    // Add the merged interval
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
- The algorithm iterates over the existing intervals to find overlapping intervals.
- The new interval is merged with overlapping intervals by updating its start and end values.
- The merged interval is added to the result vector, along with non-overlapping intervals.
# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] would result in [[1,3],[4,5],[6,9]]. However, if newInterval = [2,5], the output would be [[1,5],[6,9]] because the new interval overlaps with the existing interval [1,3].

## Approach
The algorithm iterates through the existing intervals to find the correct position for the new interval. It merges the new interval with the existing intervals if they overlap. The merged interval is then inserted into the list of intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    // Initialize result vector
    vector<vector<int>> result;
    
    // Initialize index
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
Input: intervals = [[1,3],[6,9]], newInterval = [4,5]
Output: [[1,3],[4,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The algorithm has a linear time complexity because it only needs to iterate through the list of intervals once.
- The space complexity is also linear because in the worst case, the result vector will contain all the intervals from the input.
- The algorithm assumes that the input intervals are non-overlapping and sorted by their start times.
# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] would result in [[1,3],[4,5],[6,9]]. If the new interval overlaps with existing intervals, merge them into a single interval. For instance, intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] and newInterval = [4,8] would result in [[1,2],[3,10],[12,16]].

## Approach
The approach involves iterating through the given intervals and checking for overlap with the new interval. If an overlap is found, the new interval is merged with the overlapping interval. The algorithm maintains a list of non-overlapping intervals. The time complexity of this solution is O(n), where n is the number of intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    // Initialize an empty vector to store the result
    vector<vector<int>> result;
    
    // Initialize the index to track the current position in the intervals vector
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
    
    // Add all remaining intervals to the result
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
- The algorithm iterates through the intervals to find the position where the new interval should be inserted.
- It merges overlapping intervals to the new interval.
- The solution has a time complexity of O(n), where n is the number of intervals.
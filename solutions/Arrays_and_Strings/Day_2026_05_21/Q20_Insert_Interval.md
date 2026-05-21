# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]], and the new interval is [2,5], the output will be [[1,5],[6,9]]. If the new interval is [0,0], the output will be [[0,0],[1,3],[6,9]].

## Approach
We iterate through the given intervals and check if the new interval overlaps with the current interval. If it does, we merge them by updating the start and end times of the new interval. If not, we add the current interval to the result and continue with the next interval.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
        
        // Add all remaining intervals to the output
        while (i < intervals.size()) {
            result.push_back(intervals[i]);
            i++;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- We iterate through the intervals to find the position where the new interval should be inserted.
- We merge all overlapping intervals to the new interval by updating its start and end times.
- We add the new interval and the remaining intervals to the result.
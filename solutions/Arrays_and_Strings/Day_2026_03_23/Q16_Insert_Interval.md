# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] should return [[1,3],[4,5],[6,9]]. If the new interval overlaps with any existing intervals, the overlapping parts should be merged. For instance, intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] and newInterval = [4,8] should return [[1,2],[3,10],[12,16]].

## Approach
The algorithm involves iterating through the given intervals and inserting the new interval at the correct position. If the new interval overlaps with any existing interval, it merges them by updating the start and end times of the new interval. The process continues until all intervals have been processed, resulting in a merged set of non-overlapping intervals. The solution utilizes a vector to store the merged intervals and iterates through the given intervals to find the correct position for the new interval.

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
        // Add all intervals that come before the 'newInterval'
        while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        // Merge all overlapping intervals to the 'newInterval'
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        // Add the 'newInterval'
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
Input: intervals = [[1,3],[6,9]], newInterval = [4,5]
Output: [[1,3],[4,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The solution iterates through the given intervals to find the correct position for the new interval.
- It merges overlapping intervals by updating the start and end times of the new interval.
- The resulting merged intervals are stored in a vector and returned as the output.
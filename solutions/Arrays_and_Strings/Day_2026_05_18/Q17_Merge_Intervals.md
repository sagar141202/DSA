# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array contains two integers representing the start and end of an interval. The intervals are not guaranteed to be sorted. The task is to merge all overlapping intervals and return the merged intervals. For example, given intervals [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The input intervals are non-empty and the start of each interval is less than or equal to its end.

## Approach
The algorithm sorts the intervals based on their start value, then iterates over the sorted intervals, merging any overlapping intervals. If the current interval overlaps with the last merged interval, it merges them by updating the end of the last merged interval. If not, it adds the current interval to the list of merged intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // If the input is empty, return an empty vector
        if (intervals.empty()) {
            return {};
        }
        
        // Sort the intervals based on their start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged = {intervals[0]};
        
        // Iterate over the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last merged interval
            vector<int>& lastMerged = merged.back();
            
            // If the current interval overlaps with the last merged interval, merge them
            if (intervals[i][0] <= lastMerged[1]) {
                lastMerged[1] = max(lastMerged[1], intervals[i][1]);
            } else {
                // If not, add the current interval to the list of merged intervals
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};
```

## Test Cases
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Input: [[1,4],[4,5]]
Output: [[1,5]]
Input: []
Output: []
```

## Key Takeaways
- Sort the intervals based on their start value before merging to ensure correct merging.
- Use a separate vector to store the merged intervals to avoid modifying the original input.
- Check for overlapping intervals by comparing the start of the current interval with the end of the last merged interval.
# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each subarray contains two integers representing the start and end of an interval. The input array is sorted based on the start time of the intervals. The task is to merge the overlapping intervals and return the merged intervals. For example, if the input is [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]].

## Approach
The algorithm sorts the intervals based on their start time and then iterates over the sorted intervals, merging any overlapping intervals it finds. If the current interval does not overlap with the previous one, it is added to the result list. The process continues until all intervals have been processed.

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

        // Sort the intervals based on their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result vector with the first interval
        vector<vector<int>> merged = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval in the result vector
            vector<int>& last = merged.back();

            // Check if the current interval overlaps with the last interval
            if (intervals[i][0] <= last[1]) {
                // Merge the current interval with the last interval
                last[1] = max(last[1], intervals[i][1]);
            } else {
                // Add the current interval to the result vector
                merged.push_back(intervals[i]);
            }
        }

        // Return the merged intervals
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
- Sort the intervals based on their start time to ensure that overlapping intervals are adjacent in the sorted array.
- Initialize the result vector with the first interval and then iterate over the remaining intervals, merging any overlapping intervals.
- Use a variable to keep track of the last interval in the result vector to check for overlaps and merge intervals efficiently.
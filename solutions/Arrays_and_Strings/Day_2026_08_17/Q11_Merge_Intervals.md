# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array contains two integers representing the start and end of an interval. The input array is sorted based on the start time of the intervals. The task is to merge the overlapping intervals and return the merged intervals. For example, if the input is [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The intervals [1,3] and [2,6] overlap, so they are merged into [1,6]. The intervals [8,10] and [15,18] do not overlap with any other intervals, so they remain the same.

## Approach
The algorithm sorts the intervals based on their start time and then iterates over the sorted intervals, merging any overlapping intervals it finds. The merged intervals are stored in a separate array. The algorithm uses a simple iterative approach to solve the problem efficiently.

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
        // If the input array is empty, return an empty array
        if (intervals.empty()) {
            return {};
        }

        // Sort the intervals based on their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the merged array with the first interval
        vector<vector<int>> merged = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last merged interval
            vector<int>& lastMerged = merged.back();

            // If the current interval overlaps with the last merged interval, merge them
            if (intervals[i][0] <= lastMerged[1]) {
                lastMerged[1] = max(lastMerged[1], intervals[i][1]);
            } else {
                // Otherwise, add the current interval to the merged array
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
- Sort the intervals based on their start time to ensure that overlapping intervals are adjacent in the array.
- Use a separate array to store the merged intervals to avoid modifying the input array.
- Iterate over the sorted intervals and merge any overlapping intervals to obtain the final merged intervals.
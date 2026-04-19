# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array contains two integers representing the start and end of an interval. The function should return a new 2D array where all overlapping intervals are merged. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the function should return `[[1,6],[8,10],[15,18]]`. The intervals are sorted based on their start time.

## Approach
The approach is to sort the intervals based on their start time and then iterate over them, merging any overlapping intervals. If the current interval overlaps with the last merged interval, we merge them by updating the end time of the last merged interval. If not, we add the current interval to the list of merged intervals.

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
        // Sort the intervals based on their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If the list of merged intervals is empty or if the current interval does not overlap with the last merged interval, append it
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Otherwise, there is overlap, so we merge the current and last merged interval
                merged.back()[1] = max(merged.back()[1], interval[1]);
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
- Sort the intervals based on their start time to ensure that we can merge overlapping intervals in a single pass.
- Use a separate list to store the merged intervals to avoid modifying the original list of intervals.
- Check for overlap by comparing the end time of the last merged interval with the start time of the current interval.
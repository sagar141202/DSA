# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals and return the resulting merged intervals. The intervals are represented as vectors of two integers, start and end. For example, `[[1,3],[2,6],[8,10],[15,18]]` should return `[[1,6],[8,10],[15,18]]`. The input intervals are not guaranteed to be sorted, and the output intervals should not overlap. If there are no intervals to merge, the function should return an empty vector.

## Approach
The approach involves sorting the intervals based on their start time, then iterating over them to merge any overlapping intervals. This is done by comparing the end time of the last merged interval with the start time of the current interval. If the current interval overlaps with the last merged interval, their end times are updated. Otherwise, the current interval is added to the list of merged intervals.

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
        // If the input vector is empty, return an empty vector
        if (intervals.empty()) return {};

        // Sort the intervals based on their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result vector with the first interval
        vector<vector<int>> merged = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last merged interval
            vector<int>& lastMerged = merged.back();

            // If the current interval overlaps with the last merged interval, merge them
            if (intervals[i][0] <= lastMerged[1]) {
                lastMerged[1] = max(lastMerged[1], intervals[i][1]);
            } else {
                // Otherwise, add the current interval to the list of merged intervals
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
- Sorting the intervals based on their start time is crucial for the merging process.
- The time complexity of the solution is O(n log n) due to the sorting step.
- The space complexity is O(n) as we need to store the merged intervals in a separate vector.
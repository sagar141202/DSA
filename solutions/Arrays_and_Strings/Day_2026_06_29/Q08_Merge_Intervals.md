# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as vectors of two integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. The intervals are sorted based on their start time. The task is to merge the overlapping intervals and return the merged intervals. For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], the merged intervals will be [[1,6],[8,10],[15,18]]. The constraints are that the number of intervals is between 0 and 1000, and the start and end times of the intervals are between 0 and 1000000.

## Approach
The approach to solve this problem is to use a greedy algorithm, where we sort the intervals based on their start time and then iterate through the sorted intervals, merging any overlapping intervals. We will use a vector to store the merged intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // If the input vector is empty, return an empty vector
    if (intervals.empty()) {
        return {};
    }

    // Sort the intervals based on their start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Initialize the merged vector with the first interval
    vector<vector<int>> merged = {intervals[0]};

    // Iterate through the remaining intervals
    for (int i = 1; i < intervals.size(); i++) {
        // Get the last merged interval
        vector<int>& lastMerged = merged.back();

        // If the current interval overlaps with the last merged interval, merge them
        if (intervals[i][0] <= lastMerged[1]) {
            lastMerged[1] = max(lastMerged[1], intervals[i][1]);
        } else {
            // Otherwise, add the current interval to the merged vector
            merged.push_back(intervals[i]);
        }
    }

    return merged;
}
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
- Use a greedy algorithm to merge the intervals, where we always try to merge the current interval with the last merged interval.
- If the current interval does not overlap with the last merged interval, add it to the merged vector as a new interval.
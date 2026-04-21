# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers representing the start and end of an interval. The input intervals are not guaranteed to be sorted. The goal is to return a new vector with the merged intervals. For example, if the input is `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. If the input is `[[1,4],[4,5]]`, the output should be `[[1,5]]`.

## Approach
The approach involves sorting the intervals based on their start value, then iterating over the sorted intervals and merging any overlapping intervals. This is done by checking if the current interval overlaps with the last merged interval. If they overlap, the last merged interval is updated to be the merged version of the two intervals.

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

    // Sort the intervals based on their start value
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Initialize the result vector with the first interval
    vector<vector<int>> merged = {intervals[0]};

    // Iterate over the remaining intervals
    for (int i = 1; i < intervals.size(); i++) {
        // Get the last merged interval
        vector<int>& lastMerged = merged.back();

        // Check if the current interval overlaps with the last merged interval
        if (intervals[i][0] <= lastMerged[1]) {
            // Merge the current interval with the last merged interval
            lastMerged[1] = max(lastMerged[1], intervals[i][1]);
        } else {
            // Add the current interval to the result vector
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
Input: [[1,2]]
Output: [[1,2]]
```

## Key Takeaways
- Sort the intervals based on their start value to ensure that overlapping intervals are adjacent in the sorted vector.
- Use a result vector to store the merged intervals, and update the last merged interval if a new interval overlaps with it.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for the result vector.
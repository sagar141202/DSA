# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as vectors of two integers, where the first integer is the start of the interval and the second integer is the end of the interval. If two intervals have at least one common point, they are considered overlapping. The function should return a vector of merged intervals, where each interval is a vector of two integers. For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], the function should return [[1,6],[8,10],[15,18]]. The input intervals are not guaranteed to be sorted, and the input vector can be empty.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged correctly. The time complexity is dominated by the sorting step. The space complexity is determined by the storage needed for the output.

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
        if (intervals.empty()) {
            return {};
        }

        // Sort the intervals based on their start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result vector with the first interval
        vector<vector<int>> result = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval in the result vector
            vector<int>& lastInterval = result.back();

            // If the current interval overlaps with the last interval, merge them
            if (intervals[i][0] <= lastInterval[1]) {
                lastInterval[1] = max(lastInterval[1], intervals[i][1]);
            } else {
                // Otherwise, add the current interval to the result vector
                result.push_back(intervals[i]);
            }
        }

        return result;
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
- Sort the intervals based on their start value to ensure correct merging.
- Use a result vector to store the merged intervals, starting with the first interval.
- Iterate over the remaining intervals, merging any overlapping intervals with the last interval in the result vector.
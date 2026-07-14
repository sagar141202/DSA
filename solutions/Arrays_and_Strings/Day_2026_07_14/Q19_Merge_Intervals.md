# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector of integers, where each sub-vector contains two integers representing the start and end of an interval. The goal is to merge all overlapping intervals into non-overlapping intervals. For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The input intervals are not guaranteed to be sorted, and the intervals can be empty.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. If the current interval overlaps with the last merged interval, the end value of the last merged interval is updated. Otherwise, the current interval is added to the list of merged intervals.

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
        if (intervals.empty()) return {};

        // Sort the intervals based on their start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result with the first interval
        vector<vector<int>> result = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last merged interval
            vector<int>& lastMerged = result.back();

            // Check if the current interval overlaps with the last merged interval
            if (intervals[i][0] <= lastMerged[1]) {
                // Merge the current interval with the last merged interval
                lastMerged[1] = max(lastMerged[1], intervals[i][1]);
            } else {
                // Add the current interval to the result
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
- Sort the intervals based on their start value to ensure that overlapping intervals are adjacent.
- Use a result vector to store the merged intervals, and update the last merged interval if the current interval overlaps with it.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the result vector.
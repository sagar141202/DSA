# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array has two elements, the start and end of the interval. The goal is to combine all overlapping intervals into non-overlapping intervals, returning the merged list of intervals. For example, given `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. The input intervals are guaranteed to be valid (i.e., the start of each interval is less than or equal to its end), and the intervals are not guaranteed to be sorted.

## Approach
The algorithm involves sorting the intervals by their start value and then iterating through the sorted intervals to merge any overlapping intervals. If the current interval overlaps with the last merged interval, the end of the last merged interval is updated. Otherwise, the current interval is added to the list of merged intervals.

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

        // Sort the intervals by their start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        // Initialize the result with the first interval
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
- Sorting the intervals by their start value is crucial for the algorithm to work correctly.
- The algorithm has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for storing the merged intervals.
- The algorithm iterates over the intervals only once after sorting, making it efficient for large inputs.
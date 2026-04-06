# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a collection of pairs of integers, where each pair represents the start and end of an interval. The goal is to return a new collection of intervals where all overlapping intervals are merged. For example, given the intervals [(1,3), (2,6), (8,10), (15,18)], the merged intervals would be [(1,6), (8,10), (15,18)]. The input intervals are not guaranteed to be sorted, and the output intervals should be sorted by their start value.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged in a single pass. The sorting step has a time complexity of O(n log n), and the merging step has a time complexity of O(n).

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

        // Initialize the result with the first interval
        vector<vector<int>> result = {intervals[0]};

        // Iterate over the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval in the result
            vector<int>& lastInterval = result.back();

            // If the current interval overlaps with the last interval, merge them
            if (intervals[i][0] <= lastInterval[1]) {
                lastInterval[1] = max(lastInterval[1], intervals[i][1]);
            } else {
                // Otherwise, add the current interval to the result
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
- Sorting the intervals based on their start value is crucial for the merging step to work correctly.
- The merging step has a time complexity of O(n), making the overall algorithm efficient for large inputs.
- The algorithm assumes that the input intervals are valid (i.e., the start value is less than or equal to the end value).
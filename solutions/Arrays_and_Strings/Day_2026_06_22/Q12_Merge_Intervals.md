# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array is an interval with a start and end value. The goal is to return a new array of merged intervals. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. The input intervals are not guaranteed to be sorted, and the output intervals should not have any overlap.

## Approach
The approach involves sorting the intervals based on their start value and then iterating through the sorted intervals to merge any overlapping intervals. This is done by comparing the end value of the last merged interval with the start value of the current interval. If they overlap, the end value of the last merged interval is updated. If they do not overlap, a new merged interval is added.

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
        // Sort the intervals based on their start value
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        for (auto& interval : intervals) {
            // If the merged vector is empty or the current interval does not overlap with the last merged interval
            if (merged.empty() || merged.back()[1] < interval[0]) {
                // Add the current interval to the merged vector
                merged.push_back(interval);
            } else {
                // Merge the current interval with the last merged interval
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
- Sort the intervals based on their start value to ensure that overlapping intervals are adjacent.
- Use a separate vector to store the merged intervals to avoid modifying the original input.
- Compare the end value of the last merged interval with the start value of the current interval to determine if they overlap.
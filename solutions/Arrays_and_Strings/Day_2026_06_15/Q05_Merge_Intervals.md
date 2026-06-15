# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array has two elements representing the start and end of an interval. The intervals are not guaranteed to be sorted. The task is to merge the overlapping intervals and return the merged intervals as a 2D array. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. If there are no overlapping intervals, the original intervals should be returned.

## Approach
The algorithm sorts the intervals based on their start values and then iterates through the sorted intervals, merging any overlapping intervals it finds. This approach ensures that all overlapping intervals are merged correctly. The sorting step has a time complexity of O(n log n), and the iteration step has a time complexity of O(n).

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
        // Sort the intervals based on their start values
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If the merged vector is empty or the current interval does not overlap with the last merged interval, append it
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Otherwise, merge the current interval with the last merged interval
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
- Sorting the intervals based on their start values is crucial for the merging process.
- The merging process can be done in a single pass through the sorted intervals.
- The time complexity of the solution is dominated by the sorting step, which has a time complexity of O(n log n).
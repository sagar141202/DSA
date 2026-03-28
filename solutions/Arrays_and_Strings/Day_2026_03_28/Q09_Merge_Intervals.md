# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers, start and end, representing an interval. The goal is to merge all overlapping intervals and return the resulting merged intervals. For example, given [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The intervals are assumed to be non-empty and the start value of each interval is less than or equal to the end value.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. If the current interval does not overlap with the previous one, it is added to the result list. This approach ensures that all overlapping intervals are merged efficiently.

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
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If the merged list is empty or the current interval does not overlap with the previous one, add it to the merged list
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Merge the current interval with the previous one
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
```

## Key Takeaways
- Sort the intervals based on their start value to ensure efficient merging.
- Iterate over the sorted intervals and merge any overlapping intervals to minimize the number of iterations.
- Use a separate list to store the merged intervals to avoid modifying the original list.
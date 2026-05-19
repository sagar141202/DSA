# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a collection of pairs of integers, where each pair represents the start and end of an interval. The input intervals are guaranteed to be non-empty and are sorted based on their start value. The task is to merge the overlapping intervals and return the merged intervals. For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The intervals [1,3] and [2,6] overlap, so they are merged into [1,6]. The intervals [8,10] and [15,18] do not overlap with any other intervals, so they remain unchanged.

## Approach
The approach to solve this problem is to iterate through the intervals and check if the current interval overlaps with the last merged interval. If they overlap, merge them by updating the end of the last merged interval. If they do not overlap, add the current interval to the list of merged intervals. This process continues until all intervals have been processed.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Sort the intervals based on their start value
    sort(intervals.begin(), intervals.end());
    
    vector<vector<int>> merged;
    for (auto interval : intervals) {
        // If the list of merged intervals is empty or the current interval does not overlap with the last merged interval, append it
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        } else {
            // Otherwise, merge the current and last merged interval
            merged.back()[1] = max(merged.back()[1], interval[1]);
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
```

## Key Takeaways
- The key to solving this problem is to sort the intervals based on their start value.
- The time complexity of the solution is O(n log n) due to the sorting, where n is the number of intervals.
- The space complexity of the solution is O(n), where n is the number of intervals.
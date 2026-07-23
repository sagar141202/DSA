# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as vectors of two integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. The goal is to return a new collection of non-overlapping intervals. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. The input intervals are not guaranteed to be sorted, and the output intervals should be sorted by their start value.

## Approach
The algorithm sorts the intervals by their start value and then iterates through the sorted intervals, merging any overlapping intervals. If the current interval overlaps with the last merged interval, the two intervals are merged by updating the end of the last merged interval. If the current interval does not overlap with the last merged interval, it is added to the list of merged intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Sort the intervals by their start value
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    vector<vector<int>> merged;
    for (const auto& interval : intervals) {
        // If the list of merged intervals is empty or the current interval does not overlap with the last merged interval, add it to the list
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        } else {
            // Merge the current interval with the last merged interval
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
Input: []
Output: []
```

## Key Takeaways
- Sort the intervals by their start value to ensure that overlapping intervals are adjacent in the sorted list.
- Use a list to store the merged intervals, and iterate through the sorted intervals to merge any overlapping intervals.
- Update the end of the last merged interval if the current interval overlaps with it, or add the current interval to the list if it does not overlap.
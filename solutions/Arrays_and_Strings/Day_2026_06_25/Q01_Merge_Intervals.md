# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector of integers, where each interval is a pair of integers representing the start and end of the interval. The function should return a new 2D vector with the merged intervals. For example, given `[[1,3],[2,6],[8,10],[15,18]]`, the function should return `[[1,6],[8,10],[15,18]]`. The input intervals are non-empty and the start of each interval is less than or equal to its end.

## Approach
The algorithm sorts the intervals by their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that the merged intervals are also sorted. The key insight is that if the current interval overlaps with the last merged interval, they can be merged by updating the end of the last merged interval.

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
```

## Test Cases
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: [[1,4],[4,5]]
Output: [[1,5]]
```

## Key Takeaways
- Sort the intervals by their start value to ensure that overlapping intervals are adjacent.
- Use a separate vector to store the merged intervals to avoid modifying the input vector.
- Merge overlapping intervals by updating the end of the last merged interval.
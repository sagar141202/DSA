# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector of integers, where each interval is a pair of integers representing the start and end of the interval. The function should return a new 2D vector of merged intervals. For example, given the input `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. The input intervals are not guaranteed to be sorted, and the intervals may overlap.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that the intervals are processed in a consistent order, allowing for efficient merging. The time complexity is optimized by using a sorting algorithm with a time complexity of O(n log n).

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
    // Sort the intervals based on their start value
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
Input: []
Output: []
```

## Key Takeaways
- Sorting the intervals based on their start value allows for efficient merging.
- Using a vector to store the merged intervals allows for dynamic resizing and efficient insertion of new intervals.
- The algorithm has a time complexity of O(n log n) due to the sorting step, making it efficient for large inputs.
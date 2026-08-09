# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers representing the start and end of an interval. The input intervals are guaranteed to be non-empty and the start of each interval is less than or equal to its end. The goal is to return a new vector of non-overlapping intervals after merging all overlapping intervals. For example, given the input `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged efficiently. The sorting step allows for a simple iteration to merge overlapping intervals. The time complexity of this approach is dominated by the sorting step.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Sort the intervals based on their start value
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    vector<vector<int>> merged;
    for (const auto& interval : intervals) {
        // If the list of merged intervals is empty or if the current interval does not overlap with the previous, append it
        if (merged.empty() || merged.back()[1] < interval[0]) {
            merged.push_back(interval);
        } else {
            // Otherwise, there is overlap, so we merge the current and previous intervals
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
- Sorting the intervals by their start value allows for efficient merging of overlapping intervals.
- The merge step has a linear time complexity after sorting, making the overall algorithm efficient for large inputs.
- This problem demonstrates the importance of considering the order of elements when solving problems involving intervals or ranges.
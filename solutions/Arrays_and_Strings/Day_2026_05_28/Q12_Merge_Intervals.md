# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as vectors of two integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. The input intervals are guaranteed to be non-empty and the start of each interval is less than or equal to the end of the interval. If an interval overlaps with another, they should be merged into a single interval. For example, given intervals [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The input intervals are not guaranteed to be sorted.

## Approach
The approach to solve this problem is to first sort the intervals based on their start time. Then, we iterate through the sorted intervals and check if the current interval overlaps with the previous one. If they overlap, we merge them by updating the end time of the previous interval. If they do not overlap, we add the current interval to the result.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // Sort the intervals based on their start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    vector<vector<int>> result;
    for (const auto& interval : intervals) {
        // If the result is empty or the current interval does not overlap with the last interval in the result, add it to the result
        if (result.empty() || result.back()[1] < interval[0]) {
            result.push_back(interval);
        } else {
            // Merge the current interval with the last interval in the result
            result.back()[1] = max(result.back()[1], interval[1]);
        }
    }
    return result;
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
- Sort the intervals based on their start time to ensure that we can merge overlapping intervals in a single pass.
- Use a result vector to store the merged intervals, and update the end time of the last interval in the result if the current interval overlaps with it.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the result.
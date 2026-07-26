# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals and return the result. The intervals are represented as vectors of two integers, where the first integer is the start of the interval and the second integer is the end of the interval. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the merged intervals would be `[[1,6],[8,10],[15,18]]`. The input intervals are not guaranteed to be sorted, and the intervals may overlap in any order.

## Approach
The algorithm sorts the intervals by their start time and then iterates over the sorted intervals. If the current interval overlaps with the previous one, it merges them by updating the end time of the previous interval. If the current interval does not overlap with the previous one, it adds the current interval to the result.

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
        // Sort the intervals by their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        vector<vector<int>> result;
        for (const auto& interval : intervals) {
            // If the result is empty or the current interval does not overlap with the last interval in the result
            if (result.empty() || result.back()[1] < interval[0]) {
                result.push_back(interval);
            } else {
                // Merge the current interval with the last interval in the result
                result.back()[1] = max(result.back()[1], interval[1]);
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
- Sort the intervals by their start time to ensure that we can merge overlapping intervals in a single pass.
- Use a vector to store the merged intervals, and update the end time of the last interval in the result if the current interval overlaps with it.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the merged intervals.
# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers representing the start and end of an interval. The intervals are not guaranteed to be sorted. For example, if we have intervals [[1,3],[2,6],[8,10],[15,18]], the merged intervals would be [[1,6],[8,10],[15,18]]. The input intervals are non-empty and the start of each interval is less than or equal to its end.

## Approach
The algorithm first sorts the intervals based on their start time. Then it iterates over the sorted intervals, merging any overlapping intervals. If the current interval does not overlap with the last merged interval, it is added to the list of merged intervals. The key to this solution is to maintain a list of merged intervals and update it as we iterate over the input intervals.

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

        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If the merged list is empty or the current interval does not overlap with the last merged interval, append it
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Otherwise, merge the current and last merged interval
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
- Sort the intervals by their start time before merging to ensure that we can merge overlapping intervals in a single pass.
- Keep track of the last merged interval to determine whether the current interval overlaps with it.
- Update the end of the last merged interval if the current interval overlaps with it, or append the current interval to the list of merged intervals if it does not overlap.
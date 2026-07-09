# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. An interval is represented as an array of two integers, where the first integer is the start of the interval and the second integer is the end of the interval. The intervals are non-empty and may not be distinct. The start of an interval may be larger than its end, but this is still considered a valid interval. For example, [1, 2] and [2, 3] can be merged into [1, 3]. However, [1, 2] and [3, 4] cannot be merged. The input intervals are sorted based on their start value.

## Approach
The algorithm sorts the intervals based on their start value and then iterates through the sorted intervals, merging any overlapping intervals. If the current interval overlaps with the last merged interval, the two intervals are merged by updating the end of the last merged interval. The approach ensures that all overlapping intervals are merged efficiently.

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
            // If the merged vector is empty or the current interval does not overlap with the last merged interval
            if (merged.empty() || merged.back()[1] < interval[0]) {
                // Add the current interval to the merged vector
                merged.push_back(interval);
            } else {
                // Merge the current interval with the last merged interval
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        
        return merged;
    }
};
```

## Test Cases
```
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]

Input: [[1, 4], [4, 5]]
Output: [[1, 5]]
```

## Key Takeaways
- The problem can be solved by sorting the intervals based on their start value and then merging any overlapping intervals.
- The time complexity of the solution is O(n log n) due to the sorting operation.
- The space complexity of the solution is O(n) for storing the merged intervals.
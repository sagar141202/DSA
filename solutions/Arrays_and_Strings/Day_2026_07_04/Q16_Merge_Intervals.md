# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a list of pairs, where each pair contains two integers representing the start and end of an interval. The input intervals are guaranteed to be non-empty and the start value of each interval is less than or equal to the end value. The goal is to return a new list of merged intervals.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged in a single pass. The key intuition is to maintain a list of merged intervals and update this list as we iterate over the input intervals.

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
            // If the merged list is empty or the current interval does not overlap with the last merged interval, append it
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                // Otherwise, merge the current interval with the last merged interval
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
- Sort the intervals based on their start value to ensure that we can merge overlapping intervals in a single pass.
- Maintain a list of merged intervals and update this list as we iterate over the input intervals.
- Use a conditional statement to check if the current interval overlaps with the last merged interval and merge them if necessary.
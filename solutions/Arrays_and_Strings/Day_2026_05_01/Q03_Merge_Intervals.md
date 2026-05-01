# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers representing the start and end of an interval. The input intervals are guaranteed to be non-empty and the start of each interval is less than or equal to its end. The intervals are not guaranteed to be sorted. The task is to merge the intervals and return the merged intervals as a 2D vector. For example, given the input `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`.

## Approach
The approach is to first sort the intervals based on their start value. Then, iterate through the sorted intervals and merge any overlapping intervals. This can be achieved by maintaining a result vector and adding or merging intervals to it based on whether the current interval overlaps with the last interval in the result vector.

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
        // Sort the intervals based on the start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        vector<vector<int>> result;
        for (const auto& interval : intervals) {
            // If the result vector is empty or the current interval does not overlap with the last interval in the result vector, add it to the result vector
            if (result.empty() || result.back()[1] < interval[0]) {
                result.push_back(interval);
            } else {
                // Merge the current interval with the last interval in the result vector
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
- Sort the intervals based on their start value to ensure that overlapping intervals are adjacent.
- Use a result vector to store the merged intervals and avoid modifying the original intervals vector.
- Iterate through the sorted intervals and merge any overlapping intervals by updating the end value of the last interval in the result vector.
# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array is a pair of integers representing the start and end of an interval. For example, `[[1, 3], [2, 6], [8, 10], [15, 18]]` represents four intervals: `(1, 3)`, `(2, 6)`, `(8, 10)`, and `(15, 18)`. The task is to merge these intervals into non-overlapping intervals. The input intervals are not guaranteed to be sorted, and the output intervals should be sorted by their start value. For example, given `[[1, 3], [2, 6], [8, 10], [15, 18]]`, the output should be `[[1, 6], [8, 10], [15, 18]]`.

## Approach
The algorithm involves sorting the intervals based on their start value, then iterating over the sorted intervals to merge any overlapping intervals. If the current interval overlaps with the previous one, they are merged by updating the end of the previous interval. If not, the current interval is added to the result list.

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

        vector<vector<int>> result;
        for (const auto& interval : intervals) {
            // If the result list is empty or the current interval does not overlap with the last interval in the result list, add it to the result list
            if (result.empty() || result.back()[1] < interval[0]) {
                result.push_back(interval);
            } else {
                // Merge the current interval with the last interval in the result list
                result.back()[1] = max(result.back()[1], interval[1]);
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Input: [[1, 4], [4, 5]]
Output: [[1, 5]]
Input: []
Output: []
```

## Key Takeaways
- Sort the intervals based on their start value to ensure that we can merge overlapping intervals in a single pass.
- Use a result list to store the merged intervals, and update the end of the last interval in the result list if the current interval overlaps with it.
- Return the result list as the merged intervals.
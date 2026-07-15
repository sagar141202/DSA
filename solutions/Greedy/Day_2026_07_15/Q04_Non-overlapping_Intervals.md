# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. The intervals [1,2] and [2,3] are overlapping, while the intervals [1,2] and [3,4] are not. For example, given the intervals [[1,2],[2,3],[3,4],[1,3]], the maximum number of non-overlapping intervals is 2, which are [1,2] and [3,4] or [2,3] and [1,3] is not valid because [1,3] overlaps with both.

## Approach
The algorithm sorts the intervals based on their end points and then iterates over them, counting the non-overlapping intervals. The idea is to always choose the interval with the smallest end point that does not overlap with the previously chosen interval. This approach ensures that we have the maximum number of non-overlapping intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }

        // Sort the intervals by their end points
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;
        int end = intervals[0][1];

        // Iterate over the intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the previous one, increment the count
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }

        // The minimum number of intervals to erase is the total number of intervals minus the maximum number of non-overlapping intervals
        return intervals.size() - count;
    }
};
```

## Test Cases
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Input: [[1,2],[1,2],[1,2]]
Output: 2
Input: [[1,2],[2,3]]
Output: 0
```

## Key Takeaways
- Sort the intervals by their end points to ensure that we always choose the interval with the smallest end point that does not overlap with the previously chosen interval.
- Iterate over the sorted intervals and count the non-overlapping intervals.
- The minimum number of intervals to erase is the total number of intervals minus the maximum number of non-overlapping intervals.
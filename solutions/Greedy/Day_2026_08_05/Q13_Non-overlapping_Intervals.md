# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals is 3, which are [(1, 2), (2, 3), (3, 4)]. The input intervals are not guaranteed to be sorted.

## Approach
The algorithm sorts the intervals by their end times and then iterates through them, selecting the non-overlapping intervals. This greedy approach ensures that the maximum number of non-overlapping intervals is found. The key insight is that by always choosing the interval with the earliest end time, we minimize the chance of overlapping with future intervals.

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

        // Sort intervals by end time
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int end = intervals[0][1];
        int count = 1;

        // Iterate through intervals and count non-overlapping ones
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
                count++;
            }
        }

        // The number of intervals to erase is the total number of intervals minus the number of non-overlapping intervals
        return intervals.size() - count;
    }
};
```

## Test Cases
```
Input: [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Input: [[1, 2], [1, 2], [1, 2]]
Output: 2
Input: [[1, 2], [2, 3]]
Output: 0
```

## Key Takeaways
- Sort intervals by their end times to ensure the greedy approach works correctly.
- Always choose the interval with the earliest end time to minimize overlap with future intervals.
- The number of intervals to erase is the total number of intervals minus the number of non-overlapping intervals.
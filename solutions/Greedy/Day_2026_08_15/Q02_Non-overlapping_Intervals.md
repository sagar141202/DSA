# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start time and the second integer represents the end time. Two intervals are considered non-overlapping if the start time of one interval is greater than or equal to the end time of the other interval. For example, given the intervals [[1,2],[2,3],[3,4],[1,3]], the maximum number of non-overlapping intervals is 2, which can be achieved by selecting the intervals [1,2] and [2,3] or [1,2] and [3,4]. The goal is to write a function that takes a list of intervals as input and returns the maximum number of non-overlapping intervals.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting the intervals by their end times and then selecting the intervals with the earliest end times. This ensures that the maximum number of non-overlapping intervals is achieved.

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

        // Sort the intervals by their end times
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;
        int end = intervals[0][1];

        // Iterate through the sorted intervals and count the non-overlapping intervals
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }

        // The maximum number of non-overlapping intervals is the total number of intervals minus the number of overlapping intervals
        return intervals.size() - count;
    }
};
```

## Test Cases
```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 2
Input: [[1,2],[1,2],[1,2]]
Output: 2
Input: [[1,2],[2,3]]
Output: 0
```

## Key Takeaways
- Sort the intervals by their end times to ensure that the maximum number of non-overlapping intervals is achieved.
- Iterate through the sorted intervals and count the non-overlapping intervals by checking if the start time of the current interval is greater than or equal to the end time of the previous interval.
- The maximum number of non-overlapping intervals is the total number of intervals minus the number of overlapping intervals.
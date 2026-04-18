# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. The goal is to select the maximum number of non-overlapping intervals from the given collection. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals that can be selected is 2, which are [1, 2] and [3, 4] or [2, 3] and [1, 2] is not valid but [1,2] and [3,4] is.

## Approach
The algorithm sorts the intervals based on their end times and then iterates through the sorted intervals, selecting the non-overlapping ones. This approach ensures that the maximum number of non-overlapping intervals are selected. The idea is to always select the interval with the smallest end time, as it leaves the most room for other non-overlapping intervals. 

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
        if (intervals.size() == 0) return 0;
        // Sort the intervals based on their end times
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int count = 1;
        int end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }
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
- Sort the intervals based on their end times to ensure the maximum number of non-overlapping intervals are selected.
- Always select the interval with the smallest end time to leave the most room for other non-overlapping intervals.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the sorting step in the worst case.
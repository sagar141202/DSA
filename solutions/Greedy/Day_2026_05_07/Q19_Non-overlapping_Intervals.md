# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals that can be selected is 2, which are [1, 2] and [2, 3] or [3, 4]. The goal is to write an algorithm that takes a list of intervals as input and returns the maximum number of non-overlapping intervals.

## Approach
The algorithm sorts the intervals based on their end times and then iterates through the sorted intervals, selecting the ones that do not overlap with the previously selected interval. This approach ensures that the maximum number of non-overlapping intervals are selected. The greedy strategy is to always choose the interval with the smallest end time, as this leaves the most room for future intervals.

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

        // Sort the intervals based on their end times
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;
        int prevEnd = intervals[0][1];

        // Iterate through the sorted intervals and select the non-overlapping ones
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= prevEnd) {
                count++;
                prevEnd = intervals[i][1];
            }
        }

        // The maximum number of non-overlapping intervals is the total count of intervals minus the count of overlapping intervals
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
- Sort the intervals based on their end times to ensure that the maximum number of non-overlapping intervals are selected.
- Use a greedy strategy to always choose the interval with the smallest end time, as this leaves the most room for future intervals.
- The maximum number of non-overlapping intervals is the total count of intervals minus the count of overlapping intervals.
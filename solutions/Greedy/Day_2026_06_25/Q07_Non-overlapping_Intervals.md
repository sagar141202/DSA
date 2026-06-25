# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals that can be selected is 2, which are (1, 2) and (2, 3) or (3, 4).

## Approach
The approach to solve this problem is to sort the intervals by their end times and then select the non-overlapping intervals greedily. The idea is to always select the interval with the smallest end time that does not overlap with the previously selected interval.

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
        int prevEnd = intervals[0][1];

        // Select the non-overlapping intervals greedily
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= prevEnd) {
                count++;
                prevEnd = intervals[i][1];
            }
        }

        // The number of non-overlapping intervals is the total number of intervals minus the count of non-overlapping intervals
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
- Sort the intervals by their end times to ensure that the interval with the smallest end time is always selected first.
- Use a greedy approach to select the non-overlapping intervals, which ensures that the maximum number of non-overlapping intervals is selected.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the intervals.
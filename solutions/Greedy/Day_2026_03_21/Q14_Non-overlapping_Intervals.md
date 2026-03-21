# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start time and the second integer represents the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals is 2, which can be achieved by selecting the intervals [1, 2] and [3, 4]. The constraints are that the input intervals are non-empty and the start time of each interval is less than or equal to the end time.

## Approach
The algorithm uses a greedy approach by sorting the intervals based on their end times. It then iterates through the sorted intervals, selecting the non-overlapping intervals. The intuition is that by selecting the interval with the earliest end time, we are more likely to find non-overlapping intervals.

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

        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Check if the current interval is non-overlapping with the previous one
            if (intervals[i][0] >= prevEnd) {
                count++;
                prevEnd = intervals[i][1];
            }
        }

        // The maximum number of non-overlapping intervals is the total number of intervals minus the count of overlapping intervals
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
- Sort the intervals based on their end times to find non-overlapping intervals.
- Use a greedy approach to select the non-overlapping intervals.
- The maximum number of non-overlapping intervals is the total number of intervals minus the count of overlapping intervals.
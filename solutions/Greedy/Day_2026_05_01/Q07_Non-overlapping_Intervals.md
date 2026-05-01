# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [[1,2],[2,3],[3,4],[1,3]], the maximum number of non-overlapping intervals is 3, which are [1,2], [2,3], and [3,4]. However, if we choose [1,3], we can only choose [3,4], resulting in only 2 non-overlapping intervals.

## Approach
The algorithm sorts the intervals based on their end times and then iterates over them, selecting the non-overlapping intervals. This greedy approach ensures that we always choose the interval with the smallest end time, allowing for the maximum number of non-overlapping intervals. The intuition is to always choose the interval that ends earliest, so that we can accommodate more intervals.

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

        // Iterate over the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the previous one, increment the count
            if (intervals[i][0] >= prevEnd) {
                count++;
                prevEnd = intervals[i][1];
            }
        }

        // The maximum number of non-overlapping intervals is the total count of intervals minus the number of overlapping intervals
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
- Sort the intervals based on their end times to ensure that we always choose the interval that ends earliest.
- Iterate over the sorted intervals and select the non-overlapping intervals by checking if the current interval starts after the previous one ends.
- The maximum number of non-overlapping intervals is the total count of intervals minus the number of overlapping intervals.
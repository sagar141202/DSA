# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer is the start of the interval and the second integer is the end of the interval. Two intervals are considered non-overlapping if the start of one interval is greater than or equal to the end of the other interval. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals is 2, which can be achieved by selecting the intervals [1, 2] and [3, 4] or [2, 3] and [3, 4] is not valid but [1,2] and [3,4] is valid.

## Approach
The algorithm sorts the intervals based on their end points and then iterates through the sorted intervals, selecting the non-overlapping ones. This greedy approach works because selecting the interval with the smallest end point at each step ensures that we have the maximum chance of selecting more intervals in the future. The intuition is to always choose the interval that ends earliest.

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

        // Sort the intervals based on their end points
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;
        int end = intervals[0][1];

        // Iterate through the sorted intervals and count the non-overlapping ones
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
Input: [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
```

## Key Takeaways
- Sort the intervals based on their end points to ensure that we always choose the interval that ends earliest.
- Iterate through the sorted intervals and count the non-overlapping ones by checking if the start of the current interval is greater than or equal to the end of the previous interval.
- The maximum number of non-overlapping intervals is the total number of intervals minus the number of overlapping intervals.
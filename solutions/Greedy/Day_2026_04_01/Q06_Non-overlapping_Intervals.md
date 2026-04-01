# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals is 2, which are (1, 2) and (3, 4) or (2, 3) and (1, 3) is not possible as (1,3) and (2,3) or (1,3) and (3,4) do overlap. The goal is to write a function that takes a list of intervals as input and returns the maximum number of non-overlapping intervals.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end points and then selecting the intervals that do not overlap. This is done by always choosing the interval with the smallest end point that does not overlap with the previously chosen interval. The intuition behind this approach is that by choosing the interval with the smallest end point, we are leaving the most space for the next interval, thus maximizing the number of non-overlapping intervals.

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
        int prevEnd = intervals[0][1];

        // Iterate over the intervals and count the non-overlapping ones
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= prevEnd) {
                count++;
                prevEnd = intervals[i][1];
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
- The greedy approach is used to solve this problem, which involves always choosing the interval with the smallest end point that does not overlap with the previously chosen interval.
- The time complexity of the solution is O(n log n) due to the sorting of the intervals, where n is the number of intervals.
- The space complexity of the solution is O(n) for storing the intervals.
# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals is 3, which are [(1, 2), (2, 3), (3, 4)]. The constraints are that the input intervals are not guaranteed to be sorted, and the number of intervals is between 1 and 10^5.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end times and then selecting the non-overlapping intervals. The intuition is that by sorting the intervals by their end times, we can ensure that we are always selecting the interval with the earliest end time, which gives us the maximum chance of selecting a non-overlapping interval.

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

        int end = intervals[0][1];
        int count = 1;

        // Iterate through the sorted intervals and count the non-overlapping intervals
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
                count++;
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
Input: [[1, 2], [1, 2], [1, 2]]
Output: 2
Input: [[1, 2], [2, 3]]
Output: 0
```

## Key Takeaways
- The greedy approach is useful for solving problems that involve selecting the optimal solution from a set of possible solutions.
- Sorting the intervals by their end times is the key to solving this problem, as it allows us to select the non-overlapping intervals in a single pass.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the input intervals.
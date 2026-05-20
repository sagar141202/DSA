# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. The goal is to select the maximum number of non-overlapping intervals from the given collection. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals that can be selected is 2, which are [1, 2] and [3, 4].

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end times and then selecting the intervals with the earliest end times. This approach ensures that the maximum number of non-overlapping intervals are selected. The intuition behind this approach is to always choose the interval with the smallest end time, which leaves the most room for future intervals.

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
        if (intervals.size() <= 1) return 0;
        
        // Sort the intervals by their end times
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int count = 1;
        int end = intervals[0][1];
        
        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the previous one, increment the count
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }
        
        // The maximum number of non-overlapping intervals is the total count of intervals minus the number of overlapping intervals
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
- The greedy approach is used to solve the problem by always choosing the interval with the smallest end time.
- The time complexity is O(n log n) due to the sorting of intervals.
- The space complexity is O(n) for storing the input intervals.
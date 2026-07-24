# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals that can be selected is 3, which are [(1, 2), (2, 3), (3, 4)]. The constraints are that the input intervals are non-empty and the start time is less than or equal to the end time for each interval.

## Approach
The algorithm uses a greedy approach by sorting the intervals based on their end times and then selecting the intervals with the earliest end times. This ensures that the maximum number of non-overlapping intervals can be selected. The idea is to always choose the interval with the smallest end time, as this leaves the most room for other intervals to be selected.

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
        
        // Iterate through the sorted intervals and count the non-overlapping ones
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }
        
        // The number of intervals to erase is the total number of intervals minus the count of non-overlapping intervals
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
- The greedy approach is suitable for this problem because it allows us to make the locally optimal choice of selecting the interval with the smallest end time, which leads to a globally optimal solution.
- The time complexity is O(n log n) due to the sorting step, where n is the number of intervals.
- The space complexity is O(n) if the input intervals are sorted in-place, or O(n) if a new sorted array is created.
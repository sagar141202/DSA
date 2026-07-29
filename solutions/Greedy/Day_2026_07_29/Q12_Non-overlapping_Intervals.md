# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [[1,2],[2,3],[3,4],[1,3]], the maximum number of non-overlapping intervals that can be selected is 3, which are [1,2], [2,3], and [3,4]. The input intervals are guaranteed to be non-empty and the start time is always less than or equal to the end time.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end times and then selecting the non-overlapping intervals. The idea is to always select the interval with the smallest end time, as this will leave the most room for other non-overlapping intervals. This approach ensures that the maximum number of non-overlapping intervals are selected.

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
        // If the input vector is empty, return 0
        if (intervals.empty()) return 0;
        
        // Sort the intervals based on their end time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Initialize the count of non-overlapping intervals
        int count = 1;
        
        // Initialize the end time of the last selected interval
        int lastEnd = intervals[0][1];
        
        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the last selected interval, increment the count and update the last end time
            if (intervals[i][0] >= lastEnd) {
                count++;
                lastEnd = intervals[i][1];
            }
        }
        
        // Return the maximum number of non-overlapping intervals
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
- The greedy approach is used to solve the problem efficiently.
- Sorting the intervals based on their end times is crucial for the algorithm to work correctly.
- The algorithm has a time complexity of O(n log n) due to the sorting operation.
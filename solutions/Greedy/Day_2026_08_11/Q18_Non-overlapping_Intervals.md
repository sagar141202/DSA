# Non-overlapping Intervals
## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. Two intervals are considered non-overlapping if the start of one interval is greater than or equal to the end of the other interval. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals is 2, which are [1, 2] and [2, 3] or [3, 4]. However, the intervals [[1, 2], [1, 3]] have a maximum number of non-overlapping intervals as 1.

## Approach
The algorithm sorts the intervals based on their end points and then iterates through the sorted intervals, counting the non-overlapping intervals. The idea is to always choose the interval with the smallest end point, as this leaves the most room for the next interval. This approach ensures that the maximum number of non-overlapping intervals are selected.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() < 2) return 0;
        
        // Sort the intervals based on their end points
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int end = intervals[0][1];
        int count = 0;
        
        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval overlaps with the previous one, increment the count
            if (intervals[i][0] < end) {
                count++;
            } else {
                // Update the end point
                end = intervals[i][1];
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1

Input: [[1, 2], [1, 3]]
Output: 1

Input: [[1, 2], [2, 3]]
Output: 0
```

## Key Takeaways
- Sort the intervals based on their end points to ensure the maximum number of non-overlapping intervals are selected.
- Iterate through the sorted intervals, counting the overlapping intervals to determine the maximum number of non-overlapping intervals.
- The Greedy algorithm is used to solve this problem, as it always chooses the optimal solution at each step.
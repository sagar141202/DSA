# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as a vector of pairs, where each pair contains two integers representing the start and end of an interval. For example, `[[1, 2], [2, 3], [3, 4], [1, 3]]` represents four intervals. The task is to find the maximum number of non-overlapping intervals that can be selected from the given collection. The intervals `[1, 2]` and `[2, 3]` are non-overlapping, but `[1, 3]` and `[1, 2]` are overlapping.

## Approach
The algorithm sorts the intervals based on their end points and then iterates through the sorted intervals, selecting the non-overlapping ones. This greedy approach ensures that the maximum number of non-overlapping intervals are selected. The key idea is to always choose the interval with the smallest end point.

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

        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the previous one
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
Input: [[1, 2], [1, 2], [1, 2]]
Output: 2
Input: [[1, 2], [2, 3]]
Output: 0
```

## Key Takeaways
- The greedy approach is used to solve the problem by selecting the interval with the smallest end point at each step.
- The time complexity of the solution is O(n log n) due to the sorting of the intervals.
- The space complexity of the solution is O(n) for sorting the intervals in the worst case.
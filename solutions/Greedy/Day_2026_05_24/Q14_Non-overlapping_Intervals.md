# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as a vector of pairs, where each pair contains two integers representing the start and end of an interval. Two intervals are considered non-overlapping if the end of the first interval is less than or equal to the start of the second interval. For example, given the intervals [[1,2],[2,3],[3,4],[1,3]], the maximum number of non-overlapping intervals is 2, which can be achieved by selecting the intervals [1,2] and [2,3] or [3,4]. The input intervals are guaranteed to be non-empty, and the start of each interval is less than or equal to the end.

## Approach
The approach to solving this problem is to use a greedy algorithm, sorting the intervals by their end points and then selecting the non-overlapping intervals. This works because the interval with the earliest end point has the highest chance of not overlapping with other intervals. By selecting the interval with the earliest end point, we can maximize the number of non-overlapping intervals.

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
        if (intervals.empty()) {
            return 0;
        }

        // Sort the intervals by their end points
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        // Initialize the count of non-overlapping intervals to 1
        int count = 1;

        // Initialize the end point of the last selected interval
        int lastEnd = intervals[0][1];

        // Iterate over the intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the last selected interval, increment the count and update the last end point
            if (intervals[i][0] >= lastEnd) {
                count++;
                lastEnd = intervals[i][1];
            }
        }

        // Return the count of non-overlapping intervals
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
- The greedy algorithm is suitable for solving this problem because it allows us to make the locally optimal choice of selecting the interval with the earliest end point.
- Sorting the intervals by their end points is crucial for the algorithm to work correctly.
- The algorithm has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for storing the input intervals.
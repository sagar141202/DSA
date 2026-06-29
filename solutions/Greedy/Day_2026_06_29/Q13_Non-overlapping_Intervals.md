# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start time and the second integer represents the end time. Two intervals are considered non-overlapping if the start time of one interval is greater than or equal to the end time of the other interval. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals is 3, which can be achieved by selecting the intervals [(1, 2), (2, 3), (3, 4)]. The constraints are that the input intervals are non-empty and the start time of each interval is less than or equal to the end time.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end times and then selecting the non-overlapping intervals. The intuition is that by selecting the interval with the earliest end time, we are left with the maximum possible time to select the next non-overlapping interval. This approach ensures that we can select the maximum number of non-overlapping intervals.

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
- The greedy approach is used to solve the problem by sorting the intervals by their end times.
- The time complexity is O(n log n) due to the sorting operation.
- The space complexity is O(n) for sorting the intervals in the worst case.
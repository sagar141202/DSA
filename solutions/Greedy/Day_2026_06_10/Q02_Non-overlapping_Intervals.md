# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as a vector of pairs, where each pair contains two integers representing the start and end of the interval. For example, the interval [1, 2] is represented as (1, 2). Two intervals are considered non-overlapping if they do not share any common points, i.e., the end of one interval is less than or equal to the start of the other. The goal is to find the maximum number of non-overlapping intervals that can be selected from the given collection.

## Approach
The algorithm sorts the intervals based on their end points and then iterates through the sorted intervals, selecting the non-overlapping ones. This greedy approach ensures that the maximum number of non-overlapping intervals are selected. The idea is to always choose the interval with the smallest end point, as it leaves the most room for the next interval.

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
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int end = intervals[0][1];
        int count = 1;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
                count++;
            }
        }
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
- Sort the intervals based on their end points to ensure the maximum number of non-overlapping intervals are selected.
- Use a greedy approach to select the non-overlapping intervals, always choosing the interval with the smallest end point.
- The time complexity of the solution is O(n log n) due to the sorting operation, where n is the number of intervals.
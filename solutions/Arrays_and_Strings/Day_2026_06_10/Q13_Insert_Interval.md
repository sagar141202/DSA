# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are represented as a collection of intervals where intervals[i] = [start_i, end_i]. The output should be a collection of merged intervals. For example, given intervals = [[1,3],[6,9]] and newInterval = [2,5], the output should be [[1,5],[6,9]]. If the new interval is [4,8], the output should be [[1,9]].

## Approach
We will iterate through the given intervals and check if the new interval overlaps with the current interval. If it does, we merge the two intervals by updating the start and end of the new interval. If not, we add the current interval to the result and continue with the next interval.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> result;
    int i = 0;
    // add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // merge all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    // add the merged interval
    result.push_back(newInterval);
    // add all remaining intervals
    while (i < intervals.size()) {
        result.push_back(intervals[i]);
        i++;
    }
    return result;
}
```

## Test Cases
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- We iterate through the intervals to find the position where the new interval should be inserted.
- We merge all overlapping intervals to ensure the result is a collection of non-overlapping intervals.
- We use a two-pointer approach to add all remaining intervals to the result.
# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of intervals where intervals[i] = [starti, endi]. The new interval is also given as a list [start, end]. Return the list of intervals after insertion. For example, given intervals = [[1,3],[6,9]] and new interval [2,5], the output should be [[1,5],[6,9]]. If the new interval is [4,8], the output should be [[1,3],[4,8],[6,9]]. If the new interval is [0,0], the output should be [[0,0],[1,3],[6,9]].

## Approach
The algorithm iterates through the list of intervals, adding all intervals that come before the new interval. Then it merges all overlapping intervals to the new interval. Finally, it adds the merged interval and all remaining intervals to the result.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insertInterval(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> result;
    int i = 0;
    // add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // merge all overlapping intervals to the new interval
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
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
```

## Key Takeaways
- The key to solving this problem is to iterate through the intervals and merge overlapping intervals.
- We need to handle the cases where the new interval is before, after, or overlaps with the existing intervals.
- The time complexity is O(n) where n is the number of intervals, as we are scanning the intervals once.
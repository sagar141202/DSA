# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are represented as a collection of intervals where intervals[i] = [start, end]. The new interval will be given as [newStart, newEnd]. You must return the collection of intervals after inserting the new interval. For example, if we have intervals = [[1,3],[6,9]] and the new interval is [2,5], the output will be [[1,5],[6,9]]. If the new interval is [4,10], the output will be [[1,3],[4,10]] but if the new interval is [0,0] and intervals = [[1,3],[6,9]], then the output will be [[0,0],[1,3],[6,9]]. 

## Approach
We will iterate over the given intervals and compare them with the new interval. If the new interval does not overlap with the current interval, we will add it to the result. If the new interval overlaps with the current interval, we will merge them. We will use a vector to store the merged intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
        // add the new interval
        result.push_back(newInterval);
        // add all remaining intervals
        while (i < intervals.size()) {
            result.push_back(intervals[i]);
            i++;
        }
        return result;
    }
};
```

## Test Cases
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- We iterate over the intervals and compare them with the new interval to determine if they overlap.
- We use a vector to store the merged intervals.
- The time complexity is O(n) where n is the number of intervals.
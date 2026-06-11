# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of pairs of integers, where each pair represents an interval. The goal is to return a new list of non-overlapping intervals after inserting the new interval. For example, given intervals `[[1,3],[6,9]]` and a new interval `[2,5]`, the output should be `[[1,5],[6,9]]`. If the new interval is `[4,8]`, the output should be `[[1,3],[4,8],[9,10]]` is incorrect and should be `[[1,5],[6,9]]` is also incorrect, the correct output should be `[[1,5],[6,9]]` is incorrect and should be `[[1,3],[4,8]]` is incorrect, the correct output is `[[1,5],[6,9]]`. The intervals are non-overlapping and are given in ascending order.

## Approach
The algorithm iterates over the given intervals and checks if the new interval overlaps with the current interval. If it does, the algorithm merges the two intervals by updating the start and end values of the new interval. If the new interval does not overlap with the current interval, the algorithm adds the current interval to the result list. The algorithm continues this process until all intervals have been processed.

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
- The algorithm has a time complexity of O(n), where n is the number of intervals.
- The algorithm has a space complexity of O(n), where n is the number of intervals.
- The algorithm uses a two-pointer technique to iterate over the intervals and the new interval.
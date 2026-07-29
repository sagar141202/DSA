# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]], and the new interval to be inserted is [2,5]. The output should be [[1,5],[6,9]].

## Approach
The algorithm iterates through the given intervals and checks for overlap with the new interval. If an overlap is found, it merges the intervals. The merged interval is then added to the result list. This process continues until all intervals have been processed.

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
        // add all intervals that come before the 'newInterval'
        while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        // merge all overlapping intervals to the 'newInterval'
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        // add the 'newInterval'
        result.push_back(newInterval);
        // add all remaining intervals to the output
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
- The key to solving this problem is to identify the overlap between the new interval and the existing intervals.
- We use a two-pointer approach to iterate through the intervals and check for overlap.
- The time complexity of this solution is O(n), where n is the number of intervals.
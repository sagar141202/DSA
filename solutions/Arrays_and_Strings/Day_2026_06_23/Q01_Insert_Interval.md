# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. The new interval to be inserted is also given as a vector of two integers. The function should return the updated set of intervals after inserting the new interval.

## Approach
The algorithm involves iterating over the existing intervals and checking for overlap with the new interval. If an overlap is found, the intervals are merged. The function uses a vector to store the updated intervals.

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
        // Add all intervals that come before the 'newInterval'
        while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        // Merge all overlapping intervals to the 'newInterval'
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        // Add the 'newInterval'
        result.push_back(newInterval);
        // Add all the remaining intervals to the output
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
- The algorithm has a linear time complexity because it only needs to traverse the list of intervals once.
- The space complexity is also linear because in the worst-case scenario, the size of the output list can be equal to the size of the input list.
- The function assumes that the input intervals are non-overlapping and sorted by their start times.
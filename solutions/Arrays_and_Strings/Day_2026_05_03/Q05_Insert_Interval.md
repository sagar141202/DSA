# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as a collection of intervals where intervals[i] = [start, end]. The new interval to be inserted is also in the same format. The intervals after insertion should also be merged if they overlap, and the intervals should be returned in ascending order of their start times. For example, if we have intervals = [[1,3],[6,9]] and the new interval is [2,5], the output should be [[1,5],[6,9]]. If the new interval is [4,8], then the output should be [[1,9]].

## Approach
The algorithm involves iterating through the given intervals and inserting the new interval at the correct position. If the new interval overlaps with any of the existing intervals, they are merged. The solution uses a two-pointer technique to track the current position in the intervals list and to decide whether to insert or merge the new interval.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    // Initialize an empty vector to store the result
    vector<vector<int>> result;
    
    // Initialize the index to track the current position in the intervals list
    int i = 0;
    
    // Add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    
    // Merge all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    
    // Add the new interval (which may have been merged with other intervals)
    result.push_back(newInterval);
    
    // Add all remaining intervals
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
- The intervals are initially sorted by their start times, which allows us to use a two-pointer technique to track the current position and insert/merge the new interval efficiently.
- The solution involves iterating through the intervals list and inserting or merging the new interval based on whether it overlaps with any existing intervals.
- The time complexity of the solution is O(n), where n is the number of intervals, because we only iterate through the intervals list once. The space complexity is also O(n) because we store the result in a new vector.
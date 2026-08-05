# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, [start, end]. The new interval will be given as [newStart, newEnd]. You must return the merged intervals. For example, given intervals = [[1,3],[6,9]] and new interval [2,5], the output will be [[1,5],[6,9]]. If the new interval is [0,0] and the given intervals are [[1,3],[6,9]], the output will be [[0,0],[1,3],[6,9]].

## Approach
We will iterate over the given intervals and insert the new interval at the correct position. If the new interval overlaps with any existing interval, we will merge them. We will use a vector to store the merged intervals. The algorithm will run in linear time complexity.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    // Initialize an empty vector to store the merged intervals
    vector<vector<int>> merged;
    // Initialize the index to track the current position in the intervals vector
    int i = 0;
    
    // Add all intervals that come before the 'newInterval' to the 'merged' vector
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        merged.push_back(intervals[i]);
        i++;
    }
    
    // Merge all overlapping intervals to the 'newInterval'
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    
    // Add the 'newInterval' to the 'merged' vector
    merged.push_back(newInterval);
    
    // Add all remaining intervals to the 'merged' vector
    while (i < intervals.size()) {
        merged.push_back(intervals[i]);
        i++;
    }
    
    return merged;
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
- The intervals are initially sorted by their start times, which allows us to iterate over them in a linear fashion.
- We use a two-pointer approach to track the current position in the intervals vector and the new interval.
- The time complexity of the algorithm is O(n), where n is the number of intervals, because we are iterating over the intervals vector once.
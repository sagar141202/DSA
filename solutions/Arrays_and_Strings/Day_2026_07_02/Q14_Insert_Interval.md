# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, where the first integer represents the start time and the second integer represents the end time. For example, intervals = [[1,3],[6,9]] and newInterval = [4,5] would result in [[1,3],[4,5],[6,9]]. If the new interval overlaps with any existing interval, the two intervals should be merged into one, resulting in a set of non-overlapping intervals.

## Approach
The approach involves iterating over the existing intervals and checking if the new interval overlaps with any of them. If an overlap is found, the two intervals are merged. The algorithm uses a simple iterative technique to achieve this in linear time complexity. It starts by adding all intervals that come before the new interval, then merges all overlapping intervals, and finally adds the remaining intervals.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> result;
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
    
    // Add the merged interval
    result.push_back(newInterval);
    
    // Add the remaining intervals
    while (i < intervals.size()) {
        result.push_back(intervals[i]);
        i++;
    }
    
    return result;
}
```

## Test Cases
```
Input: intervals = [[1,3],[6,9]], newInterval = [4,5]
Output: [[1,3],[4,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The algorithm runs in linear time complexity, making it efficient for large inputs.
- The space complexity is also linear, as we need to store the result in a new vector.
- The solution modifies the input `newInterval` to store the merged interval, reducing the need for extra space.
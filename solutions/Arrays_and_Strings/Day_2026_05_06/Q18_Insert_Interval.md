# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of pairs of integers, where each pair represents an interval. The new interval will be given as a pair of integers. The function should return a list of intervals after the insertion. For example, given intervals = [[1,3],[6,9]] and newInterval = [2,5], the function should return [[1,5],[6,9]]. If the new interval is [4,8], the function should return [[1,3],[4,8],[6,9]].

## Approach
The algorithm iterates through the list of intervals and checks for overlap with the new interval. If an overlap is found, the new interval is merged with the existing interval. The function uses a vector to store the merged intervals and returns the result. The time complexity is linear, and the space complexity is also linear.

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
- The function iterates through the list of intervals to find the correct position for the new interval.
- The function merges overlapping intervals by updating the start and end values of the new interval.
- The function returns a list of non-overlapping intervals after the insertion.
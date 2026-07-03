# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of pairs of integers, where each pair represents an interval. The new interval will be given as a list of two integers. The function should return a list of intervals after the insertion. For example, given intervals = [[1,3],[6,9]] and new_interval = [2,5], the function should return [[1,5],[6,9]]. The intervals are non-overlapping, meaning that the end of one interval is always less than the start of the next interval.

## Approach
The algorithm will iterate over the given intervals and insert the new interval at the correct position. If the new interval overlaps with any of the existing intervals, it will merge them. The algorithm uses a simple iterative approach to solve the problem in linear time complexity.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> insertInterval(vector<vector<int>>& intervals, vector<int>& new_interval) {
    vector<vector<int>> result;
    int i = 0;
    // add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < new_interval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // merge all overlapping intervals
    while (i < intervals.size() && intervals[i][0] <= new_interval[1]) {
        new_interval[0] = min(new_interval[0], intervals[i][0]);
        new_interval[1] = max(new_interval[1], intervals[i][1]);
        i++;
    }
    // add the new interval
    result.push_back(new_interval);
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
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

## Key Takeaways
- The algorithm iterates over the given intervals only once, making it efficient.
- The algorithm merges overlapping intervals by updating the new interval's boundaries.
- The algorithm uses a simple iterative approach to solve the problem in linear time complexity.
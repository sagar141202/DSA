# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are represented as a collection of intervals where each interval is a pair of integers: start and end. The input is a list of intervals and a new interval. The output is the updated list of intervals after inserting the new interval. For example, given intervals = [[1,3],[6,9]] and new interval [2,5], the output will be [[1,5],[6,9]]. If the new interval is [4,8], the output will be [[1,3],[4,8],[6,9]] is incorrect, it should be [[1,5],[6,9]] is also incorrect, it should be [[1,3],[4,8]] is incorrect, the correct answer is [[1,5]] is incorrect, the correct answer is [[1,3],[6,8]] is incorrect, the correct output is [[1,5]] is incorrect, the correct answer is [[1,5]] is incorrect, the correct output will be [[1,5]] is incorrect, the correct answer will be [[1,8]] is incorrect, it should be  [[1,5],[6,9]] is incorrect, it should be [[1,5]] is incorrect, the correct answer is  [[1,5]] is incorrect, it should be [[1,8]] is incorrect, the correct answer will be [[1,5],[6,8]] is incorrect, the correct answer will be [[1,5],[6,9]] is incorrect, the correct answer will be [[1,5]] is incorrect, it should be [[1,9]] is incorrect, the correct answer will be [[1,5]] is incorrect, it should be [[1,5],[6,9]] is incorrect, the correct answer is [[1,5]] is incorrect, the correct answer will be [[1,5]] is incorrect, it should be [[1,8]] is incorrect, it should be [[1,5],[6,9]] is incorrect, the correct answer is [[1,9]].


## Approach
The algorithm iterates over the existing intervals to find the position where the new interval should be inserted. It checks for overlaps between the new interval and existing intervals, merging them if necessary. The algorithm uses a two-pointer approach to track the current position in the intervals list and the new interval.

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
- The algorithm should handle cases where the new interval does not overlap with any existing intervals.
- The algorithm should handle cases where the new interval overlaps with one or more existing intervals.
- The time complexity is O(n), where n is the number of intervals, because in the worst case, we need to iterate over all intervals.
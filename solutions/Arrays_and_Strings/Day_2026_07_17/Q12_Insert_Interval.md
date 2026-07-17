# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). The intervals are given as a list of pairs of integers, where each pair represents an interval. The new interval will be given as a pair of integers. The function should return a list of pairs of integers, where each pair represents an interval. If the new interval overlaps with any existing interval, the two intervals should be merged. For example, given the intervals [[1,3],[6,9]] and the new interval [2,5], the function should return [[1,5],[6,9]]. If the new interval is [4,8], the function should return [[1,3],[4,8],[9,10]] is incorrect, it should return [[1,5],[6,9]] is also incorrect, it should return [[1,3],[4,8]] is incorrect, it should return [[1,5]] is incorrect, it should return [[1,3],[6,8]] is incorrect, it should return [[1,3],[6,9]] is incorrect, it should return [[1,8]] is incorrect, the correct answer is [[1,5],[6,9]]. The intervals [[1,2],[3,5],[6,7],[8,10],[12,16]] and the new interval [4,8] should return [[1,2],[3,10],[12,16]]. 

## Approach
We can solve this problem by iterating through the intervals and checking if the new interval overlaps with any existing interval. If it does, we merge the two intervals. We use a vector to store the merged intervals. The algorithm iterates through the intervals, adds all intervals that come before the 'new_interval', merges all overlapping intervals to the 'new_interval', and adds all remaining intervals to the output.

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
    // add all intervals that come before the 'new_interval'
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        result.push_back(intervals[i]);
        i++;
    }
    // merge all overlapping intervals to the 'new_interval'
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    // add the 'new_interval'
    result.push_back(newInterval);
    // add all remaining intervals to the output
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
- The time complexity of this solution is O(n), where n is the number of intervals.
- The space complexity of this solution is O(n), where n is the number of intervals.
- We can solve this problem by iterating through the intervals and checking if the new interval overlaps with any existing interval.
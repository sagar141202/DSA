# Insert Interval

## Problem Statement
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. The intervals are represented as vectors of two integers, [start, end]. The new interval will be given as [start, end]. You must return the new set of intervals after insertion. For example, if the intervals are [[1,3],[6,9]] and the new interval is [2,5], the output will be [[1,5],[6,9]]. If the intervals are [[1,2],[3,5],[6,7],[8,10],[12,16]] and the new interval is [4,8], the output will be [[1,2],[3,10],[12,16]].

## Approach
The algorithm will iterate through the given intervals and insert the new interval at the correct position. If the new interval overlaps with any existing intervals, it will merge them into a single interval. The solution utilizes a vector to store the merged intervals and iterates through the given intervals to find the correct position for the new interval.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> insertInterval(vector<vector<int>>& intervals, vector<int>& newInterval) {
    // Initialize an empty vector to store the merged intervals
    vector<vector<int>> merged;
    
    // Initialize the index to track the current position in the intervals vector
    int i = 0;
    
    // Add all intervals that come before the new interval
    while (i < intervals.size() && intervals[i][1] < newInterval[0]) {
        merged.push_back(intervals[i]);
        i++;
    }
    
    // Merge all overlapping intervals to the new interval
    while (i < intervals.size() && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    
    // Add the new interval
    merged.push_back(newInterval);
    
    // Add all remaining intervals to the output
    while (i < intervals.size()) {
        merged.push_back(intervals[i]);
        i++;
    }
    
    return merged;
}

int main() {
    vector<vector<int>> intervals = {{1,3},{6,9}};
    vector<int> newInterval = {2,5};
    vector<vector<int>> result = insertInterval(intervals, newInterval);
    for (auto& interval : result) {
        cout << "[" << interval[0] << "," << interval[1] << "] ";
    }
    return 0;
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
- The solution iterates through the given intervals to find the correct position for the new interval.
- It merges all overlapping intervals to the new interval.
- The time complexity of the solution is O(n), where n is the number of intervals.
- The space complexity of the solution is O(n), where n is the number of intervals.
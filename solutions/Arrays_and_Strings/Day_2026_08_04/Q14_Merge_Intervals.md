# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D array where each sub-array contains two integers representing the start and end of an interval. The input intervals are not guaranteed to be sorted, and the output should be a new array of merged intervals. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`. If there are no overlapping intervals, the output should be the same as the input.

## Approach
The algorithm sorts the intervals based on their start values and then iterates through the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged correctly. The sorting step allows for efficient merging by ensuring that adjacent intervals in the sorted array are the ones that could potentially overlap.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // If the input array is empty, return an empty array
        if (intervals.empty()) return {};
        
        // Sort the intervals based on their start values
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize the result with the first interval
        vector<vector<int>> result = {intervals[0]};
        
        // Iterate through the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval in the result
            vector<int>& last = result.back();
            
            // If the current interval overlaps with the last interval, merge them
            if (intervals[i][0] <= last[1]) {
                last[1] = max(last[1], intervals[i][1]);
            } else {
                // Otherwise, add the current interval to the result
                result.push_back(intervals[i]);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: [[1,4],[4,5]]
Output: [[1,5]]

Input: []
Output: []
```

## Key Takeaways
- Sorting the intervals based on their start values allows for efficient merging of overlapping intervals.
- The algorithm has a time complexity of O(n log n) due to the sorting step, where n is the number of intervals.
- The space complexity is O(n) as in the worst-case scenario, the output array can contain all the input intervals (when there are no overlapping intervals).
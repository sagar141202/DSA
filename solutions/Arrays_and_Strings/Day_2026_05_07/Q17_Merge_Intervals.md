# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a collection of intervals where each interval is a pair of integers, such as [1,3] and [2,6]. The overlapping intervals are merged into a single interval, [1,6]. The intervals are sorted based on their start value. The goal is to return the merged collection of intervals. For example, given [[1,3],[2,6],[8,10],[15,18]], the output will be [[1,6],[8,10],[15,18]]. The input intervals are non-empty and are in the form of [start, end] where 0 <= start <= end.

## Approach
The algorithm sorts the intervals based on their start value and then iterates through them, merging any overlapping intervals. If the current interval does not overlap with the previous one, it is added to the result list. The algorithm uses a simple iterative approach to achieve this. It maintains a list of merged intervals and updates it accordingly.

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
        // If the input is empty, return an empty vector
        if (intervals.empty()) {
            return {};
        }
        
        // Sort the intervals based on their start value
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize the result with the first interval
        vector<vector<int>> result = {intervals[0]};
        
        // Iterate through the remaining intervals
        for (int i = 1; i < intervals.size(); i++) {
            // Get the last interval in the result
            vector<int>& last = result.back();
            
            // If the current interval overlaps with the last one, merge them
            if (intervals[i][0] <= last[1]) {
                last[1] = max(last[1], intervals[i][1]);
            } 
            // If the current interval does not overlap, add it to the result
            else {
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
- Sort the intervals based on their start value to simplify the merging process.
- Use a result list to keep track of the merged intervals.
- Iterate through the intervals and merge any overlapping ones.
# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a collection of intervals where each interval is a pair of integers, e.g., [1, 3] represents the interval from 1 to 3. The input intervals are guaranteed to be non-empty. The intervals may be overlapping, and it's required to merge them into non-overlapping intervals. For example, given intervals [[1, 3], [2, 6], [8, 10], [15, 18]], the output should be [[1, 6], [8, 10], [15, 18]]. The intervals should be merged in a way that the start time of the merged interval is the minimum start time of the overlapping intervals, and the end time of the merged interval is the maximum end time of the overlapping intervals.

## Approach
The algorithm sorts the intervals based on their start time and then iterates over the sorted intervals. If the current interval overlaps with the last merged interval, it merges them by updating the end time of the last merged interval. If the current interval does not overlap with the last merged interval, it adds the current interval to the list of merged intervals.

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
        // Sort the intervals based on their start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        for (const auto& interval : intervals) {
            // If the list of merged intervals is empty or the current interval does not overlap with the last merged interval
            if (merged.empty() || merged.back()[1] < interval[0]) {
                // Add the current interval to the list of merged intervals
                merged.push_back(interval);
            } else {
                // Merge the current interval with the last merged interval
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        return merged;
    }
};
```

## Test Cases
```
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Input: [[1, 4], [4, 5]]
Output: [[1, 5]]
```

## Key Takeaways
- Sort the intervals based on their start time to ensure that overlapping intervals are adjacent to each other.
- Use a list to store the merged intervals and update the last merged interval when an overlapping interval is found.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the merged intervals.
# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a collection of pairs of integers, where each pair represents the start and end of an interval. The input intervals are guaranteed to be non-empty and may have overlapping intervals. The goal is to return a new collection of non-overlapping intervals that cover all the intervals in the input. For example, given the intervals [[1,3],[2,6],[8,10],[15,18]], the output should be [[1,6],[8,10],[15,18]]. The intervals can be merged if they have any overlap, i.e., if the start of one interval is less than or equal to the end of another interval.

## Approach
The algorithm sorts the intervals based on their start value and then iterates through the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged correctly. The time complexity is optimized by sorting the intervals first. The algorithm uses a simple iterative approach to merge the intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // If the input is empty, return an empty vector
    if (intervals.size() == 0) {
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
        vector<int>& lastInterval = result.back();

        // If the current interval overlaps with the last interval, merge them
        if (intervals[i][0] <= lastInterval[1]) {
            lastInterval[1] = max(lastInterval[1], intervals[i][1]);
        } else {
            // Otherwise, add the current interval to the result
            result.push_back(intervals[i]);
        }
    }

    return result;
}
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
- Sort the intervals based on their start value to ensure that overlapping intervals are merged correctly.
- Use a simple iterative approach to merge the intervals, which reduces the time complexity.
- The space complexity is optimized by only storing the merged intervals in the result vector.
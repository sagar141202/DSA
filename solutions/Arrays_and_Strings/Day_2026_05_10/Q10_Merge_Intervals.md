# Merge Intervals

## Problem Statement
Given a collection of intervals, merge all overlapping intervals. The intervals are represented as a 2D vector where each sub-vector contains two integers representing the start and end of the interval. The input intervals are not guaranteed to be sorted. The task is to return a new vector of merged intervals, where no two intervals overlap. For example, given the intervals `[[1,3],[2,6],[8,10],[15,18]]`, the output should be `[[1,6],[8,10],[15,18]]`.

## Approach
The algorithm sorts the intervals based on their start value and then iterates over the sorted intervals, merging any overlapping intervals. This approach ensures that all overlapping intervals are merged correctly. The sorting step is necessary to ensure that we are always comparing adjacent intervals.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // If the input vector is empty, return an empty vector
    if (intervals.empty()) {
        return {};
    }

    // Sort the intervals based on their start value
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });

    // Initialize the result vector with the first interval
    vector<vector<int>> merged = {intervals[0]};

    // Iterate over the remaining intervals
    for (int i = 1; i < intervals.size(); i++) {
        // Get the last interval in the result vector
        vector<int>& last = merged.back();

        // If the current interval overlaps with the last interval, merge them
        if (intervals[i][0] <= last[1]) {
            last[1] = max(last[1], intervals[i][1]);
        } else {
            // Otherwise, add the current interval to the result vector
            merged.push_back(intervals[i]);
        }
    }

    return merged;
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
- Sorting the intervals based on their start value is necessary to ensure that we are always comparing adjacent intervals.
- We only need to compare each interval with the last interval in the result vector to determine if they overlap.
- The time complexity of the algorithm is O(n log n) due to the sorting step, where n is the number of intervals.
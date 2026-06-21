# Minimum Number of Arrows to Burst Balloons

## Problem Statement
Given a 2D array `points` where `points[i] = [x_start, x_end]` represents a balloon, where `x_start` and `x_end` are the start and end points of the balloon on the x-axis, find the minimum number of arrows needed to burst all the balloons. The constraint is that if two balloons overlap, one arrow can burst both of them. For example, if we have `points = [[10,16],[2,8],[1,6],[7,12]]`, the minimum number of arrows needed is 2.

## Approach
The approach to solve this problem is to use a greedy algorithm, sorting the balloons by their end points and then iterating through the sorted list to find the minimum number of arrows needed. This is because if we burst a balloon at its end point, we can burst all the balloons that overlap with it.

## Complexity
- Time: O(n log n) due to sorting
- Space: O(1) as we only use a constant amount of space

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    // If there are no balloons, return 0
    if (points.size() == 0) return 0;

    // Sort the balloons by their end points
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });

    // Initialize the count of arrows and the end point of the last burst balloon
    int count = 1;
    int last = points[0][1];

    // Iterate through the sorted list to find the minimum number of arrows needed
    for (int i = 1; i < points.size(); i++) {
        // If the current balloon does not overlap with the last burst balloon, increment the count and update the last end point
        if (points[i][0] > last) {
            count++;
            last = points[i][1];
        }
    }

    return count;
}
```

## Test Cases
```
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the balloons by their end points to ensure that we burst the balloons that overlap with each other.
- Use a greedy algorithm to find the minimum number of arrows needed, as it allows us to make the locally optimal choice of bursting the balloon at its end point.
- The time complexity of the solution is O(n log n) due to sorting, and the space complexity is O(1) as we only use a constant amount of space.
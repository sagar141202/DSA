# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a certain range of values where it will burst when shot with an arrow. The ranges are represented by intervals of the form [start, end], where start and end are the start and end points of the interval respectively. The goal is to find the minimum number of arrows required to burst all the balloons. The constraint is that if two balloons have overlapping intervals, one arrow can burst both of them.

## Approach
The algorithm sorts the balloons based on their end points and then iterates over the sorted balloons, using a greedy approach to find the minimum number of arrows required. If the current balloon's start point is greater than the end point of the previous arrow, a new arrow is needed.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    // If there are no balloons, return 0
    if (points.size() == 0) return 0;
    
    // Sort the balloons based on their end points
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    
    // Initialize the count of arrows and the position of the previous arrow
    int count = 1;
    int pos = points[0][1];
    
    // Iterate over the sorted balloons
    for (int i = 1; i < points.size(); i++) {
        // If the current balloon's start point is greater than the position of the previous arrow,
        // a new arrow is needed
        if (points[i][0] > pos) {
            count++;
            pos = points[i][1];
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
- Sort the balloons based on their end points to ensure that we can burst as many balloons as possible with each arrow.
- Use a greedy approach to find the minimum number of arrows required, by only using a new arrow when the current balloon's start point is greater than the position of the previous arrow.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) if we consider the input as part of the space complexity.
# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons moving in a straight line on the x-axis at different speeds. Each balloon has a certain point at which it will burst, represented by an array of intervals where each interval is of the form [start, end]. The task is to find the minimum number of arrows required to burst all the balloons. An arrow can burst a balloon if it is shot at any point within the interval of the balloon. If two balloons have overlapping intervals, one arrow can burst both of them.

## Approach
The algorithm sorts the intervals by their end points and iterates over them, maintaining a count of the minimum number of arrows needed so far and the position of the last arrow shot. If the current balloon's start point is greater than the last arrow's position, a new arrow is needed.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    
    // Sort the intervals by their end points
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    
    int count = 1;
    int last = points[0][1];
    
    for (int i = 1; i < points.size(); i++) {
        // If the current balloon's start point is greater than the last arrow's position, a new arrow is needed
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
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the intervals by their end points to ensure that we consider the balloon that ends first and can potentially be burst by an arrow shot at a later balloon.
- Maintain a count of the minimum number of arrows needed so far and the position of the last arrow shot to efficiently determine when a new arrow is needed.
- The algorithm has a time complexity of O(n log n) due to the sorting step and a space complexity of O(n) for storing the input intervals.
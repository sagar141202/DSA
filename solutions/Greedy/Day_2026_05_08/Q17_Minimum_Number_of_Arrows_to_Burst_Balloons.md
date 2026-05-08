# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons tied to a line, and it is given that each balloon has an associated start and end point on the line, represented as an array of pairs `[start, end]`. The goal is to find the minimum number of arrows required to burst all the balloons. An arrow can burst all balloons in a range if it is shot at any point within that range. The input array is not sorted, and the balloons may overlap.

## Approach
The approach involves sorting the balloons by their end points, then iterating over them and keeping track of the end point of the last burst balloon. If the current balloon's start point is greater than the last burst balloon's end point, a new arrow is needed. The intuition is to always burst the balloon that ends first.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        // If there are no balloons, no arrows are needed
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end points
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int count = 1;  // Initialize the count of arrows
        int lastEnd = points[0][1];  // Initialize the end point of the last burst balloon
        
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon's start point is greater than the last burst balloon's end point,
            // a new arrow is needed
            if (points[i][0] > lastEnd) {
                count++;
                lastEnd = points[i][1];
            }
        }
        
        return count;
    }
};
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
- The problem can be solved using a greedy approach by sorting the balloons by their end points.
- The key insight is to always burst the balloon that ends first.
- The time complexity is O(n log n) due to the sorting step.
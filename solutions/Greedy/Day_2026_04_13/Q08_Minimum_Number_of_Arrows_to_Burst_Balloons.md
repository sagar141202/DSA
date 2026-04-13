# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a certain number of arrows, and each arrow can burst a balloon. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals on the x-axis, where the start position is the first element of the interval and the end position is the second element. Two balloons can be burst by one arrow if they overlap, i.e., if the start position of one balloon is less than or equal to the end position of the other balloon. The input is a 2D vector of integers, where each vector represents a balloon. The output is the minimum number of arrows needed to burst all the balloons. For example, if the input is [[10,16],[2,8],[1,6],[7,12]], the output is 2, because two arrows can burst all the balloons.

## Approach
The algorithm sorts the balloons based on their end positions and then iterates over the sorted balloons, using a greedy approach to find the minimum number of arrows. If the current balloon does not overlap with the previous one, a new arrow is needed. The intuition is to always try to burst the current balloon with the previous arrow if possible.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) {
        return 0;
    }
    
    // Sort the points based on their end positions
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    
    int arrows = 1;
    int currentEnd = points[0][1];
    
    // Iterate over the sorted points
    for (int i = 1; i < points.size(); i++) {
        // If the current point does not overlap with the previous one, a new arrow is needed
        if (points[i][0] > currentEnd) {
            arrows++;
            currentEnd = points[i][1];
        }
    }
    
    return arrows;
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
- The problem can be solved using a greedy approach by sorting the balloons based on their end positions.
- The time complexity is O(n log n) due to the sorting operation.
- The space complexity is O(n) for the input and output.
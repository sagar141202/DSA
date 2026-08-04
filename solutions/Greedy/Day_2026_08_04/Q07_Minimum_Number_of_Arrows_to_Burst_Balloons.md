# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D array `points` where `points[i] = [start, end]`. The start and end positions are non-negative integers, and the start position is always less than or equal to the end position.

## Approach
The problem can be solved using a greedy algorithm by first sorting the balloons based on their end positions. Then, we initialize the end position of the last burst balloon and the count of arrows. We iterate over the sorted balloons, and if the current balloon's start position is greater than the last burst balloon's end position, we increment the arrow count and update the last burst balloon's end position.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    int end = points[0][1];
    int count = 1;
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > end) {
            count++;
            end = points[i][1];
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
```

## Key Takeaways
- Sort the balloons based on their end positions to ensure that we burst the balloons with the earliest end positions first.
- Initialize the end position of the last burst balloon and the count of arrows to keep track of the minimum number of arrows needed.
- Iterate over the sorted balloons and update the count and end position as necessary to find the minimum number of arrows.
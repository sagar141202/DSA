# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D vector, where each sub-vector contains two integers representing the start and end positions of a balloon. For example, `[[10,16],[2,8],[1,6],[7,12]]` represents four balloons with start and end positions 10-16, 2-8, 1-6, and 7-12 respectively.

## Approach
The approach to solve this problem is to use a greedy algorithm. We first sort the balloons based on their end positions. Then, we initialize the count of arrows and the position of the last arrow. We iterate over the sorted balloons and check if the current balloon can be burst by the last arrow. If not, we increment the count of arrows and update the position of the last arrow.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int arrows = 1;
    int last = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > last) {
            arrows++;
            last = points[i][1];
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
- Sort the balloons based on their end positions to ensure that we are considering the balloon with the earliest end position first.
- Use a greedy approach to find the minimum number of arrows needed to burst all the balloons.
- Keep track of the position of the last arrow to determine if the current balloon can be burst by the last arrow.
# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented by a 2D vector, where each element is a pair of two integers representing the start and end positions of a balloon.

## Approach
The algorithm sorts the balloons by their end positions and then iterates over them, using a greedy approach to find the minimum number of arrows. If the current balloon's start position is greater than the previous arrow's end position, a new arrow is needed.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int count = 1;
    int pos = points[0][1];
    for (int i = 1; i < points.size(); i++) {
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
- Sort the balloons by their end positions to ensure that we can burst as many balloons as possible with each arrow.
- Use a greedy approach to find the minimum number of arrows, by only using a new arrow when the current balloon's start position is greater than the previous arrow's end position.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the sorting step in the worst case.
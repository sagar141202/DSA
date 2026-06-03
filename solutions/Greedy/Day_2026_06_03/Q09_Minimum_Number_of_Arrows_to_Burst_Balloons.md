# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons floating in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D vector, where each inner vector contains two integers representing the start and end positions of a balloon.

## Approach
The problem can be solved using a greedy algorithm by first sorting the balloons based on their end positions. Then, we initialize the end position of the last burst balloon and the count of arrows. We iterate over the sorted balloons, and if the start position of the current balloon is greater than the end position of the last burst balloon, we increment the count of arrows and update the end position of the last burst balloon.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int arrow = 1;
        int lastEnd = points[0][1];
        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > lastEnd) {
                arrow++;
                lastEnd = points[i][1];
            }
        }
        return arrow;
    }
};
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
- Use a greedy approach to minimize the number of arrows needed by only bursting a new balloon when the current arrow cannot burst it.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) as we only use a constant amount of space.
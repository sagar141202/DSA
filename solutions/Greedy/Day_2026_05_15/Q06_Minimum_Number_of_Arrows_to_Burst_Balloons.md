# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons, each attached to a dartboard at a specific point. The points are represented as pairs of integers, where the first integer is the start of the balloon and the second integer is the end of the balloon. You are given a list of these points, and you want to find the minimum number of arrows you need to burst all the balloons. An arrow can burst all the balloons in a range if the range is [start, end] and the arrow is shot at any point x where start <= x <= end. The input is a list of pairs of integers, and the output is the minimum number of arrows needed to burst all the balloons. For example, given the input [[10,16],[2,8],[1,6],[7,12]], the output is 2.

## Approach
The algorithm sorts the balloons by their end points and then iterates over them, using a variable to keep track of the end point of the last burst balloon. If the current balloon's start point is greater than the last burst balloon's end point, a new arrow is needed. The algorithm uses a greedy approach to minimize the number of arrows.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.empty()) return 0;
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    int count = 1;
    int lastEnd = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > lastEnd) {
            count++;
            lastEnd = points[i][1];
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
- Sort the balloons by their end points to ensure that we are considering the balloons that end earliest first.
- Use a greedy approach to minimize the number of arrows by only using a new arrow when necessary.
- Keep track of the end point of the last burst balloon to determine when a new arrow is needed.
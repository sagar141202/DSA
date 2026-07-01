# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons floating in the air, and each balloon has a start and end point. You have a certain number of arrows, and each arrow can burst a balloon. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals, where each interval is a pair of integers representing the start and end points of the balloon. The arrows can be shot at any point on the x-axis, and a balloon is burst if the arrow is shot at a point within the balloon's interval. For example, if we have the intervals [[10,16],[2,8],[1,6],[7,12]], we can burst all the balloons with 2 arrows, one shot at point 6 and one shot at point 11. The constraints are that the number of balloons is between 1 and 10^4, and the start and end points of each balloon are between 1 and 10^6.

## Approach
The algorithm sorts the balloons by their end points and then iterates over them, keeping track of the end point of the last burst balloon. If the current balloon's start point is greater than the last burst balloon's end point, a new arrow is needed. The algorithm uses a greedy approach, always trying to burst the current balloon with the last arrow if possible.

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
        // If there are no balloons, we don't need any arrows
        if (points.empty()) return 0;

        // Sort the balloons by their end points
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        // Initialize the number of arrows and the end point of the last burst balloon
        int arrows = 1;
        int last_end = points[0][1];

        // Iterate over the balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon's start point is greater than the last burst balloon's end point,
            // a new arrow is needed
            if (points[i][0] > last_end) {
                arrows++;
                last_end = points[i][1];
            }
        }

        return arrows;
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
- The greedy approach is suitable for this problem, as it always tries to burst the current balloon with the last arrow if possible.
- Sorting the balloons by their end points is crucial, as it allows us to efficiently determine whether a new arrow is needed.
- The algorithm has a time complexity of O(n log n) due to the sorting step, and a space complexity of O(n) for storing the sorted balloons.
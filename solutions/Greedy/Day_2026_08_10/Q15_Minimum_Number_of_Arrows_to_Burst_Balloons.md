# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D vector, where each element is a vector of two integers representing the start and end positions of a balloon.

## Approach
The algorithm sorts the balloons based on their end positions and then uses a greedy approach to find the minimum number of arrows. It iterates through the sorted balloons and checks if the current balloon can be burst by the previous arrow. If not, a new arrow is used.

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

        // Sort the balloons based on their end positions
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int arrows = 1;
        int pos = points[0][1];

        // Iterate through the sorted balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon can be burst by the previous arrow, skip it
            if (points[i][0] <= pos) continue;
            // Otherwise, use a new arrow
            arrows++;
            pos = points[i][1];
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
- Sorting the balloons based on their end positions is crucial for the greedy approach to work.
- The algorithm uses a single pass through the sorted balloons to find the minimum number of arrows.
- The time complexity is O(n log n) due to the sorting step, where n is the number of balloons.
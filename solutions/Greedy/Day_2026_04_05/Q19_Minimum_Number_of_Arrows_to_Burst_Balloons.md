# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. We have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented by a 2D vector, where each sub-vector contains two integers representing the start and end positions of a balloon. For example, `[[10,16],[2,8],[1,6],[7,12]]` represents four balloons with start and end positions.

## Approach
The algorithm sorts the balloons based on their end positions and then iterates over them, using a greedy approach to find the minimum number of arrows. The idea is to burst as many balloons as possible with each arrow, so we always try to burst the balloons with the earliest end position.

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
        // If there are no balloons, return 0
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end positions
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Initialize the count of arrows and the position of the last arrow
        int count = 1;
        int last = points[0][1];
        
        // Iterate over the balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon is not burst by the last arrow, increment the count and update the last position
            if (points[i][0] > last) {
                count++;
                last = points[i][1];
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
- Sort the balloons by their end positions to ensure that we burst as many balloons as possible with each arrow.
- Use a greedy approach to find the minimum number of arrows, always trying to burst the balloons with the earliest end position.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the balloons.
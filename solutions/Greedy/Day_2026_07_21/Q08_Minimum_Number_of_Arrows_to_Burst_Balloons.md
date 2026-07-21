# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst a balloon. However, if two balloons overlap (i.e., one balloon's start position is less than or equal to another balloon's end position), one arrow can burst both of them. Given the start and end positions of the balloons, find the minimum number of arrows required to burst all the balloons. The input will be a vector of pairs, where each pair represents the start and end positions of a balloon.

## Approach
The approach is to sort the balloons by their end positions and then use a greedy strategy to find the minimum number of arrows. We initialize the end position of the current arrow and the count of arrows. Then, we iterate over the sorted balloons and update the end position and the count as necessary.

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
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end positions
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int end = points[0][1];
        int count = 1;
        
        // Iterate over the sorted balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon does not overlap with the current arrow, update the end position and the count
            if (points[i][0] > end) {
                end = points[i][1];
                count++;
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
- Sort the balloons by their end positions to ensure that we consider the balloons that end earliest first.
- Use a greedy strategy to find the minimum number of arrows by iterating over the sorted balloons and updating the end position and the count as necessary.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the input and output.
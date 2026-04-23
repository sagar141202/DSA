# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons, each with a start and end value. The task is to find the minimum number of arrows that can burst all the balloons. An arrow can burst a balloon if it is shot within the range of the balloon. The input is an array of pairs, where each pair represents the start and end value of a balloon. The output should be the minimum number of arrows required to burst all the balloons. For example, given the input `[[10,16],[2,8],[1,6],[7,12]]`, the output should be `2`, because two arrows can burst all the balloons.

## Approach
The approach is to sort the balloons by their end values and then use a greedy algorithm to find the minimum number of arrows. The idea is to always try to burst the current balloon with the previous arrow if possible.

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
        
        // Sort the balloons by their end values
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Initialize the count of arrows and the position of the last arrow
        int count = 1;
        int lastArrow = points[0][1];
        
        // Iterate over the balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon cannot be burst by the last arrow, increment the count and update the last arrow
            if (points[i][0] > lastArrow) {
                count++;
                lastArrow = points[i][1];
            }
        }
        
        // Return the minimum number of arrows
        return count;
    }
};
```

## Test Cases
```
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Input: [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the balloons by their end values to ensure that we can burst the maximum number of balloons with each arrow.
- Use a greedy algorithm to find the minimum number of arrows, by always trying to burst the current balloon with the previous arrow if possible.
- The time complexity is O(n log n) due to the sorting, and the space complexity is O(n) for the input array.
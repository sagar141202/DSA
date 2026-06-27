# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. The goal is to find the minimum number of arrows required to burst all the balloons. An arrow can burst all the balloons in a range if the range is covered by the arrow. The input is an array of pairs where each pair represents the start and end position of a balloon. The constraint is that the input array can have at most 10^5 pairs, and the start and end positions are between 1 and 10^6.

## Approach
The approach to solve this problem is to use a greedy algorithm by first sorting the balloons based on their end positions. Then, we initialize the count of arrows and the position of the last arrow. We iterate through the sorted balloons, and for each balloon, we check if it can be burst by the last arrow. If not, we increment the count of arrows and update the position of the last arrow.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.empty()) return 0;
    
    // Sort the balloons based on their end positions
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int count = 1;
    int last = points[0][1];
    
    // Iterate through the sorted balloons
    for (int i = 1; i < points.size(); i++) {
        // Check if the current balloon can be burst by the last arrow
        if (points[i][0] > last) {
            count++;
            last = points[i][1];
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
- The key to solving this problem is to sort the balloons based on their end positions.
- The greedy approach ensures that we use the minimum number of arrows to burst all the balloons.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) as we only use a constant amount of space.
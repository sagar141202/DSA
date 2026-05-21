# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and you have a certain number of arrows to burst them. Each balloon has a start and end point, and if an arrow is shot at a point within the range of a balloon, it will burst. Given a list of balloons, where each balloon is represented as a pair of integers (start, end), find the minimum number of arrows needed to burst all the balloons. The input list will not be empty and will contain at least one balloon. The start and end points of each balloon will be distinct. For example, given the input [[10,16],[2,8],[1,6],[7,12]], the output will be 2.

## Approach
The problem can be solved using a greedy approach by first sorting the balloons based on their end points. Then, we can iterate through the sorted list and keep track of the end point of the last burst balloon. If the current balloon's start point is greater than the last burst balloon's end point, we need to use a new arrow.

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
        // If the input list is empty, return 0
        if (points.empty()) {
            return 0;
        }

        // Sort the balloons based on their end points
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;  // Initialize the count of arrows
        int lastEnd = points[0][1];  // Initialize the end point of the last burst balloon

        // Iterate through the sorted list of balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon's start point is greater than the last burst balloon's end point
            if (points[i][0] > lastEnd) {
                count++;  // Increment the count of arrows
                lastEnd = points[i][1];  // Update the end point of the last burst balloon
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
Input: [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

## Key Takeaways
- Sort the balloons based on their end points to ensure that we can burst the maximum number of balloons with the minimum number of arrows.
- Keep track of the end point of the last burst balloon to determine if a new arrow is needed.
- The time complexity of the solution is O(n log n) due to the sorting operation.
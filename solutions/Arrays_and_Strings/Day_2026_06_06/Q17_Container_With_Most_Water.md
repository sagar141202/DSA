# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this area of water, which the container contains. The width of the container is the distance between the two lines, and the height of the container is the minimum of the two lines.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array, and moving the pointer with the smaller height towards the center. This ensures that we consider all possible containers and find the one with the maximum area.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        // Initialize two pointers, one at the start and one at the end of the array
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;
        
        // Continue the loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            // Calculate the height of the container, which is the minimum of the two lines
            int minHeight = min(height[left], height[right]);
            // Calculate the area of the container
            int area = width * minHeight;
            // Update the maximum area if the current area is larger
            maxArea = max(maxArea, area);
            // Move the pointer with the smaller height towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
};
```

## Test Cases
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Input: height = [1,1]
Output: 1
```

## Key Takeaways
- Use a two-pointer approach to consider all possible containers and find the one with the maximum area.
- The height of the container is the minimum of the two lines, and the width is the distance between the two lines.
- Move the pointer with the smaller height towards the center to ensure that we consider all possible containers.
# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximum. The width of the container is the difference between the x-coordinates of the two lines, and the height of the container is the minimum of the two lines. The area of the container is the product of the width and the height.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated at each step, and the maximum area is updated accordingly. The pointer with the shorter line is moved towards the center, as moving the pointer with the taller line wouldn't increase the area.

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
        
        // Initialize the maximum area
        int maxArea = 0;
        
        // Loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            
            // Calculate the height of the container
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of the container
            int area = width * minHeight;
            
            // Update the maximum area
            maxArea = max(maxArea, area);
            
            // Move the pointer with the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        // Return the maximum area
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
- The two-pointer approach is used to solve this problem efficiently.
- The area of water that can be trapped between two lines is calculated at each step, and the maximum area is updated accordingly.
- The pointer with the shorter line is moved towards the center, as moving the pointer with the taller line wouldn't increase the area.
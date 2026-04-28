# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The width of the container is the distance between the two lines, and the height of the container is the minimum of the two lines. The area of water the container contains is the product of its width and height. The constraint is that the lines are non-negative and there are at least two lines.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated as the product of the distance between the lines and the minimum height of the two lines. The maximum area is updated at each step.

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
        int maxArea = 0;
        int left = 0;
        int right = height.size() - 1;
        
        // Loop through the array from both ends
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            
            // Calculate the height of the container
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of water that can be trapped
            int area = width * minHeight;
            
            // Update the maximum area
            maxArea = max(maxArea, area);
            
            // Move the pointer of the shorter line towards the center
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
- The two-pointer approach is used to reduce the time complexity to O(n).
- The maximum area is updated at each step, and the pointer of the shorter line is moved towards the center.
- The height of the container is the minimum of the two lines, and the width is the distance between the lines.
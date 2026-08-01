# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximum. The width of the container is the difference between the x-coordinates of the two lines, and the height of the container is the minimum of the two lines. The area of the container is the product of its width and height.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The intuition is to maximize the area by considering the maximum possible width and height at each step.

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
        
        // Move the pointers towards the center
        while (left < right) {
            // Calculate the width and height of the current container
            int width = right - left;
            int minHeight = min(height[left], height[right]);
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
- Use a two-pointer approach to maximize the area by considering the maximum possible width and height at each step.
- Move the pointer of the shorter line towards the center to potentially increase the area.
- The time complexity is O(n) and the space complexity is O(1), making the solution efficient for large inputs.
# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. Constraints: 2 <= length of array <= 10^5, 0 <= height of array <= 10^4, and the array is not empty. Example: Input: height = [1,8,6,2,5,4,8,3,7], Output: 49.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped is calculated at each step, and the maximum area is updated accordingly. This approach ensures that all possible containers are considered.

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
        // Initialize two pointers, one at the beginning and one at the end of the array
        int left = 0;
        int right = height.size() - 1;
        
        // Initialize the maximum area
        int maxArea = 0;
        
        // Loop through the array until the two pointers meet
        while (left < right) {
            // Calculate the width of the current container
            int width = right - left;
            
            // Calculate the height of the current container, which is the minimum of the two lines
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of the current container
            int area = width * minHeight;
            
            // Update the maximum area if the current area is larger
            maxArea = max(maxArea, area);
            
            // Move the pointer of the shorter line towards the center
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
Input: height = [4,3,2,1,4]
Output: 16
```

## Key Takeaways
- The two-pointer approach is useful for problems that involve finding the maximum or minimum of something in an array.
- The area of the container is calculated as the product of the width and the minimum height of the two lines.
- The pointer of the shorter line is moved towards the center because the area of the container is limited by the shorter line.
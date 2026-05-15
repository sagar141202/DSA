# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of the water it contains is maximal. The program should return this max area. The height of each line is given by the array height = [a1, a2, ..., an]. The width of the container is the difference between the x-coordinates of the lines.

## Approach
We can solve this problem using a two-pointer approach, starting from both ends of the array and moving towards the center. The area of the container is determined by the shorter line, so we move the pointer of the shorter line towards the center.

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
        // Initialize two pointers, one at the beginning and one at the end
        int left = 0;
        int right = height.size() - 1;
        
        // Initialize the max area
        int maxArea = 0;
        
        // Loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            
            // Calculate the height of the container, which is the minimum of the two lines
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of the container
            int area = width * minHeight;
            
            // Update the max area if the current area is larger
            maxArea = max(maxArea, area);
            
            // Move the pointer of the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        // Return the max area
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
- The two-pointer approach can be used to solve this problem efficiently.
- The area of the container is determined by the shorter line, so we move the pointer of the shorter line towards the center.
- The time complexity of this solution is O(n), where n is the number of lines.
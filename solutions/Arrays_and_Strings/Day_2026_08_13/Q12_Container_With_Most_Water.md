# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is the maximum. The width of the container is the distance between the two lines, and the height of the container is the minimum height of the two lines. The area of the container is the product of its width and height. Constraints: 2 <= a.length <= 10^5, 0 <= a[i] <= 10^4, a is a non-empty array.

## Approach
The algorithm uses two pointers, one starting from the beginning of the array and one from the end. The pointers move towards each other based on the height of the lines. The area of water that can be trapped between the two lines is calculated at each step, and the maximum area found so far is updated.

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
        
        // Initialize the maximum area found so far
        int max_area = 0;
        
        // Loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            
            // Calculate the height of the container, which is the minimum height of the two lines
            int min_height = min(height[left], height[right]);
            
            // Calculate the area of the container
            int area = width * min_height;
            
            // Update the maximum area found so far
            max_area = max(max_area, area);
            
            // Move the pointer of the shorter line towards the other pointer
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        // Return the maximum area found
        return max_area;
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
- Use two pointers to solve this problem efficiently.
- The area of the container is the product of its width and height.
- Move the pointer of the shorter line towards the other pointer to maximize the area.
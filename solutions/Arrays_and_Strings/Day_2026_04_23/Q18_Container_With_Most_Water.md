# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The height of the water is determined by the shorter line, and the width is determined by the distance between the lines. For example, given the array [1,8,6,2,5,4,8,3,7], the maximum area that can be trapped between two vertical lines is 49.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array. The area between the two pointers is calculated, and the pointer with the shorter height is moved towards the other pointer. This process continues until the two pointers meet.

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
        int max_area = 0;
        
        // Continue the process until the two pointers meet
        while (left < right) {
            // Calculate the width of the area
            int width = right - left;
            
            // Calculate the height of the area, which is the minimum of the heights at the two pointers
            int min_height = min(height[left], height[right]);
            
            // Calculate the area
            int area = width * min_height;
            
            // Update the maximum area if the current area is larger
            max_area = max(max_area, area);
            
            // Move the pointer with the shorter height towards the other pointer
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        // Return the maximum area
        return max_area;
    }
};
```

## Test Cases
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Input: [1,1]
Output: 1
```

## Key Takeaways
- The two-pointer approach is used to solve the problem efficiently.
- The area between the two pointers is calculated, and the pointer with the shorter height is moved towards the other pointer.
- The process continues until the two pointers meet, at which point the maximum area has been found.
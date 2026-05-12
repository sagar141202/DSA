# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. For example, given the height [1,8,6,2,5,4,8,3,7], the max area is 49.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area between two lines is calculated as the minimum height times the distance between them. The maximum area found so far is updated at each step.

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
        int maxArea = 0;
        
        // Loop until the two pointers meet
        while (left < right) {
            // Calculate the area between the two lines
            int area = min(height[left], height[right]) * (right - left);
            // Update the maximum area if the current area is larger
            maxArea = max(maxArea, area);
            // Move the pointer of the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        // Return the maximum area found
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
- Use a two-pointer approach to efficiently find the maximum area.
- The area between two lines is calculated as the minimum height times the distance between them.
- Move the pointer of the shorter line towards the center to potentially increase the area.
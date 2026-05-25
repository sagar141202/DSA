# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is the maximum. The width of the container is the distance between the two lines. The height of the container is the minimum height of the two lines. The area of the container is the product of its width and height. The constraint is that the lines must be non-negative. For example, given the array [1,8,6,2,5,4,8,3,7], the output is 49.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped is calculated at each step, and the maximum area is updated accordingly. This approach ensures that all possible combinations of lines are considered.

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
        
        // Continue the loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            
            // Calculate the height of the container
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of the container
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
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Input: [1,1]
Output: 1
```

## Key Takeaways
- The two-pointer approach is useful for solving problems that require considering all possible combinations of elements in an array.
- The time complexity of the solution is O(n), where n is the number of elements in the array, because each element is visited at most once.
- The space complexity of the solution is O(1), because only a constant amount of space is used to store the pointers and the maximum area.
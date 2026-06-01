# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. The constraints are 2 <= a.length <= 105, 0 <= a[i] <= 104, and a[i] are non-negative integers.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area between two lines is calculated as the minimum height of the two lines times the distance between them. The maximum area is updated at each step.

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
            // Calculate the width of the current area
            int width = right - left;
            
            // Calculate the height of the current area
            int minHeight = min(height[left], height[right]);
            
            // Calculate the current area
            int currentArea = width * minHeight;
            
            // Update the maximum area if the current area is larger
            maxArea = max(maxArea, currentArea);
            
            // Move the pointer at the shorter line towards the other end
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
- Use a two-pointer approach to solve this problem efficiently.
- The area between two lines is determined by the minimum height of the two lines and the distance between them.
- Move the pointer at the shorter line towards the other end to potentially increase the area.
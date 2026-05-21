# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximum. The program should return this maximum area. The constraints are 2 <= a.length <= 10^5 and 0 <= a[i] <= 10^4.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated as the minimum height of the two lines multiplied by the distance between them. The maximum area is updated at each step.

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
- Use a two-pointer approach to solve the problem efficiently.
- Calculate the area of water that can be trapped between two lines at each step.
- Update the maximum area whenever a larger area is found.
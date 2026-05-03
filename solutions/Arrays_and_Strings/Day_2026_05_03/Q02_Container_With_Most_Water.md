# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this maximal area. For example, given the height [1,8,6,2,5,4,8,3,7], the output should be 49.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated as the minimum height of the two lines multiplied by the distance between them. The maximum area found so far is updated at each step.

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
        int max_area = 0;
        int left = 0;
        int right = height.size() - 1;
        
        // Calculate the area of water that can be trapped between two lines
        while (left < right) {
            int h = min(height[left], height[right]);
            int w = right - left;
            max_area = max(max_area, h * w);
            
            // Move the pointer of the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
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
- Use a two-pointer approach to solve the problem efficiently.
- The area of water that can be trapped between two lines is determined by the minimum height of the two lines.
- Move the pointer of the shorter line towards the center to explore other possible solutions.
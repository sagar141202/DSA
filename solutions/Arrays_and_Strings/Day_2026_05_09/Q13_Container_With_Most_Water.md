# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. Constraints: 2 <= a.length <= 105, 0 <= a[i] <= 104, a is sorted in non-decreasing order.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array. The width of the container is the difference between the two pointers, and the height is the minimum of the two lines. The area is calculated as the product of the width and height. The pointers are moved based on which line is shorter.

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
        
        while (left < right) {
            // Calculate the width and height of the container
            int width = right - left;
            int minHeight = min(height[left], height[right]);
            
            // Calculate the area of the container
            int area = width * minHeight;
            
            // Update the max area if the current area is larger
            maxArea = max(maxArea, area);
            
            // Move the pointer of the shorter line
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
- The two-pointer approach is effective in solving problems that involve finding a maximum or minimum value in an array.
- The key to this problem is to realize that the area of the container is determined by the shorter line, so moving the pointer of the shorter line will not decrease the area.
- The time complexity is O(n) because we only need to traverse the array once. The space complexity is O(1) because we only use a constant amount of space to store the pointers and the max area.
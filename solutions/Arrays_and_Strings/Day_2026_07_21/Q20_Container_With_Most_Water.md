# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area, and the constraints are 2 <= a.length <= 105, 0 <= a[i] <= 104, a.length >= 2.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array. It calculates the area between the two lines and updates the maximum area. The pointer with the smaller height is moved towards the other pointer, as moving the pointer with the larger height wouldn't increase the area.

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
        
        // Calculate the area and update maxArea
        while (left < right) {
            int minHeight = min(height[left], height[right]);
            int width = right - left;
            int area = minHeight * width;
            maxArea = max(maxArea, area);
            
            // Move the pointer with the smaller height
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
- The two-pointer approach can be used to solve problems that involve finding a maximum or minimum value in an array.
- The key to this problem is to realize that the area of the container is determined by the smaller height of the two lines.
- Moving the pointer with the smaller height towards the other pointer is the optimal strategy to find the maximum area.
# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of the water it contains is maximal. The program should return this area of water, which the container contains. The width is the distance between each line, for example, the area between the first and the second line is 1. The height is the minimum height of the two lines.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water is calculated at each step, and the maximum area is updated accordingly. The pointer with the smaller height is moved towards the center, as moving the pointer with the larger height would not increase the area.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height) {
    int maxArea = 0;
    int left = 0;
    int right = height.size() - 1;
    
    // Calculate the area at each step and update the maximum area
    while (left < right) {
        int currentArea = min(height[left], height[right]) * (right - left);
        maxArea = max(maxArea, currentArea);
        
        // Move the pointer with the smaller height towards the center
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
```

## Test Cases
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Input: height = [1,1]
Output: 1
```

## Key Takeaways
- The two-pointer approach is useful for solving problems that involve finding a maximum or minimum value in an array.
- The key to solving this problem is to realize that the area of water is determined by the minimum height of the two lines, and that moving the pointer with the larger height would not increase the area.
- The time complexity is O(n) because we are scanning the array once, and the space complexity is O(1) because we are using a constant amount of space.
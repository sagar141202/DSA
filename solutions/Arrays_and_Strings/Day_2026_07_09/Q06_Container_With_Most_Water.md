# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. The width of each line is 1. The constraints are 2 <= length of array <= 10^5 and 0 <= height of each line <= 10^4.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array. It calculates the area between the two lines and updates the max area. The pointer with the smaller height is moved towards the other end.

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
        
        // loop until the two pointers meet
        while (left < right) {
            // calculate the width
            int width = right - left;
            
            // calculate the height
            int minHeight = min(height[left], height[right]);
            
            // calculate the area
            int area = width * minHeight;
            
            // update the max area
            maxArea = max(maxArea, area);
            
            // move the pointer with the smaller height
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
- The area of water contained is determined by the width and the minimum height of the two lines.
- Move the pointer with the smaller height towards the other end to potentially increase the area.
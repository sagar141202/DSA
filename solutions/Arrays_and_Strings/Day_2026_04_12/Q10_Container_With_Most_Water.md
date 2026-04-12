# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this max area. The constraints are 2 <= a.length <= 10^5 and 0 <= a[i] <= 10^4.

## Approach
The algorithm uses a two-pointer approach, starting from both ends of the array and moving towards the center. The area of water that can be trapped is calculated at each step, and the maximum area is updated accordingly. The pointer with the smaller height is moved towards the center.

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
            // Calculate the area of water that can be trapped
            int area = min(height[left], height[right]) * (right - left);
            maxArea = max(maxArea, area);
            
            // Move the pointer with the smaller height towards the center
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
- The two-pointer approach is useful for solving problems that involve finding the maximum or minimum value in an array.
- The area of water that can be trapped is calculated as the minimum height of the two lines multiplied by the distance between them.
- The pointer with the smaller height is moved towards the center because the area of water that can be trapped is limited by the smaller height.
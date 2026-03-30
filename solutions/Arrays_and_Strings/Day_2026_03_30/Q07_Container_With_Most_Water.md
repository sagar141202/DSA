# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is maximal. The program should return this maximal area. The constraints are 2 <= a.length <= 10^5 and 0 <= a[i] <= 10^4.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array, and moving the pointer with the smaller height towards the center. This approach works because the area of water that can be trapped between two lines is determined by the shorter line.

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
        
        // continue the loop until the two pointers meet
        while (left < right) {
            // calculate the area between the two lines
            int area = min(height[left], height[right]) * (right - left);
            
            // update the maxArea if the current area is larger
            maxArea = max(maxArea, area);
            
            // move the pointer with the smaller height towards the center
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
- The area of water that can be trapped between two lines is determined by the shorter line.
- Move the pointer with the smaller height towards the center to find the maximal area.
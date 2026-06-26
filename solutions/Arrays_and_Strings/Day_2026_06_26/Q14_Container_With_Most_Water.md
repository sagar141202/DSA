# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is the maximum. The width of the container is the distance between the two lines, and the height of the container is the minimum height of the two lines. The area of the container is the product of the width and the height. For example, given the array [1,8,6,2,5,4,8,3,7], the maximum area that can be trapped is 49.

## Approach
The algorithm uses a two-pointer approach, starting from the beginning and end of the array. It calculates the area between the two lines at the current pointers and moves the pointer with the smaller height towards the other pointer. This approach ensures that we consider all possible containers and find the maximum area.

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
        // Initialize two pointers, one at the start and one at the end
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;
        
        // Continue the loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            // Calculate the height of the container (minimum height of the two lines)
            int minHeight = min(height[left], height[right]);
            // Calculate the area of the container
            int area = width * minHeight;
            // Update the maximum area if the current area is larger
            maxArea = max(maxArea, area);
            // Move the pointer with the smaller height towards the other pointer
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
- The two-pointer approach is useful for solving problems that involve finding the maximum or minimum value in an array.
- The key to solving this problem is to realize that the area of the container is determined by the minimum height of the two lines.
- By moving the pointer with the smaller height towards the other pointer, we ensure that we consider all possible containers and find the maximum area.
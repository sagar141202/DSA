# Container With Most Water

## Problem Statement
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the area of water it contains is the maximum. The width of the container is the difference between the x-coordinates of the two lines, and the height of the container is the minimum of the two lines. The area of the container is the product of the width and the height. The constraints are 2 <= length of array <= 10^5, and each element in the array is between 1 and 10^4.

## Approach
The approach is to use a two-pointer technique, starting from both ends of the array and moving towards the center. The area of water that can be trapped between two lines is calculated at each step, and the maximum area found so far is updated. The pointer corresponding to the shorter line is moved towards the center because moving the pointer corresponding to the taller line wouldn't increase the area.

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
        // Initialize two pointers, one at the start and one at the end of the array
        int left = 0, right = height.size() - 1;
        // Initialize the maximum area found so far
        int max_area = 0;
        
        // Loop until the two pointers meet
        while (left < right) {
            // Calculate the width of the container
            int width = right - left;
            // Calculate the height of the container
            int min_height = min(height[left], height[right]);
            // Calculate the area of the container
            int area = width * min_height;
            // Update the maximum area found so far
            max_area = max(max_area, area);
            // Move the pointer corresponding to the shorter line towards the center
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        // Return the maximum area found
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
- The two-pointer technique is useful for solving problems that involve finding a maximum or minimum value in an array.
- The key to solving this problem is to realize that the area of the container is determined by the shorter line, so moving the pointer corresponding to the taller line wouldn't increase the area.
- The time complexity of the solution is O(n), where n is the length of the input array, because we only need to traverse the array once.
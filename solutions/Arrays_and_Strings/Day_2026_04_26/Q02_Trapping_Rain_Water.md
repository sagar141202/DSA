# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the corresponding element in the array. The water can be trapped between two bars if the height of the bars is greater than the height of the bars in between. The problem requires finding the maximum amount of water that can be trapped.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. The pointer with the smaller height is moved towards the other pointer, and the amount of water that can be trapped is calculated based on the difference between the maximum height and the current height.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxLeft = 0, maxRight = 0;
        int result = 0;
        
        // Move the pointers towards each other
        while (left <= right) {
            // If the height of the left bar is less than the height of the right bar
            if (height[left] < height[right]) {
                // If the height of the left bar is greater than the maxLeft
                if (height[left] > maxLeft) {
                    // Update maxLeft
                    maxLeft = height[left];
                } else {
                    // Calculate the water that can be trapped
                    result += maxLeft - height[left];
                }
                // Move the left pointer to the right
                left++;
            } else {
                // If the height of the right bar is greater than the maxRight
                if (height[right] > maxRight) {
                    // Update maxRight
                    maxRight = height[right];
                } else {
                    // Calculate the water that can be trapped
                    result += maxRight - height[right];
                }
                // Move the right pointer to the left
                right--;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to track the maximum height of the bars on both sides.
- Move the pointer with the smaller height towards the other pointer.
- Calculate the amount of water that can be trapped based on the difference between the maximum height and the current height.
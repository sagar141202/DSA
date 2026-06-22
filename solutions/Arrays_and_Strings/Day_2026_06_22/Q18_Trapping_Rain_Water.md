# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The bars are represented as lines on a graph, and the water can be trapped between them if there are higher bars on both sides. The goal is to calculate the total amount of water that can be trapped. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. The pointer that points to the shorter bar is moved towards the other pointer, and the trapped water is calculated based on the difference between the maximum height and the current bar height.

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
        
        // Loop through the array from both ends
        while (left <= right) {
            // If the current bar on the left is shorter than the current bar on the right
            if (height[left] < height[right]) {
                // If the current bar on the left is greater than the maxLeft, update maxLeft
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } 
                // Otherwise, add the trapped water to the result
                else {
                    result += maxLeft - height[left];
                }
                // Move the left pointer to the right
                left++;
            } 
            // If the current bar on the right is shorter than or equal to the current bar on the left
            else {
                // If the current bar on the right is greater than the maxRight, update maxRight
                if (height[right] > maxRight) {
                    maxRight = height[right];
                } 
                // Otherwise, add the trapped water to the result
                else {
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
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Input: [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to track the maximum height of the bars on both sides.
- Move the pointer that points to the shorter bar towards the other pointer to calculate the trapped water.
- Update the maximum height of the bars on both sides as the pointers move.
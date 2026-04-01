# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the value at each index in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and the right side of the current bar. The amount of water that can be trapped is the difference between the minimum of the maximum height of the bars on the left and the right, and the height of the current bar. For example, given the array [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers to track the maximum height of the bars on the left and the right. It starts from both ends of the array and moves towards the center, keeping track of the maximum height encountered so far on both sides. The amount of water that can be trapped at each position is calculated as the minimum of the maximum height on the left and the right minus the height of the current bar.

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
        // Initialize variables to store the maximum height on the left and the right
        int leftMax = 0, rightMax = 0;
        // Initialize variables to store the current position of the left and the right pointers
        int left = 0, right = height.size() - 1;
        // Initialize variable to store the total amount of water that can be trapped
        int totalWater = 0;
        
        // Loop through the array until the left and the right pointers meet
        while (left <= right) {
            // If the height of the bar on the left is less than the height of the bar on the right
            if (height[left] < height[right]) {
                // If the height of the bar on the left is greater than the maximum height on the left
                if (height[left] > leftMax) {
                    // Update the maximum height on the left
                    leftMax = height[left];
                } else {
                    // Calculate the amount of water that can be trapped at the current position
                    totalWater += leftMax - height[left];
                }
                // Move the left pointer to the right
                left++;
            } else {
                // If the height of the bar on the right is greater than the maximum height on the right
                if (height[right] > rightMax) {
                    // Update the maximum height on the right
                    rightMax = height[right];
                } else {
                    // Calculate the amount of water that can be trapped at the current position
                    totalWater += rightMax - height[right];
                }
                // Move the right pointer to the left
                right--;
            }
        }
        
        // Return the total amount of water that can be trapped
        return totalWater;
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
- Use two pointers to track the maximum height of the bars on the left and the right.
- Calculate the amount of water that can be trapped at each position as the minimum of the maximum height on the left and the right minus the height of the current bar.
- Move the pointers towards the center of the array based on the height of the bars.
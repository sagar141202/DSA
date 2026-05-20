# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at the corresponding index in the array. The water can be trapped between two bars if the height of the bars is greater than the height of the bars in between. The goal is to calculate the total amount of water that can be trapped.

## Approach
The approach is to use two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. We then calculate the trapped water by finding the minimum of the maximum heights on both sides and subtracting the height of the current bar.

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
        // Initialize variables to store the total trapped water and the maximum heights on both sides
        int totalWater = 0;
        int leftMax = 0;
        int rightMax = 0;
        int left = 0;
        int right = height.size() - 1;
        
        // Loop through the array until the two pointers meet
        while (left <= right) {
            // Update the maximum heights on both sides
            leftMax = max(leftMax, height[left]);
            rightMax = max(rightMax, height[right]);
            
            // If the maximum height on the left is less than the maximum height on the right, update the left pointer
            if (leftMax < rightMax) {
                // Calculate the trapped water and update the total
                totalWater += max(0, leftMax - height[left]);
                left++;
            } 
            // Otherwise, update the right pointer
            else {
                // Calculate the trapped water and update the total
                totalWater += max(0, rightMax - height[right]);
                right--;
            }
        }
        
        // Return the total trapped water
        return totalWater;
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
- Use two pointers to track the maximum heights on both sides of the array.
- Calculate the trapped water by finding the minimum of the maximum heights on both sides and subtracting the height of the current bar.
- Update the pointers based on the comparison of the maximum heights on both sides.
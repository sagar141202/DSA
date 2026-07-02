# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the corresponding element in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and the right sides. The amount of water that can be trapped is equal to the difference between the minimum of the maximum heights on the left and the right and the height of the bar. For example, given the array [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The approach to solve this problem is to use two pointers, one starting from the left and one from the right, and maintain the maximum height of the bars on the left and the right. The pointer that points to the smaller bar is moved towards the other end, and the amount of water that can be trapped is calculated.

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
            // If the height of the bar on the left is smaller than the height of the bar on the right
            if (height[left] < height[right]) {
                // If the height of the bar on the left is greater than the maxLeft, update maxLeft
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } 
                // Otherwise, add the difference between maxLeft and the height of the bar on the left to the result
                else {
                    result += maxLeft - height[left];
                }
                // Move the left pointer to the right
                left++;
            } 
            // If the height of the bar on the right is smaller than or equal to the height of the bar on the left
            else {
                // If the height of the bar on the right is greater than the maxRight, update maxRight
                if (height[right] > maxRight) {
                    maxRight = height[right];
                } 
                // Otherwise, add the difference between maxRight and the height of the bar on the right to the result
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
- Use two pointers to track the maximum height of the bars on the left and the right.
- Move the pointer that points to the smaller bar towards the other end.
- Calculate the amount of water that can be trapped by finding the difference between the minimum of the maximum heights on the left and the right and the height of the bar.
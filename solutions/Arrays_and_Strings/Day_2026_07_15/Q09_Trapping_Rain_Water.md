# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The bars are represented as lines in a 2D plane, and the water can be trapped between them if there is a bar of greater height on both sides. The function should take an array of integers as input and return the total amount of water that can be trapped. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers, one from the left and one from the right, to track the maximum height of the bars on both sides. The pointer that points to the smaller bar is moved towards the other end, and the difference between the maximum height and the current bar height is added to the total water trapped.

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
        int water = 0;
        
        // Move the pointers towards each other
        while (left <= right) {
            // If the left bar is smaller, move the left pointer
            if (height[left] < height[right]) {
                // If the current bar is greater than the max left, update max left
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } 
                // Otherwise, add the trapped water to the total
                else {
                    water += maxLeft - height[left];
                }
                left++;
            } 
            // If the right bar is smaller, move the right pointer
            else {
                // If the current bar is greater than the max right, update max right
                if (height[right] > maxRight) {
                    maxRight = height[right];
                } 
                // Otherwise, add the trapped water to the total
                else {
                    water += maxRight - height[right];
                }
                right--;
            }
        }
        
        return water;
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
- Move the pointer that points to the smaller bar towards the other end.
- Add the difference between the maximum height and the current bar height to the total water trapped if the current bar is smaller than the maximum height.
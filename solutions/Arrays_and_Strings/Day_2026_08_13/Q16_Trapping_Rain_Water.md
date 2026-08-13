# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the value at each index in the array. Water can be trapped between two bars if there is a bar of greater height on both the left and right sides. The goal is to calculate the total amount of water that can be trapped. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of bars on both sides. The pointer with the smaller maximum height is moved towards the other pointer, and the difference between the maximum height and the current bar height is added to the total trapped water.

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
        
        while (left <= right) {
            if (height[left] < height[right]) {
                if (height[left] >= maxLeft) {
                    maxLeft = height[left];
                } else {
                    result += maxLeft - height[left];
                }
                left++;
            } else {
                if (height[right] >= maxRight) {
                    maxRight = height[right];
                } else {
                    result += maxRight - height[right];
                }
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
- Use two pointers to track the maximum height of bars on both sides.
- Move the pointer with the smaller maximum height towards the other pointer.
- Calculate the difference between the maximum height and the current bar height to determine the trapped water.
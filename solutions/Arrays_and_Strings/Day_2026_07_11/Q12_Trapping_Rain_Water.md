# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at each index in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and right side of the bars. The task is to calculate the total amount of water that can be trapped.

## Approach
The approach to solve this problem is to use two pointers, one starting from the left and one from the right, and move them towards each other. At each step, we choose the pointer with the smaller height and move it towards the other pointer. We keep track of the maximum height of the bars on the left and right side of the current pointer.

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
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to track the maximum height of bars on the left and right side.
- Move the pointer with the smaller height towards the other pointer to minimize the water trapped.
- Keep track of the maximum height of bars on both sides to calculate the water trapped.
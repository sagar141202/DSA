# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the corresponding element in the array. The water can only be trapped between two bars if there is a bar of greater height on both the left and the right. The amount of water that can be trapped is the difference between the height of the shorter of the two greater bars and the height of the bar between them. For example, given the array [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The approach is to use two pointers, one starting from the left and one from the right, to keep track of the maximum height of the bars on both sides. The algorithm iterates through the array, updating the maximum heights and calculating the amount of water that can be trapped.

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
- Use two pointers to keep track of the maximum heights on both sides.
- Update the maximum heights and calculate the amount of water that can be trapped at each step.
- The time complexity is O(n) where n is the number of bars in the histogram.
# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the corresponding element in the array. The water can only be trapped between two bars if there is a bar of greater height on both the left and the right side. The task is to calculate the total amount of water that can be trapped. For example, given the height array [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The approach to solve this problem involves using two pointers, one starting from the left and one from the right, and maintaining the maximum height of the bars on both sides. The water that can be trapped at each position is calculated as the minimum of the maximum heights on the left and right minus the height of the current bar.

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
```

## Key Takeaways
- Use two pointers to track the maximum height of bars on both sides.
- Calculate the water that can be trapped at each position based on the minimum of the maximum heights on the left and right.
- The time complexity is linear, and the space complexity is constant, making this solution efficient for large inputs.
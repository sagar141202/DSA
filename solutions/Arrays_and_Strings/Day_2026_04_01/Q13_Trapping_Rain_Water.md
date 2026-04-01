# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the value at each index in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and the right side of the lower bar. The amount of water that can be trapped is the difference between the minimum of the maximum heights on the left and the right, and the height of the bar.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum heights on both sides. It then calculates the amount of water that can be trapped at each position and adds it to the total.

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
- Use two pointers to track the maximum heights on both sides of the array.
- Calculate the amount of water that can be trapped at each position by finding the minimum of the maximum heights on the left and the right, and subtracting the height of the bar.
- The time complexity is O(n) because we only iterate through the array once.
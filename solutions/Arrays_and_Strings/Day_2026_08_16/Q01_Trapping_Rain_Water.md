# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at the corresponding index in the array. Water can be trapped between two bars if there is a bar of greater height on both the left and the right side of the bar. The amount of water that can be trapped is the difference between the minimum of the maximum height of the bars on the left and the maximum height of the bars on the right, and the height of the bar itself.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. It calculates the amount of water that can be trapped at each bar by finding the minimum of the maximum heights on both sides and subtracting the height of the bar.

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
- Use two pointers to track the maximum height of the bars on both sides.
- Calculate the amount of water that can be trapped at each bar by finding the minimum of the maximum heights on both sides and subtracting the height of the bar.
- The time complexity is O(n) where n is the number of bars, and the space complexity is O(1) as only a constant amount of space is used.
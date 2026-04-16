# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the value at the corresponding index in the array. Two pointers, one starting from the left and one from the right, can be used to track the maximum height of the bars on both sides. The amount of water that can be trapped at each position is the difference between the minimum of the maximum heights on both sides and the height of the bar at that position.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. It maintains the maximum height of the bars on the left and right sides and calculates the amount of water that can be trapped at each position. The time complexity is O(n), where n is the number of bars.

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
- Use two pointers to track the maximum height of the bars on both sides.
- Calculate the amount of water that can be trapped at each position by finding the difference between the minimum of the maximum heights on both sides and the height of the bar at that position.
- The time complexity is O(n), where n is the number of bars, and the space complexity is O(1) as it only uses a constant amount of space.
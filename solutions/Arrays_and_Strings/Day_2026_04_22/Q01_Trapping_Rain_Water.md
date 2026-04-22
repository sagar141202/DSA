# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at each index in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and right sides. The goal is to calculate the total amount of water that can be trapped.

## Approach
The solution uses a two-pointer approach, starting from both ends of the array and moving towards the center. The algorithm keeps track of the maximum height of bars on the left and right sides and calculates the trapped water based on the minimum of these two maximum heights.

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
- Use two pointers to track the maximum height of bars on the left and right sides.
- Calculate the trapped water based on the minimum of the two maximum heights.
- The time complexity is O(n), where n is the number of bars in the histogram.
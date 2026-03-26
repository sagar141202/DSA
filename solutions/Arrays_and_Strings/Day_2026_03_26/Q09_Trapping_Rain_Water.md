# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at the corresponding index in the array. The water can be trapped between two bars if there is a bar of greater height on both the left and right sides of the valley. The problem statement requires finding the total amount of water that can be trapped.

## Approach
The approach involves using two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. The algorithm iterates through the array, updating the maximum heights and calculating the trapped water.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
```

## Test Cases
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to track the maximum heights on both sides.
- Update the maximum heights and calculate the trapped water based on the current bar height.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), where n is the number of bars in the histogram.
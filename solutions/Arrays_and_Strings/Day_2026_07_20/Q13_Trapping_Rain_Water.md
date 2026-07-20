# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at each index in the array. The amount of water that can be trapped is calculated by summing the differences between the minimum of the maximum height of the bars to the left and right of each bar and the height of the bar itself, for all bars where this difference is positive.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars to the left and right of the current bar. The amount of water that can be trapped at each bar is calculated and added to the total.

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
            // If the height of the bar at the left pointer is less than the height of the bar at the right pointer,
            // update the maxLeft and calculate the trapped water at the left pointer.
            if (height[left] < height[right]) {
                if (height[left] >= maxLeft) {
                    maxLeft = height[left];
                } else {
                    result += maxLeft - height[left];
                }
                left++;
            } 
            // Otherwise, update the maxRight and calculate the trapped water at the right pointer.
            else {
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
- Use two pointers to track the maximum height of the bars to the left and right of the current bar.
- Calculate the amount of water that can be trapped at each bar by taking the minimum of the maximum height of the bars to the left and right and subtracting the height of the bar itself.
- The time complexity of the solution is O(n), where n is the number of bars in the histogram, and the space complexity is O(1), as only a constant amount of space is used.
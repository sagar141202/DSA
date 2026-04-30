# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The water can only be trapped if there are bars on both sides that are higher than the bar in between. The input array will have a length of at least 3 and at most 10^5, and the height of each bar will be between 0 and 10^4. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to keep track of the maximum height of the bars on both sides. The pointer that points to the smaller bar is moved towards the other pointer, and the water that can be trapped is calculated based on the difference between the maximum height and the current bar height.

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
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Input: [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to keep track of the maximum height of the bars on both sides.
- Move the pointer that points to the smaller bar towards the other pointer.
- Calculate the water that can be trapped based on the difference between the maximum height and the current bar height.
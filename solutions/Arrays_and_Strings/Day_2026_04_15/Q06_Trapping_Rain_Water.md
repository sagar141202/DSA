# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a graph, calculate the amount of water that can be trapped between the bars. The water can be trapped if there is a bar on the left and right with a greater height than the current bar. The constraint is that the input array will have at least 3 elements and all elements will be non-negative integers. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output will be 6.

## Approach
The algorithm uses two pointers, one from the left and one from the right, to track the maximum height of the bars. The amount of water that can be trapped at each position is calculated by finding the minimum of the maximum heights on the left and right and subtracting the height of the current bar. This approach ensures that we consider all possible combinations of bars that can trap water.

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
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

## Key Takeaways
- Use two pointers to track the maximum height of the bars from the left and right.
- Calculate the amount of water that can be trapped at each position by finding the minimum of the maximum heights on the left and right and subtracting the height of the current bar.
- The time complexity is O(n) where n is the number of bars, and the space complexity is O(1) as we only use a constant amount of space.
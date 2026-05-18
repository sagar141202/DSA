# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The water can only be trapped between two bars if the height of the bars is greater than the height of the bars in between. The input array will have a length of at least 3 and at most 10^5. Each element in the array will be between 0 and 10^4. For example, given the input [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The approach to solve this problem is to use two pointers, one from the left and one from the right, to track the maximum height of the bars on both sides. We then calculate the trapped water by finding the minimum of the maximum heights on both sides and subtracting the height of the current bar.

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
Input: [4,2,0,3,2,5]
Output: 9
```

## Key Takeaways
- Use two pointers to track the maximum height of the bars on both sides.
- Calculate the trapped water by finding the minimum of the maximum heights on both sides and subtracting the height of the current bar.
- The time complexity is O(n) and the space complexity is O(1), where n is the length of the input array.
# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The water can only be trapped if there are bars on both sides of the water with a height greater than the water's height. The input array will have a length of at least 1 and at most 10^5, and each element will be between 0 and 10^5.

## Approach
The algorithm uses two pointers, one at the start and one at the end of the array, to keep track of the maximum height of the bars on the left and right sides. The pointer with the smaller maximum height is moved towards the other pointer, and the trapped water is calculated at each step. This approach ensures that the time complexity is linear, making it efficient for large inputs.

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
        
        // Loop through the array until the two pointers meet
        while (left <= right) {
            // If the height at the left pointer is less than the height at the right pointer
            if (height[left] < height[right]) {
                // If the height at the left pointer is greater than the maxLeft, update maxLeft
                if (height[left] > maxLeft) {
                    maxLeft = height[left];
                } else {
                    // Otherwise, add the trapped water to the result
                    result += maxLeft - height[left];
                }
                // Move the left pointer to the right
                left++;
            } else {
                // If the height at the right pointer is greater than the maxRight, update maxRight
                if (height[right] > maxRight) {
                    maxRight = height[right];
                } else {
                    // Otherwise, add the trapped water to the result
                    result += maxRight - height[right];
                }
                // Move the right pointer to the left
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
- The two-pointer technique can be used to solve problems that involve finding a maximum or minimum value in an array.
- The time complexity of the solution is linear, making it efficient for large inputs.
- The space complexity is constant, as only a few variables are used to store the maximum heights and the result.
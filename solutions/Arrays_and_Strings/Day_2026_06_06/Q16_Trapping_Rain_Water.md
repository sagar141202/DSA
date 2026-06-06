# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the value at the corresponding index in the array. The water can only be trapped between two bars if there is a bar of greater height on both the left and right sides. The task is to calculate the total amount of water that can be trapped.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. The pointer with the smaller maximum height is moved towards the other pointer, and the trapped water is calculated at each step. This approach ensures that we consider all possible pairs of bars that can trap water.

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
        
        // Move the pointers towards each other
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
- The two-pointer technique is useful for solving problems that involve comparing elements from both ends of an array.
- Keeping track of the maximum height on both sides is crucial for calculating the trapped water.
- The time complexity is O(n) because we only need to traverse the array once.
# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is given by the corresponding element in the array. For example, if the input array is [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6, which is the total amount of water that can be trapped between the bars.

## Approach
The algorithm uses two pointers, one at the beginning and one at the end of the array, to keep track of the maximum height of the bars on the left and right sides. The pointer with the smaller maximum height is moved towards the other pointer, and the trapped water is calculated based on the difference between the maximum height and the current bar height.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int trap(vector<int>& height) {
    // Initialize two pointers, one at the beginning and one at the end
    int left = 0, right = height.size() - 1;
    // Initialize the maximum height of the bars on the left and right sides
    int maxLeft = 0, maxRight = 0;
    // Initialize the total amount of trapped water
    int water = 0;
    
    // Loop through the array until the two pointers meet
    while (left <= right) {
        // If the maximum height on the left is less than the maximum height on the right
        if (maxLeft < maxRight) {
            // If the current bar height is greater than the maximum height on the left
            if (height[left] > maxLeft) {
                // Update the maximum height on the left
                maxLeft = height[left];
            } else {
                // Calculate the trapped water and update the total amount
                water += maxLeft - height[left];
            }
            // Move the left pointer to the right
            left++;
        } else {
            // If the current bar height is greater than the maximum height on the right
            if (height[right] > maxRight) {
                // Update the maximum height on the right
                maxRight = height[right];
            } else {
                // Calculate the trapped water and update the total amount
                water += maxRight - height[right];
            }
            // Move the right pointer to the left
            right--;
        }
    }
    // Return the total amount of trapped water
    return water;
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
- The algorithm uses two pointers to keep track of the maximum height of the bars on the left and right sides.
- The pointer with the smaller maximum height is moved towards the other pointer to calculate the trapped water.
- The time complexity is O(n) and the space complexity is O(1), making it efficient for large inputs.
# Trapping Rain Water

## Problem Statement
Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars. The height of each bar is represented by the value at each index in the array. The water can be trapped between two bars if the height of the bars is greater than the height of the bars in between them. The goal is to calculate the total amount of water that can be trapped. For example, given the array [0,1,0,2,1,0,1,3,2,1,2,1], the output should be 6.

## Approach
The algorithm uses two pointers, one starting from the left and one from the right, to track the maximum height of the bars on both sides. The pointer with the smaller height is moved towards the other pointer, and the difference between the height of the bar at the current position and the maximum height is added to the total water trapped.

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
    int water = 0;
    
    // loop through the array until the two pointers meet
    while (left <= right) {
        // if the height at the left pointer is less than the height at the right pointer
        if (height[left] < height[right]) {
            // if the height at the left pointer is greater than the maxLeft, update maxLeft
            if (height[left] > maxLeft) {
                maxLeft = height[left];
            } 
            // else, add the difference between maxLeft and the height at the left pointer to the water
            else {
                water += maxLeft - height[left];
            }
            // move the left pointer to the right
            left++;
        } 
        // else, the height at the left pointer is greater than or equal to the height at the right pointer
        else {
            // if the height at the right pointer is greater than the maxRight, update maxRight
            if (height[right] > maxRight) {
                maxRight = height[right];
            } 
            // else, add the difference between maxRight and the height at the right pointer to the water
            else {
                water += maxRight - height[right];
            }
            // move the right pointer to the left
            right--;
        }
    }
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
- The two-pointer technique can be used to solve problems that involve finding the maximum or minimum value in an array.
- The key to solving this problem is to keep track of the maximum height on both sides of the current position.
- The time complexity of the solution is O(n), where n is the number of elements in the array, because we only need to traverse the array once.
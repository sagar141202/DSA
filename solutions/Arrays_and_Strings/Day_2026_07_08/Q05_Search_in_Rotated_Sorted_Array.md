# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, some elements may be shifted to the end. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotation of the sorted array `[0, 1, 2, 4, 5, 6, 7]`. The function should return the index of the target element if it exists in the array; otherwise, it returns -1. The function takes two parameters: a vector of integers representing the rotated sorted array and an integer representing the target element.

## Approach
The algorithm uses a modified binary search approach to find the target element in the rotated sorted array. It first checks if the middle element is the target, then determines which half of the array is sorted and if the target could be in that half. The search space is reduced by half at each step, resulting in a logarithmic time complexity.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // Initialize two pointers, one at the start and one at the end of the array
        int left = 0, right = nums.size() - 1;
        
        // Continue the search until the two pointers meet
        while (left <= right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;
            
            // If the target is found at the middle index, return the index
            if (nums[mid] == target) {
                return mid;
            }
            
            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If the target is in the left half, update the right pointer
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } 
                // Otherwise, update the left pointer
                else {
                    left = mid + 1;
                }
            } 
            // If the right half is sorted
            else {
                // If the target is in the right half, update the left pointer
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } 
                // Otherwise, update the right pointer
                else {
                    right = mid - 1;
                }
            }
        }
        
        // If the target is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

## Key Takeaways
- The algorithm uses a modified binary search approach to find the target element in the rotated sorted array.
- The search space is reduced by half at each step, resulting in a logarithmic time complexity.
- The algorithm handles cases where the target element is not present in the array by returning -1.
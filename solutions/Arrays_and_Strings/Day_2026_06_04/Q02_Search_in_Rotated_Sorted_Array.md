# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, some elements may be shifted to the end of the array. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array where the target element could be any number. The function should return the index of the target element if found, otherwise return -1. The array does not contain duplicate elements. Constraints: 1 <= nums.length <= 5000, -10^4 <= nums[i] <= 10^4, -10^4 <= target <= 10^4.

## Approach
The algorithm uses a modified binary search approach to find the target element in the rotated sorted array. It checks which half of the array is sorted and then decides which half to continue searching in. This approach takes advantage of the fact that the array is sorted in ascending order before rotation. The search space is reduced by half at each step, resulting in an efficient solution.

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
        
        // Continue searching while the two pointers have not crossed each other
        while (left <= right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;
            
            // If the target element is found at the middle index, return the index
            if (nums[mid] == target) {
                return mid;
            }
            
            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If the target element is in the left half, update the right pointer
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
                // If the target element is in the right half, update the left pointer
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } 
                // Otherwise, update the right pointer
                else {
                    right = mid - 1;
                }
            }
        }
        
        // If the target element is not found, return -1
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
- The key to solving this problem is to identify which half of the array is sorted at each step.
- The search space is reduced by half at each step, resulting in a time complexity of O(log n).
- The solution does not use any extra space, resulting in a space complexity of O(1).
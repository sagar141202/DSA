# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find the index of a target element. The array was initially sorted in ascending order, but it was rotated at some point, and we don't know how many times it was rotated. For example, if we have the array [1, 2, 3, 4, 5] and it was rotated twice, the resulting array would be [3, 4, 5, 1, 2]. We need to write a function that takes this rotated array and a target element as input and returns the index of the target element if it exists in the array, or -1 if it doesn't exist. The function should run in O(log n) time, where n is the number of elements in the array.

## Approach
We can use a modified binary search algorithm to solve this problem, taking into account the fact that the array is rotated. We will divide the array into two halves and determine which half is sorted, then decide which half to continue searching in based on the target element's value.

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
        
        // Continue searching while the two pointers haven't crossed each other
        while (left <= right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;
            
            // If the target element is found at the middle index, return the middle index
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
- The key to solving this problem is to determine which half of the array is sorted and then decide which half to continue searching in based on the target element's value.
- We use a modified binary search algorithm to achieve a time complexity of O(log n).
- The space complexity is O(1) because we only use a constant amount of space to store the pointers and the target element.
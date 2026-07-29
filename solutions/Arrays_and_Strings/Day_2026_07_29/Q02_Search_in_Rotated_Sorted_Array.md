# Search in Rotated Sorted Array

## Problem Statement
Search for a target element in a sorted array that has been rotated an unknown number of times. The array was initially sorted in ascending order, but after rotation, some elements may be shifted to the end. The goal is to find the index of the target element if it exists in the array. Constraints: the array contains distinct integers, and the target element may or may not be present. Example: given the array [4, 5, 6, 7, 0, 1, 2] and the target 0, the output should be 4, which is the index of the target element.

## Approach
The algorithm uses a modified binary search to find the target element in the rotated array. It checks which half of the array is sorted and then decides which half to continue searching in. The search space is reduced by half at each step, making the algorithm efficient.

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
        // initialize two pointers, one at the start and one at the end of the array
        int left = 0, right = nums.size() - 1;
        
        // continue the search until the two pointers meet
        while (left <= right) {
            // calculate the middle index
            int mid = left + (right - left) / 2;
            
            // if the target is found at the middle index, return the index
            if (nums[mid] == target) {
                return mid;
            }
            
            // if the left half is sorted
            if (nums[left] <= nums[mid]) {
                // if the target is in the left half, update the right pointer
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } 
                // otherwise, update the left pointer
                else {
                    left = mid + 1;
                }
            } 
            // if the right half is sorted
            else {
                // if the target is in the right half, update the left pointer
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } 
                // otherwise, update the right pointer
                else {
                    right = mid - 1;
                }
            }
        }
        
        // if the target is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Input: nums = [1], target = 0
Output: -1
```

## Key Takeaways
- The algorithm uses a modified binary search approach to find the target element in the rotated array.
- The search space is reduced by half at each step, resulting in a time complexity of O(log n).
- The algorithm handles cases where the target element may or may not be present in the array.
# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, some elements may now be out of order. The rotation is done in a way that each element is shifted to the right by a certain number of positions. For example, if the original array is [1, 2, 3, 4, 5, 6, 7] and it is rotated by 3 positions, the resulting array would be [5, 6, 7, 1, 2, 3, 4]. The goal is to find the index of the target element in the rotated array. If the target element is not present in the array, return -1.

## Approach
The solution uses a modified binary search algorithm to find the target element in the rotated array. The algorithm checks which half of the array is sorted and then decides which half to continue searching in. This approach takes advantage of the fact that even though the array is rotated, one half of it will always be sorted.

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
        int left = 0;
        int right = nums.size() - 1;
        
        // Continue searching while the two pointers haven't crossed each other
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
- The problem can be solved using a modified binary search algorithm.
- The algorithm takes advantage of the fact that one half of the rotated array will always be sorted.
- The time complexity of the solution is O(log n), making it efficient for large inputs.
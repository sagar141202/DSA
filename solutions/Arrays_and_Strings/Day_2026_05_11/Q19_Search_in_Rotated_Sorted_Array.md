# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array was originally sorted in ascending order. You can assume there are no duplicate elements in the array. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` which was originally `[0, 1, 2, 4, 5, 6, 7]`, and the target `0`, the function should return `4` which is the index of `0` in the rotated array. If the target is not found, return `-1`.

## Approach
We can solve this problem by using a modified binary search algorithm that takes into account the rotation of the array. The key intuition is to determine which half of the array is sorted and then decide which half to continue searching in.

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
        // Initialize the low and high pointers for binary search
        int low = 0, high = nums.size() - 1;
        
        // Continue the search until the low and high pointers meet
        while (low <= high) {
            // Calculate the mid index
            int mid = low + (high - low) / 2;
            
            // If the target is found at the mid index, return the mid index
            if (nums[mid] == target) {
                return mid;
            }
            
            // If the left half is sorted
            if (nums[low] <= nums[mid]) {
                // If the target is in the range of the left half, update the high pointer
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } 
                // Otherwise, update the low pointer
                else {
                    low = mid + 1;
                }
            } 
            // If the right half is sorted
            else {
                // If the target is in the range of the right half, update the low pointer
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } 
                // Otherwise, update the high pointer
                else {
                    high = mid - 1;
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
- The key to solving this problem is to identify which half of the array is sorted and then decide which half to continue searching in.
- We use a modified binary search algorithm to achieve a time complexity of O(log n).
- The problem can be solved with a space complexity of O(1) as we only use a constant amount of space to store the low, high, and mid indices.
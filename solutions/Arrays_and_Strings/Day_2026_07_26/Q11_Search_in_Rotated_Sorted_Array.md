# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array. You can assume that there are no duplicates in the array. The array may contain duplicate values but the target will always be unique. For example, given the rotated array `[4, 5, 6, 7, 0, 1, 2]` and the target `0`, return `4` which is the index of `0` in the array. The array may be very large, so an efficient solution is required.

## Approach
The algorithm uses a modified binary search to find the target in the rotated array. It first checks if the middle element is the target, then decides which half of the array to continue searching in based on whether the left or right half is sorted. The search space is reduced by half at each step, leading to an efficient solution.

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
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            
            // Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If the target is in the sorted left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // If the left half is not sorted, the right half must be sorted
            else {
                // If the target is in the sorted right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;  // Return -1 if the target is not found
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
- The key to solving this problem is to determine which half of the array is sorted at each step.
- By comparing the middle element with the leftmost element, we can decide which half to search in.
- The search space is reduced by half at each step, resulting in a time complexity of O(log n).
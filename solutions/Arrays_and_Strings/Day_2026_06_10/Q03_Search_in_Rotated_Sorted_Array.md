# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array. The array is sorted in ascending order but rotated at some pivot. For example, the array `[4, 5, 6, 7, 0, 1, 2]` represents the sorted array `[0, 1, 2, 4, 5, 6, 7]` rotated at index 3. You are given the rotated array `nums` and a target value `target`, return the index of `target` if it is in `nums`, otherwise return `-1`. The array may contain duplicate values.

## Approach
The algorithm uses a modified binary search to find the target in the rotated array. It checks which half of the array is sorted and decides which half to continue searching in. The search space is reduced by half at each step, resulting in a logarithmic time complexity.

## Complexity
- Time: O(log n) for the best case when there are no duplicates, O(n) for the worst case when all elements are the same
- Space: O(1) as it only uses a constant amount of space

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        
        int left = 0, right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) return mid;
            
            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // If the right half is sorted
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
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
- The algorithm handles the case where the array is rotated at some unknown pivot.
- It uses a binary search approach to find the target in the rotated array.
- The search space is reduced by half at each step, resulting in a logarithmic time complexity in the best case.
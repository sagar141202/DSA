# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value. The array was originally sorted in ascending order. The problem can be solved using a modified binary search algorithm. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and target `0`, the output should be `4` (the index of `0` in the array). The array can contain duplicate values and may be rotated any number of times.

## Approach
The approach is to use a modified binary search algorithm that checks the middle element and determines which half of the array is sorted. The algorithm then decides which half to continue searching in based on the target value. This process continues until the target value is found or the search space is empty.

## Complexity
- Time: O(log n) for the best-case scenario when there are no duplicates, but it can be O(n) in the worst-case scenario when all elements are the same.
- Space: O(1) as only a constant amount of space is used.

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
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // If left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // If right half is sorted
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

Input: nums = [1], target = 0
Output: -1

Input: nums = [2, 2, 2, 3, 4, 2], target = 3
Output: 3
```

## Key Takeaways
- The algorithm's efficiency relies on the array being sorted and rotated, allowing for a binary search approach.
- Handling duplicate values in the array can affect the algorithm's performance, potentially leading to a linear search in the worst case.
- The choice of the middle element's calculation (`mid = left + (right - left) / 2`) helps avoid potential integer overflow issues.
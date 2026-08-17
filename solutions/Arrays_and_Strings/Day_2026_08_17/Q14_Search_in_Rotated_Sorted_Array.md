# Search in Rotated Sorted Array

## Problem Statement
Suppose an array of distinct integers is sorted in ascending order and rotated at some pivot unknown to you beforehand. Given the rotated array and an integer, find the index of the target integer in the array if it exists. If it does not exist, return -1. The array may contain duplicate elements. For example, given the array [4, 5, 6, 7, 0, 1, 2] and the target 0, the function should return 4, which is the index of 0 in the array.

## Approach
The approach is to use a modified binary search algorithm that takes into account the rotation of the array. We will find the middle element and compare it with the target, then decide which half of the array to continue searching in based on whether the left or right half is sorted and whether the target could be in that half.

## Complexity
- Time: O(n) in the worst case, but O(log n) on average
- Space: O(1)

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

Input: nums = [1], target = 0
Output: -1
```

## Key Takeaways
- The key to solving this problem is to determine which half of the array is sorted and then decide which half to continue searching in based on the target value.
- The time complexity is O(n) in the worst case when the array is rotated by one position and the target is at the end, but it is O(log n) on average.
- The space complexity is O(1) because we only use a constant amount of space to store the indices and the target value.
# Search in Rotated Sorted Array

## Problem Statement
Suppose an array of distinct integers is sorted in ascending order and rotated an unknown number of times. Given the array and a target value, return the index of the target if it is present in the array, otherwise return -1. For example, if the input array is [4,5,6,7,0,1,2] and the target is 0, the function should return 4. The array may contain duplicate elements.

## Approach
The solution uses a modified binary search algorithm to find the target element in the rotated array. It first checks if the middle element is the target, then determines which half of the array is sorted and if the target could be in that half. The search space is reduced by half at each step, resulting in a logarithmic time complexity.

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
        if (nums.empty()) return -1;
        
        int left = 0, right = nums.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) return mid;
            
            // if the left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // if the right half is sorted
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
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [1], target = 0
Output: -1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The search space is reduced by half at each step, resulting in a logarithmic time complexity.
- The solution handles cases where the input array is empty or contains duplicate elements.
# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array may contain duplicate values. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and target `0`, return `4` which is the index of `0`. If the target is not found, return `-1`. The array is rotated in the range `[0, n-1]`, where `n` is the length of the array.

## Approach
We can use a modified binary search algorithm to solve this problem, taking into account the rotation of the sorted array. The idea is to determine which half of the array is sorted and decide which half to continue searching in based on the target value.

## Complexity
- Time: O(n)
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
```

## Key Takeaways
- Binary search can be adapted for rotated sorted arrays by considering the sorted halves.
- Handling duplicates in the array is crucial as they can affect the search result.
- The problem can be solved in linear time complexity in the worst case, but with a more efficient approach using binary search, the average time complexity can be improved.
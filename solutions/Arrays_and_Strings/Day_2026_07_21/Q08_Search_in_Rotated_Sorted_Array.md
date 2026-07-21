# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, search for a target value. The array was originally sorted in ascending order. You do not know where rotation began. For example, given the sorted array `[0,1,2,4,5,6,7]`, it will become `[4,5,6,7,0,1,2]` after rotating it to the right by 3 steps. You are given an array of integers `nums` and an integer `target`. If `target` is in `nums`, return its index. Otherwise, return `-1`. You must write an algorithm with a time complexity of O(log n), where n is the number of elements in `nums`.

## Approach
We will use a modified binary search algorithm, taking into account the rotation of the array. The idea is to determine which half of the array is sorted and then decide which half to continue searching in. We will keep doing this until we find the target or the search space becomes empty.

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
            if (nums[mid] == target) {
                return mid;
            }
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
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Key Takeaways
- The key to solving this problem is to identify which half of the array is sorted.
- We use a modified binary search algorithm to achieve a time complexity of O(log n).
- The search space is reduced by half at each step, similar to traditional binary search.
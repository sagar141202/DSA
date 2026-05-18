# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array. The array was originally sorted in ascending order. You can assume there are no duplicate elements in the array. For example, if the original sorted array is `[1, 2, 3, 4, 5, 6, 7]`, it may become `[4, 5, 6, 7, 1, 2, 3]` after rotation. You need to find the index of a target value, e.g., `5` in the rotated array. If the target is not found, return `-1`. The input array is guaranteed to be non-empty and there will be at most one rotation.

## Approach
We can use a modified binary search algorithm to solve this problem. The idea is to find the pivot point where the rotation occurred and then decide which half of the array to search in. We will compare the middle element with the first and last elements to determine which half is sorted and if the target can be in that half.

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
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Input: nums = [1], target = 0
Output: -1
```

## Key Takeaways
- The key to solving this problem is to identify which half of the array is sorted and then decide which half to continue searching in.
- We use a modified binary search algorithm to achieve a time complexity of O(log n).
- The space complexity is O(1) as we are not using any extra space that scales with input size.
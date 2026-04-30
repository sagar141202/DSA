# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, some part of the array is now at the end. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotation of the sorted array `[0, 1, 2, 4, 5, 6, 7]`. The task is to find the index of the target element in the rotated array. If the target is not found, return -1. The array does not contain duplicates. Constraints: 1 <= nums.length <= 5000, -10^4 <= nums[i] <= 10^4, -10^4 <= target <= 10^4.

## Approach
The algorithm uses a modified binary search approach to find the target in the rotated array. It checks which half of the array is sorted and decides which half to continue searching in based on the target's value. This approach takes advantage of the fact that even though the array is rotated, one half of it will always be sorted.

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
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

## Key Takeaways
- The key to solving this problem is recognizing that even in a rotated sorted array, one half of the array will always be sorted.
- Using a modified binary search that takes into account the rotation of the array can efficiently find the target element.
- The solution has a time complexity of O(log n), making it efficient for large inputs.
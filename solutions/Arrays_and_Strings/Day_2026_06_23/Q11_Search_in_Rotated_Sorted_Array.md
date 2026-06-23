# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array was originally sorted in ascending order. You can assume there are no duplicate elements in the array. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and target `0`, the output should be `4` which is the index of `0` in the array. If the target is not found, return `-1`.

## Approach
The algorithm uses a modified binary search approach to find the target element in the rotated sorted array. It first determines which half of the array is sorted, then decides which half to continue searching in based on the target value.

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
- The problem can be solved using a modified binary search algorithm that takes into account the rotation of the sorted array.
- It's essential to handle the cases where the left or right half of the array is sorted to correctly determine the next search space.
- The time complexity of the solution is O(log n), making it efficient for large inputs.
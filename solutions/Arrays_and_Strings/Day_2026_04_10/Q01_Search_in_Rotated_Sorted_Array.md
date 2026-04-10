# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array. The array was originally sorted in ascending order. You can assume there are no duplicates in the array. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and target `0`, the output should be `4` because `0` is at index `4` in the array. If the target is not found, return `-1`. The array size is between `1` and `5000`, and all elements are between `1` and `10^4`.

## Approach
We can use a modified binary search algorithm to solve this problem. The idea is to find the pivot point where the array is rotated and then decide which half of the array to search in. We can do this by comparing the middle element with the start and end elements of the array.

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
            // if left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // if right half is sorted
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
- The key to solving this problem is to identify which half of the array is sorted.
- We use a modified binary search algorithm to achieve a time complexity of O(log n).
- The space complexity is O(1) because we only use a constant amount of space to store the indices and the target value.
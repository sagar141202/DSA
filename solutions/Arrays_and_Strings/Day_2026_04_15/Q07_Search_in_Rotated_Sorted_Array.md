# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, some elements may now be in a different position. The array does not contain duplicate elements. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and a target of `0`, the function should return `4`, which is the index of `0` in the array.

## Approach
The approach is to use a modified binary search algorithm that takes into account the rotation of the array. We will divide the array into two halves and determine which half is sorted. We will then decide which half to continue searching in based on the target element's value.

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
- The key to solving this problem is to determine which half of the array is sorted and then decide which half to continue searching in.
- We use a modified binary search algorithm that takes into account the rotation of the array.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.
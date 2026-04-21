# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to rotation, the order is now changed. For example, if the initial array was [1, 2, 3, 4, 5, 6, 7], after rotation it could become [4, 5, 6, 7, 1, 2, 3]. The task is to find the index of the target element in the rotated array. The array does not contain duplicate elements. The function should return the index of the target element if found, otherwise return -1.

## Approach
The algorithm uses a modified binary search approach to find the target element in the rotated sorted array. It first determines which half of the array is sorted and then decides which half to continue searching in based on the target element's value. This process continues until the target element is found or the search space is exhausted.

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
            // Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // If the left half is not sorted, the right half must be sorted
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
- Binary search can be adapted for rotated sorted arrays by checking which half is sorted and deciding the search direction based on the target element's value.
- The time complexity of this solution is O(log n) due to the use of binary search.
- The space complexity is O(1) as it only uses a constant amount of space to store the indices and the target element.
# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but after rotation, some elements may be shifted to the end of the array. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated version of the array [0, 1, 2, 4, 5, 6, 7]. The target element can be any integer, and the function should return its index if found, or -1 if not found. The array does not contain duplicates.

## Approach
The algorithm uses a modified binary search approach to find the target element in the rotated array. It first determines which half of the array is sorted, then decides which half to continue searching in based on the target element's value. This process is repeated until the target element is found or the search space is empty.

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
- The algorithm uses a modified binary search approach to find the target element in the rotated array.
- The time complexity is O(log n) due to the use of binary search, making it efficient for large arrays.
- The space complexity is O(1) since only a constant amount of space is used to store the indices and the target element.
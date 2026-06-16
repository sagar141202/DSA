# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find the index of a target element in the array. The array was originally sorted in ascending order, but due to the rotation, some elements may now be in a different order. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotation of the sorted array `[0, 1, 2, 4, 5, 6, 7]`. The function should take as input the rotated array and the target element, and return the index of the target element if it exists in the array, or -1 if it does not exist. The function should run in O(log n) time, where n is the number of elements in the array.

## Approach
The problem can be solved using a modified binary search algorithm. The algorithm checks if the left or right half of the array is sorted, and then decides which half to continue searching in. This approach allows the function to run in O(log n) time.

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
        // Initialize the left and right pointers for the binary search
        int left = 0;
        int right = nums.size() - 1;

        // Continue the binary search until the left and right pointers meet
        while (left <= right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;

            // If the target is found at the middle index, return the middle index
            if (nums[mid] == target) {
                return mid;
            }

            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If the target is in the left half, update the right pointer
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    // Otherwise, update the left pointer
                    left = mid + 1;
                }
            } else {
                // If the right half is sorted
                // If the target is in the right half, update the left pointer
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    // Otherwise, update the right pointer
                    right = mid - 1;
                }
            }
        }

        // If the target is not found, return -1
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
- The problem can be solved using a modified binary search algorithm.
- The algorithm checks if the left or right half of the array is sorted, and then decides which half to continue searching in.
- The function runs in O(log n) time, where n is the number of elements in the array.
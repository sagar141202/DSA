# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array was originally sorted in ascending order, but it was rotated an unknown number of times. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` which was originally `[0, 1, 2, 4, 5, 6, 7]`, and a target `0`, the function should return `4` which is the index of `0` in the rotated array. If the target is not found, return `-1`. The constraints are: `1 <= nums.length <= 5000`, `-10^4 <= nums[i] <= 10^4`, `nums` is guaranteed to be a rotated sorted array, and all elements in `nums` are unique.

## Approach
The algorithm uses a modified binary search to find the target in the rotated sorted array. It checks which half of the array is sorted and decides which half to continue searching in. The intuition is to always search in the half that is guaranteed to have the target if it exists.

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
            if (nums[mid] == target) return mid;
            
            // Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If target is in the sorted left half, search in left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // If the left half is not sorted, the right half must be sorted
            else {
                // If target is in the sorted right half, search in right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1; // Target not found
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
- The key to solving this problem is recognizing that at least one half of the rotated array will always be sorted.
- By determining which half is sorted, we can decide which half to continue searching in for the target value.
- This approach allows us to apply a modified binary search algorithm to find the target efficiently.
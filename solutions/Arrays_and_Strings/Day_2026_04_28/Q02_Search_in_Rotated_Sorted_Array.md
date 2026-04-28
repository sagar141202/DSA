# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array may contain duplicate values. The time complexity should be better than O(n), where n is the number of elements in the array. For example, given the array `[4, 5, 6, 7, 0, 1, 2]` and target `0`, the function should return `4`, which is the index of `0` in the array.

## Approach
The algorithm uses a modified binary search to find the target element. It checks which half of the array is sorted and then decides which half to continue searching in. The algorithm handles duplicate values by moving the pointers accordingly.

## Complexity
- Time: O(n) in the worst case when all elements are the same, O(log n) on average
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1;
        
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            
            // Check which half is sorted
            if (nums[left] <= nums[mid]) {
                // Left half is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
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
- The algorithm uses a modified binary search approach to solve the problem efficiently.
- It handles duplicate values by adjusting the pointers based on the sorted half of the array.
- The time complexity is O(n) in the worst case and O(log n) on average, making it efficient for large inputs.
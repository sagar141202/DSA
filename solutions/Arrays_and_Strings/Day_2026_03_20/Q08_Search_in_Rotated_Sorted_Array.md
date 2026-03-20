# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find the index of a target element. The array was initially sorted in ascending order, but after rotation, some elements may be out of order. For example, if the initial array was `[1, 2, 3, 4, 5]`, a rotated version could be `[3, 4, 5, 1, 2]`. The target element is an integer that may or may not be present in the array. If the target is found, return its index; otherwise, return -1. The array does not contain duplicates.

## Approach
The algorithm uses a modified binary search to find the target in the rotated array, checking which half of the array is sorted and determining if the target could be in that half. This process continues until the target is found or the search space is exhausted.

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
        if (nums.empty()) return -1;
        
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            
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
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Key Takeaways
- The key to solving this problem is recognizing which half of the array is sorted and using that information to guide the binary search.
- The algorithm's efficiency comes from reducing the search space by half at each step, similar to standard binary search.
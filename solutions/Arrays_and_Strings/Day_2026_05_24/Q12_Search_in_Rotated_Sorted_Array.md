# Search in Rotated Sorted Array

## Problem Statement
Suppose an array of distinct integers is sorted in ascending order and then rotated at an unknown pivot index. Given the rotated array and an integer target, return the index of the target if it is present in the array; otherwise, return -1. The array may contain duplicate elements. The problem can be solved using a modified binary search algorithm. For example, given the input array [4, 5, 6, 7, 0, 1, 2] and the target 0, the function should return 4.

## Approach
The algorithm works by first checking if the middle element is the target. If not, it checks which half of the array is sorted and then decides which half to continue searching in based on the target value. This process continues until the target is found or the search space is empty.

## Complexity
- Time: O(log n) for the best case when there are no duplicates, O(n) for the worst case when all elements are the same
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
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Input: nums = [1], target = 0
Output: -1
```

## Key Takeaways
- The key is to identify which half of the array is sorted at each step.
- The presence of duplicates in the array can lead to a worst-case time complexity of O(n).
- The algorithm uses a modified binary search approach to achieve efficient search in the rotated sorted array.
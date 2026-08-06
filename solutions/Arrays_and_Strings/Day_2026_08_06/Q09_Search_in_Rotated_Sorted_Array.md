# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array may contain duplicate values. The problem constraints are: 1 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4, and -10^4 <= target <= 10^4. For example, given the array [4, 5, 6, 7, 0, 1, 2] and target 0, the function should return 4, which is the index of 0 in the array.

## Approach
The algorithm uses a modified binary search approach to find the target in the rotated sorted array. It checks which half of the array is sorted and decides which half to continue searching in. The search space is reduced by half at each step, resulting in a logarithmic time complexity.

## Complexity
- Time: O(n) in the worst case due to duplicates, O(log n) on average
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
- The key to solving this problem is to identify which half of the array is sorted.
- We must consider the case where the array contains duplicate values, which can affect the search process.
- The time complexity can degrade to O(n) in the worst case due to duplicates, but it remains O(log n) on average.
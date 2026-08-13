# Search in Rotated Sorted Array

## Problem Statement
Suppose a sorted array is rotated at some pivot unknown to you beforehand. Given the rotated sorted array, find a target value in the array if it exists. The array was originally sorted in ascending order, but its rotation was done at an unknown pivot index. For example, the array [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2] after rotation. You must write a function that takes the rotated array and target as input, and returns the index of the target if it exists, otherwise returns -1.

## Approach
We can solve this problem by using a modified binary search algorithm, as the array is still partially sorted. The key idea is to determine which half of the array is sorted and then decide which half to continue searching in. This approach allows us to maintain an efficient time complexity.

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
- The array is rotated, but parts of it remain sorted, allowing for a modified binary search approach.
- Determine which half of the array is sorted to decide where to continue the search.
- The solution has a logarithmic time complexity due to the use of binary search.
# Search in Rotated Sorted Array

## Problem Statement
Suppose an array of distinct integers is sorted in ascending order and rotated (i.e., cyclically shifted) an unknown number of times. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotation of the sorted array `[0, 1, 2, 4, 5, 6, 7]`. Given such an array and a target value, find the index of the target in the array if it exists, or return -1 if it does not exist. The array may contain duplicate elements. The input array is guaranteed to have at least one element.

## Approach
We can use a modified binary search algorithm to solve this problem. The key insight is to determine which half of the array is sorted and then decide which half to continue searching in. This approach takes advantage of the fact that the array is sorted in ascending order before rotation.

## Complexity
- Time: O(n) in the worst case (when the array is rotated n times), O(log n) on average
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
- The key to this problem is recognizing that the array is sorted in ascending order before rotation, and using this fact to guide the search.
- We need to handle the case where the array contains duplicate elements, which can affect the correctness of the solution.
- The time complexity can be O(n) in the worst case, but it is typically much faster than this for large inputs.
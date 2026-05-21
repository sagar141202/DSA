# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a target element in the array. The array was originally sorted in ascending order, but after rotation, some elements may be shifted to the end of the array. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotation of the sorted array `[0, 1, 2, 4, 5, 6, 7]`. The target element is an integer that may or may not be present in the array. The function should return the index of the target element if it is present, and -1 otherwise. The input array will contain unique elements.

## Approach
We can solve this problem using a modified binary search algorithm. The key idea is to determine which half of the array is sorted and then decide which half to continue searching in. This approach takes advantage of the fact that the array was originally sorted.

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
- The problem can be solved using a modified binary search algorithm.
- The key idea is to determine which half of the array is sorted and then decide which half to continue searching in.
- The time complexity of the solution is O(log n), which makes it efficient for large inputs.
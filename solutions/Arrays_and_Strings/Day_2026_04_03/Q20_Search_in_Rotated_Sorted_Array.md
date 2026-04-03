# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a target element in the array. The array was initially sorted in ascending order, but after rotation, some elements may be at the beginning of the array that were previously at the end. The rotation is done in a circular manner, i.e., the last element becomes the first element after rotation. For example, if the original array is `[1, 2, 3, 4, 5, 6, 7]`, after rotating it by 3 positions, the array becomes `[5, 6, 7, 1, 2, 3, 4]`. The task is to find the index of a given target element in the rotated array. If the target element is not present in the array, return -1.

## Approach
The solution uses a modified binary search algorithm to find the target element in the rotated array. The algorithm checks which half of the array is sorted and decides which half to continue searching in based on the target element's value. This approach takes advantage of the fact that even after rotation, one half of the array remains sorted.

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
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Key Takeaways
- The key to solving this problem efficiently is recognizing that even after rotation, at least one half of the array remains sorted.
- Using a modified binary search allows us to take advantage of the sorted half to narrow down the search space efficiently.
- The algorithm's time complexity is significantly improved by using binary search, reducing it from a linear search (O(n)) to O(log n).
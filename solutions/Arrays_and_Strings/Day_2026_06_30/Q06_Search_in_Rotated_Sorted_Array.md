# Search in Rotated Sorted Array

## Problem Statement
Given a sorted array that has been rotated an unknown number of times, find a specific target element in the array. The array was initially sorted in ascending order, but due to the rotation, some elements may now be out of order. The rotation is done in a circular manner, meaning the last element of the original array becomes the first element of the rotated array. For example, if the original array is `[1, 2, 3, 4, 5, 6, 7]`, a rotated version could be `[4, 5, 6, 7, 1, 2, 3]`. The task is to find the index of a target element within this rotated array, or return -1 if the target is not present.

## Approach
We can solve this problem using a modified binary search algorithm that accounts for the rotation. The key insight is to determine which half of the current search range is sorted and then decide which half to continue searching in based on the target's value relative to the middle element and the bounds of the sorted half.

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
            
            // If target is found at mid, return mid
            if (nums[mid] == target) return mid;
            
            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If target is within the sorted left half, continue search in left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    // Otherwise, search in the right half
                    left = mid + 1;
                }
            } 
            // If the right half is sorted
            else {
                // If target is within the sorted right half, continue search in right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    // Otherwise, search in the left half
                    right = mid - 1;
                }
            }
        }
        
        // If target is not found, return -1
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
- The problem can be efficiently solved using a modified binary search approach that considers the rotation of the array.
- Determining which half of the search range is sorted at each step is crucial for deciding where to continue the search.
- The solution has a logarithmic time complexity due to the use of binary search, making it efficient for large inputs.
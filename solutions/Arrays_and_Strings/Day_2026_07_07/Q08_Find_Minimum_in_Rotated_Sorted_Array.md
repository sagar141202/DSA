# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a sorted array that has been rotated an unknown number of times. The array is sorted in ascending order, but it has been rotated (clockwise) by some number of positions. For example, if the original array is `[1, 2, 3, 4, 5]`, it could be rotated to `[3, 4, 5, 1, 2]` or `[5, 1, 2, 3, 4]`. The constraint is that there are no duplicates in the array. The goal is to write an efficient algorithm that finds the minimum element in the rotated array.

## Approach
The approach to solving this problem involves using a modified binary search algorithm. The idea is to find the pivot point where the rotation occurs, and then determine which half of the array the minimum element is in. This can be done by comparing the middle element with the rightmost element.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // if the middle element is greater than the rightmost element, 
            // the minimum element must be in the right half
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            // if the middle element is less than or equal to the rightmost element, 
            // the minimum element must be in the left half
            else {
                right = mid;
            }
        }
        return nums[left];
    }
};
```

## Test Cases
```
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [1]
Output: 1
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The key insight is to find the pivot point where the rotation occurs.
- The time complexity of the solution is O(log n), making it efficient for large inputs.
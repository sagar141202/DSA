# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem asks to find the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then rotated (or shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array because it was initially `[0, 1, 2, 4, 5, 6, 7]` and then rotated by 4 positions. The minimum element in this array is `0`. The array can contain duplicates and the rotation can be to the left or right. The constraints are that the array is non-empty and contains at least one element.

## Approach
The approach to solve this problem is to use a modified binary search algorithm that can handle the rotation. The idea is to compare the middle element with the rightmost element and decide which half to continue searching in.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left];
    }
};
```

## Test Cases
```
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [1, 2, 3, 4, 5]
Output: 1
```

## Key Takeaways
- The array can be rotated to the left or right, and the rotation can be by any number of positions.
- The array can contain duplicates, which can make the problem more challenging.
- The modified binary search algorithm can handle the rotation and find the minimum element in O(n) time complexity.
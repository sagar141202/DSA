# Find Minimum in Rotated Sorted Array

## Problem Statement
Given a rotated sorted array, find the minimum element. The array was initially sorted in ascending order, but it was rotated an unknown number of times. For example, given the array [3, 4, 5, 1, 2], the minimum element is 1. The array can contain duplicates and the rotation can be to the right or left. The size of the array will be in the range [1, 5000]. The elements in the array will be in the range [-5000, 5000].

## Approach
We will use a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm will divide the array into two halves and determine which half contains the minimum element. This process will be repeated until the minimum element is found.

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
        int left = 0;
        int right = nums.size() - 1;
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
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
Input: [1, 2, 3, 4, 5]
Output: 1
```

## Key Takeaways
- The binary search algorithm can be modified to find the minimum element in a rotated sorted array.
- The algorithm should handle duplicate elements in the array.
- The time complexity of the algorithm can be O(n) in the worst case when the array contains all duplicate elements.
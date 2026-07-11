# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order but has been rotated an unknown number of times. For example, the array [4, 5, 6, 7, 0, 1, 2] is a rotated sorted array where the minimum element is 0. The array may contain duplicate elements. The goal is to find the minimum element in the array.

## Approach
The approach involves using a modified binary search algorithm to find the minimum element in the rotated sorted array. The algorithm checks the middle element of the array and compares it with the last element to determine which half of the array the minimum element is in.

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
Input: [3, 3, 1, 3]
Output: 1
```

## Key Takeaways
- The minimum element in a rotated sorted array can be found using a modified binary search algorithm.
- The algorithm checks the middle element of the array and compares it with the last element to determine which half of the array the minimum element is in.
- The time complexity of the algorithm is O(n) in the worst case when all elements are the same.
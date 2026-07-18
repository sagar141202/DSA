# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then its elements were rotated (shifted) by some number of positions. For example, the array [3, 4, 5, 1, 2] is a rotated sorted array because it can be obtained by rotating the sorted array [1, 2, 3, 4, 5] by 3 positions. The problem assumes that there are no duplicates in the array and that the array is non-empty. The goal is to write a function that takes a rotated sorted array as input and returns the minimum element in the array.

## Approach
The approach to solving this problem is to use a modified binary search algorithm. The idea is to find the pivot point where the rotation occurred, which is the point where the smallest element is located. We can do this by comparing the middle element of the array with the last element. If the middle element is greater than the last element, then the pivot point must be in the right half of the array. Otherwise, it must be in the left half.

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
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
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
```

## Key Takeaways
- The problem can be solved using a modified binary search algorithm.
- The pivot point where the rotation occurred is the point where the smallest element is located.
- The time complexity of the solution is O(log n), which makes it efficient for large inputs.
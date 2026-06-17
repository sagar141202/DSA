# Find Minimum in Rotated Sorted Array

## Problem Statement
The problem requires finding the minimum element in a rotated sorted array. A rotated sorted array is an array that was initially sorted in ascending order, but then rotated (or shifted) by some number of positions. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated sorted array. The minimum element in this array is `0`. The array can contain duplicate elements. The constraints are: the array will not be empty, and there will be at least one element in the array.

## Approach
The algorithm uses a modified binary search approach to find the minimum element. If the middle element is greater than the rightmost element, the minimum element must be in the right half. If the middle element is less than or equal to the rightmost element, the minimum element must be in the left half.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
- The algorithm has a time complexity of O(n) in the worst case when all elements are the same.
- The algorithm has a space complexity of O(1) as it only uses a constant amount of space.
- The algorithm uses a modified binary search approach to find the minimum element in the rotated sorted array.
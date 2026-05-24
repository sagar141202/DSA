# Find Minimum in Rotated Sorted Array

## Problem Statement
Given a rotated sorted array, find the minimum element. The array was initially sorted in ascending order, but it was rotated an unknown number of times. For example, if the original array was [1, 2, 3, 4, 5], it could have been rotated to [3, 4, 5, 1, 2] or [5, 1, 2, 3, 4]. The constraints are that the array is non-empty and contains distinct elements.

## Approach
The approach is to use a modified binary search algorithm to find the minimum element in the rotated array. The algorithm checks the middle element and compares it with the rightmost element to determine which half the minimum element is in. This process is repeated until the minimum element is found.

## Complexity
- Time: O(log n)
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
            // minimum element is in the right half
            left = mid + 1;
        } else {
            // minimum element is in the left half
            right = mid;
        }
    }
    return nums[left];
}
```

## Test Cases
```
Input: [3, 4, 5, 1, 2]
Output: 1
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

## Key Takeaways
- The modified binary search algorithm is used to find the minimum element in the rotated array.
- The time complexity is O(log n) due to the use of binary search.
- The space complexity is O(1) as no extra space is used.
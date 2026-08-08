# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If `k` is larger than the length of the array, return `-1`. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`.

## Approach
The algorithm uses the `sort` function from the C++ Standard Template Library (STL) to sort the array in descending order. It then checks if `k` is within the bounds of the array and returns the `k`th element if it is.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    // Check if k is within the bounds of the array
    if (k < 1 || k > nums.size()) {
        return -1;
    }
    
    // Sort the array in descending order
    sort(nums.rbegin(), nums.rend());
    
    // Return the kth element
    return nums[k - 1];
}
```

## Test Cases
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

## Key Takeaways
- The `sort` function in C++ can be used to sort arrays in ascending or descending order.
- The `rbegin` and `rend` functions are used to get reverse iterators for the array, which can be used to sort the array in descending order.
- It's essential to check the bounds of `k` to handle edge cases where `k` is larger than the length of the array.
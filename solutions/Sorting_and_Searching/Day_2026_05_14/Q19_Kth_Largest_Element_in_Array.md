# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and k is within the range [1, nums.size()]. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The approach is to sort the array in descending order and then return the element at index `k-1`. This is because array indices in C++ start from 0, so the kth largest element will be at index `k-1`. We can use the built-in `sort` function in C++ to sort the array.

## Complexity
- Time: O(n log n)
- Space: O(1) if sorting is done in-place, O(n) if a new array is created for sorting

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    // Sort the array in descending order
    sort(nums.begin(), nums.end(), greater<int>());
    
    // Return the element at index k-1
    return nums[k-1];
}
```

## Test Cases
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1], k = 1
Output: 1
```

## Key Takeaways
- The `sort` function in C++ can be used to sort arrays in ascending or descending order.
- When using the `sort` function with a custom comparator (like `greater<int>`), it sorts the array in descending order.
- Array indices in C++ start from 0, so the kth largest element will be at index `k-1`.
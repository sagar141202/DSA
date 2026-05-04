# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and k is within the range [1, nums.size()]. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because the 2nd largest element in the array is `5`. If `nums = [3, 3, 3, 3]` and `k = 2`, the output should still be `3` because all elements are the same.

## Approach
The approach is to use the sort function in C++ to sort the array in descending order. Then, we can simply return the element at index `k-1` to get the kth largest element. This is because array indices in C++ start at 0.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        // Return the element at index k-1
        return nums[k-1];
    }
};
```

## Test Cases
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Input: nums = [3, 3, 3, 3], k = 2
Output: 3
```

## Key Takeaways
- The sort function in C++ can be used with reverse iterators to sort an array in descending order.
- Array indices in C++ start at 0, so the kth largest element is at index `k-1`.
- This solution has a time complexity of O(n log n) due to the sort operation.
# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the element that would be at index `k-1` if the array were sorted in descending order. The input array `nums` will have at least `k` elements, and `k` will be between 1 and the length of `nums` (inclusive). For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the `k`th largest element is `5`.

## Approach
The approach involves using the `std::sort` function from the C++ Standard Template Library to sort the array in descending order, then returning the element at index `k-1`. Alternatively, we can use a partial sort or a heap data structure for more efficiency.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        // Return the kth largest element
        return nums[k-1];
    }
};
```

## Test Cases
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

## Key Takeaways
- The `std::sort` function can be used with reverse iterators to sort an array in descending order.
- The `std::nth_element` function can be used for a more efficient partial sort.
- A heap data structure can also be used to find the kth largest element in O(n log k) time.
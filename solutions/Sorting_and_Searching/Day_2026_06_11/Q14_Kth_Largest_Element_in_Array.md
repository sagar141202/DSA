# Kth Largest Element in Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the `k`th largest element in the array. The array can contain duplicate elements and the `k`th largest element is the `k`th element when the array is sorted in descending order. The constraints are: `1 <= k <= nums.size()` and `nums.size()` will be at most 10^4.

## Approach
The algorithm uses the sorting approach to find the `k`th largest element. The idea is to sort the array in descending order and then return the element at index `k-1`. This is because array indices in C++ start at 0.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    // Sort the array in descending order
    sort(nums.rbegin(), nums.rend());
    
    // Return the kth largest element
    return nums[k-1];
}
```

## Test Cases
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1,2,3,4,5], k = 1
Output: 5
```

## Key Takeaways
- The problem can be solved by sorting the array in descending order.
- The `k`th largest element is the element at index `k-1` in the sorted array.
- The time complexity of the solution is O(n log n) due to the sorting operation.
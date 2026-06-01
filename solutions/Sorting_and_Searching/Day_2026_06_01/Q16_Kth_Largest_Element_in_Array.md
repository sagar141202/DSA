# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()` and `nums` contains distinct elements. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5` because the array in descending order is `[6,5,4,3,2,1]` and the element at index `1` is `5`.

## Approach
The algorithm uses the `std::sort` function from the C++ Standard Library to sort the array in descending order, then returns the element at index `k-1`. Alternatively, a priority queue or a partial sorting algorithm like `std::nth_element` can be used for a more efficient solution.

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

// Alternative solution using std::nth_element
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Use std::nth_element to partially sort the array
        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        // Return the kth largest element
        return nums[k-1];
    }
};
```

## Test Cases
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1], k = 1
Output: 1
```

## Key Takeaways
- The `std::sort` function can be used to sort the array in descending order by passing `nums.rbegin()` and `nums.rend()` as the range.
- The `std::nth_element` function can be used to partially sort the array, which is more efficient than sorting the entire array.
- The `greater<int>()` function is used as the comparison function for `std::nth_element` to sort the array in descending order.
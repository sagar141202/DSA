# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and k is within the range [1, nums.size()]. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5` because the 2nd largest element in the array is `5`. If there are duplicate elements, they should be treated as distinct elements.

## Approach
We can use the sorting approach to solve this problem by sorting the array in descending order and then returning the element at index `k-1`. Alternatively, we can use a priority queue to store the k largest elements.

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
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Input: nums = [1,2,3,4,5], k = 1
Output: 5
```

## Key Takeaways
- The sorting approach has a time complexity of O(n log n) due to the sorting operation.
- The priority queue approach has a time complexity of O(n log k) because we only need to store the k largest elements in the queue.
- We can also use the `nth_element` function in C++ to find the kth largest element in linear time on average.
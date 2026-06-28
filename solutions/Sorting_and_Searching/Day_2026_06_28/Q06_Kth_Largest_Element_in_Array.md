# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()`. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`, because the array in descending order is `[6, 5, 4, 3, 2, 1]`, and the element at index `1` is `5`.

## Approach
The approach to solve this problem is to use the sorting algorithm to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue or the `nth_element` function in C++ to find the `k`th largest element.

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
        
        // Return the element at index k-1
        return nums[k-1];
    }
};

// Alternatively, using priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq;
        
        // Push all elements into the priority queue
        for (int num : nums) {
            pq.push(num);
        }
        
        // Pop k-1 elements from the priority queue
        for (int i = 0; i < k-1; i++) {
            pq.pop();
        }
        
        // The top element is the kth largest
        return pq.top();
    }
};

// Alternatively, using nth_element
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Use nth_element to find the kth largest element
        nth_element(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
        
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
- The `sort` function in C++ can be used to sort the array in descending order by passing `rbegin()` and `rend()` as arguments.
- The `priority_queue` in C++ is a max heap by default, so it can be used to find the kth largest element.
- The `nth_element` function in C++ can be used to find the kth largest element in linear time on average.
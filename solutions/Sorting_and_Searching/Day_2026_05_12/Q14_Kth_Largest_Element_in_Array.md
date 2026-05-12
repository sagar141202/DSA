# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and can be unsorted. The kth largest element is the element that would be at index `k-1` if the array were sorted in descending order. For example, if the input array is `[3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array. The constraints are `1 <= k <= nums.size()` and the array can contain integers in the range `[-10^4, 10^4]`.

## Approach
The approach is to use the `sort` function in C++ to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to store the k largest elements.

## Complexity
- Time: O(n log n)
- Space: O(1) for the sort approach, O(k) for the priority queue approach

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

// Alternatively, using a priority queue
int findKthLargestPriorityQueue(vector<int>& nums, int k) {
    priority_queue<int> pq;
    for (int num : nums) {
        pq.push(num);
    }
    for (int i = 0; i < k - 1; i++) {
        pq.pop();
    }
    return pq.top();
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
- The problem can be solved using sorting or a priority queue.
- The time complexity of the sorting approach is O(n log n) and the space complexity is O(1).
- The time complexity of the priority queue approach is O(n log k) and the space complexity is O(k).
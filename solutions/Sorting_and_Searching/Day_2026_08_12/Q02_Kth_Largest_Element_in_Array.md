# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()` and that the input array is non-empty. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the `k`th largest element is `5`.

## Approach
We can use the `sort` function in C++ to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to store the `k` largest elements.

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

// Alternatively, using a priority queue
int findKthLargestPriorityQueue(vector<int>& nums, int k) {
    priority_queue<int> pq;
    for (int num : nums) {
        pq.push(num);
    }
    for (int i = 0; i < k-1; i++) {
        pq.pop();
    }
    return pq.top();
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
- The problem can be solved using sorting or a priority queue.
- The time complexity of the sorting solution is O(n log n), while the time complexity of the priority queue solution is O(n log k).
- The space complexity of both solutions is O(n), where n is the size of the input array.
# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The kth largest element is the element at the kth position when the array is sorted in descending order. If there are duplicate elements, their order does not matter. For example, given `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5` because the array in descending order is `[6,5,4,3,2,1]` and the 2nd largest element is `5`. The constraints are `1 <= k <= nums.size()` and `nums` contains only integers.

## Approach
The approach is to use the built-in sort function in C++ to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to store the k largest elements. The algorithm first checks if k is within the bounds of the array, then proceeds with the sorting or priority queue approach.

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
        // Return the kth largest element
        return nums[k-1];
    }
};

// Alternative solution using priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        // Iterate over the array
        for (int num : nums) {
            // Push the element into the min heap
            minHeap.push(num);
            // If the size of the min heap is greater than k, pop the smallest element
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        // The top of the min heap is the kth largest element
        return minHeap.top();
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
- Use the built-in sort function in C++ to sort the array in descending order.
- Alternatively, use a min heap to store the k largest elements and return the top of the heap.
- Always check if k is within the bounds of the array to avoid index out of range errors.
# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If the array has less than `k` elements, return -1. For example, given `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because the array in descending order is `[6, 5, 4, 3, 2, 1]` and the 2nd largest element is `5`. The array can have duplicate elements and the input array is not guaranteed to be sorted.

## Approach
We can use the `std::sort` function in C++ to sort the array in descending order, then return the `k-1`th element. Alternatively, we can use a priority queue to keep track of the `k` largest elements. The algorithm will iterate over the array, pushing elements into the priority queue and popping the smallest element when the queue size exceeds `k`.

## Complexity
- Time: O(n log n) for sorting, O(n log k) for priority queue
- Space: O(n) for sorting, O(k) for priority queue

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Sort the array in descending order
        sort(nums.rbegin(), nums.rend());
        
        // Return the k-1th element
        if (k > nums.size()) {
            return -1;
        }
        return nums[k-1];
    }
};

// Alternative solution using priority queue
class Solution2 {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a priority queue to keep track of the k largest elements
        priority_queue<int, vector<int>, greater<int>> pq;
        
        // Iterate over the array
        for (int num : nums) {
            // Push the element into the priority queue
            pq.push(num);
            
            // If the queue size exceeds k, pop the smallest element
            if (pq.size() > k) {
                pq.pop();
            }
        }
        
        // Return the top element of the priority queue
        return pq.top();
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
- To find the kth largest element in an array, we can sort the array in descending order and return the k-1th element.
- We can also use a priority queue to keep track of the k largest elements, which has a better time complexity when k is much smaller than the array size.
- The choice of algorithm depends on the specific constraints of the problem.
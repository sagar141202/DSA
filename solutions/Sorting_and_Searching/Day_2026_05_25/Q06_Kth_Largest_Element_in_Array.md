# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and the value of k is guaranteed to be within the bounds of the array. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
We can solve this problem by sorting the array in descending order and then returning the element at index `k-1`. Alternatively, we can use a priority queue to store the k largest elements.

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

// Alternatively, we can use a priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Iterate over the array
        for (int num : nums) {
            // Push the element into the heap
            minHeap.push(num);
            
            // If the heap size is greater than k, pop the smallest element
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // The top of the heap is the kth largest element
        return minHeap.top();
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
- The problem can be solved using sorting or a priority queue.
- The time complexity of the sorting approach is O(n log n) while the time complexity of the priority queue approach is O(n log k).
- The space complexity of both approaches is O(n) in the worst case.
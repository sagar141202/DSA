# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and the value of `k` will be in the range `[1, nums.size()]`. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`, which is the 2nd largest element in the array.

## Approach
The algorithm uses a priority queue to store the elements of the array. It iterates over the array, pushing each element into the priority queue. Then, it pops the largest element from the queue `k-1` times. The top element of the queue after this process is the kth largest element.

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
        
        // The top element of the min heap is the kth largest element
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
- We can use a min heap to find the kth largest element in an array.
- The time complexity of this approach is O(n log k) because we are pushing and popping elements from the min heap.
- The space complexity is O(k) because we are storing the k largest elements in the min heap.
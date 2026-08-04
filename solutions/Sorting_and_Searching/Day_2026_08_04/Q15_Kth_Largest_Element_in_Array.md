# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. The array can contain duplicate elements and the value of `k` is within the bounds of the array (i.e., `1 <= k <= nums.size()`). For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The approach to solve this problem is to use a min-heap data structure to store the `k` largest elements encountered so far. We iterate through the array, and for each element, we check if the heap has less than `k` elements or if the current element is larger than the smallest element in the heap.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min-heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Iterate through the array
        for (int num : nums) {
            // If the heap has less than k elements, push the current element into the heap
            if (minHeap.size() < k) {
                minHeap.push(num);
            } 
            // If the heap has k elements and the current element is larger than the smallest element in the heap
            else if (num > minHeap.top()) {
                // Remove the smallest element from the heap and push the current element into the heap
                minHeap.pop();
                minHeap.push(num);
            }
        }
        
        // The kth largest element is the smallest element in the heap
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
- We use a min-heap to efficiently keep track of the `k` largest elements encountered so far.
- The time complexity is O(n log k) because we perform a heap operation for each element in the array, and each heap operation takes O(log k) time.
- The space complexity is O(k) because we store at most `k` elements in the heap.
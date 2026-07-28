# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the element that would be at index `k-1` if the array were sorted in descending order. If there are duplicate elements, the `k`th largest element is the one that appears first in the sorted array. The array can contain both positive and negative integers, and `k` is within the range of the array length. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the output should be `5`, because `5` is the second largest element in the array.

## Approach
The approach to solve this problem is to use a priority queue to store the elements of the array. We can use the `std::priority_queue` in C++ to achieve this. The priority queue will automatically sort the elements in descending order, and we can then pop the top element `k-1` times to find the `k`th largest element.

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
        // Create a min heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        // Iterate over the array
        for (int num : nums) {
            // Push the element into the min heap
            minHeap.push(num);
            
            // If the size of the min heap is greater than k, pop the top element
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
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [1,2,3,4,5], k = 1
Output: 5

Input: nums = [1,2,3,4,5], k = 5
Output: 1
```

## Key Takeaways
- Use a min heap to store the k largest elements.
- The time complexity is O(n log k) because we are pushing and popping elements from the min heap.
- The space complexity is O(k) because we are storing at most k elements in the min heap.
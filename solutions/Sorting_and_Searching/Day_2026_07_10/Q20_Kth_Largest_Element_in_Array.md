# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If `k` is larger than the number of elements in the array, return `-1`. The array can contain duplicate elements and the range of `k` is `1 <= k <= 10^5`. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because the array in descending order is `[6, 5, 4, 3, 2, 1]` and the 2nd largest element is `5`.

## Approach
We can use a priority queue to store the elements of the array and then pop the queue `k-1` times to get the `k`th largest element. Alternatively, we can use the `nth_element` function in C++ which partially sorts the array such that the `k`th element is in its final sorted position.

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
- Use a min-heap to store the k largest elements to achieve O(n log k) time complexity.
- The `nth_element` function in C++ can also be used to solve this problem with a time complexity of O(n) on average.
- Always check the constraints of the problem to determine the most efficient solution.
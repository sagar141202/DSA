# Kth Largest Element in Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. The input array `nums` contains at least `k` elements, and `k` is between 1 and the length of `nums` (inclusive). For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`, which is the 2nd largest element in the array.

## Approach
The approach involves using a priority queue to store the elements of the array. We then pop the largest element from the queue `k-1` times, and the `k`th largest element will be at the top of the queue. Alternatively, we can use the `nth_element` function in C++ or the `sorted` function in Python to find the `k`th largest element.

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
        // Create a min-heap and push all elements into it
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for (int num : nums) {
            // Push the element into the min-heap
            minHeap.push(num);
            // If the size of the min-heap is greater than k, pop the smallest element
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        // The kth largest element is at the top of the min-heap
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
- We can use a min-heap to find the kth largest element in an array.
- The time complexity of the solution is O(n log n) due to the use of the priority queue.
- The space complexity of the solution is O(n) as we need to store all elements in the priority queue.
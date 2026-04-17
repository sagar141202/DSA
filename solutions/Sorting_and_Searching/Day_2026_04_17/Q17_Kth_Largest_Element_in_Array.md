# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If `k` is larger than the length of the array, return `-1`. For example, given `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The algorithm uses the `std::sort` function from the C++ Standard Library to sort the array in descending order, then returns the `k-1`th element. Alternatively, a min-heap can be used to find the kth largest element more efficiently.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findKthLargest(vector<int>& nums, int k) {
    // Check if k is larger than the length of the array
    if (k > nums.size()) {
        return -1;
    }
    
    // Sort the array in descending order
    sort(nums.rbegin(), nums.rend());
    
    // Return the kth largest element
    return nums[k-1];
}

// Alternatively, using a min-heap
int findKthLargestHeap(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    // Push all elements into the min-heap
    for (int num : nums) {
        minHeap.push(num);
        
        // If the size of the min-heap is larger than k, pop the smallest element
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }
    
    // The top of the min-heap is the kth largest element
    return minHeap.top();
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
- The problem can be solved by sorting the array in descending order and returning the `k-1`th element.
- A min-heap can be used to find the kth largest element more efficiently, especially for large arrays.
- Always check the constraints of the problem and handle edge cases.
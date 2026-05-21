# Kth Largest Element in Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the kth largest element in the array. The kth largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()`. For example, if `nums = [3,2,1,5,6,4]` and `k = 2`, the kth largest element is `5`.

## Approach
We can use the sort function from the C++ Standard Library to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to find the kth largest element. The priority queue will store the k largest elements seen so far.

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

// Alternatively, using a priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a min heap to store the k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        // Iterate over the array
        for (int num : nums) {
            // Push the current element into the min heap
            minHeap.push(num);
            // If the size of the min heap exceeds k, pop the smallest element
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
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Key Takeaways
- The problem can be solved by sorting the array in descending order and returning the kth element.
- A priority queue can be used to find the kth largest element in O(n log k) time complexity.
- The choice of approach depends on the size of the input array and the value of k.
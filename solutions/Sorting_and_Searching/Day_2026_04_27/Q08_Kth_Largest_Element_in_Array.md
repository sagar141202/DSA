# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. The array can contain duplicate elements and the value of `k` is within the range of the array length. If the array is empty or `k` is larger than the array length, return an error message. For example, if the input array is `[3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The approach is to use a sorting algorithm to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to store the `k` largest elements. The algorithm will iterate through the array, pushing elements into the priority queue and popping the smallest element when the queue size exceeds `k`.

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
        // Create a priority queue to store the k largest elements
        priority_queue<int> maxHeap;
        // Iterate through the array and push elements into the priority queue
        for (int num : nums) {
            maxHeap.push(num);
        }
        // Pop the largest element k-1 times
        for (int i = 0; i < k-1; i++) {
            maxHeap.pop();
        }
        // Return the kth largest element
        return maxHeap.top();
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
- The problem can be solved using sorting or priority queue.
- The time complexity of the sorting solution is O(n log n) and the space complexity is O(n).
- The time complexity of the priority queue solution is O(n log k) and the space complexity is O(k).
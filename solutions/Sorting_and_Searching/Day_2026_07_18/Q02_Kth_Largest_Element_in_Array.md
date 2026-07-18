# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. The array can contain duplicate elements and the value of `k` is guaranteed to be within the bounds of the array. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The approach to solve this problem is to use a sorting algorithm to sort the array in descending order, then return the element at index `k-1`. Alternatively, we can use a priority queue to store the `k` largest elements.

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
        
        // Return the element at index k-1
        return nums[k-1];
    }
};

// Alternatively, using priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a priority queue to store the k largest elements
        priority_queue<int> pq;
        
        // Iterate over the array and push elements into the priority queue
        for (int num : nums) {
            pq.push(num);
        }
        
        // Pop elements from the priority queue k-1 times
        for (int i = 0; i < k-1; i++) {
            pq.pop();
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
- The problem can be solved using sorting or priority queue.
- The time complexity of the sorting approach is O(n log n) and the space complexity is O(n).
- The time complexity of the priority queue approach is O(n log k) and the space complexity is O(k).
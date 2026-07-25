# Kth Largest Element in Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, find the kth largest element in the array. The kth largest element is the element that would be at index `k-1` if the array were sorted in descending order. You may assume that `1 <= k <= nums.size()` and that the array contains distinct elements. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`, which is the 2nd largest element in the array.

## Approach
The approach is to sort the array in descending order and then return the element at index `k-1`. Alternatively, we can use a priority queue to store the k largest elements. The algorithm will iterate through the array, adding elements to the priority queue and removing the smallest element when the queue size exceeds `k`.

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
```

## Test Cases
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

## Key Takeaways
- We can solve this problem using sorting or a priority queue.
- The time complexity of the sorting approach is O(n log n), while the priority queue approach has a time complexity of O(n log k).
- The space complexity of the sorting approach is O(n), while the priority queue approach has a space complexity of O(k).
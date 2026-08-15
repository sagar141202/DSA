# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, find the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If there are duplicate elements, the `k`th largest element is the `k`th element when the array is sorted in descending order and the duplicate elements are considered as separate elements. The array `nums` contains only integers and `k` is within the range of the array size.

## Approach
We can use a priority queue to store the elements of the array and then remove the largest element `k-1` times to find the `k`th largest element. Alternatively, we can use the `nth_element` function in C++ which partially sorts the array to find the `k`th largest element. We can also use the QuickSelect algorithm, a variant of the QuickSort algorithm, to find the `k`th largest element.

## Complexity
- Time: O(n log n) for sorting approach, O(n) for QuickSelect approach on average
- Space: O(1) for in-place sorting, O(n) for priority queue approach

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Use nth_element function to partially sort the array
        nth_element(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
        // Return the kth largest element
        return nums[k-1];
    }
};

// Alternatively, using priority queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Create a priority queue to store the elements of the array
        priority_queue<int> pq;
        // Push all elements into the priority queue
        for (int num : nums) {
            pq.push(num);
        }
        // Remove the largest element k-1 times
        for (int i = 0; i < k-1; i++) {
            pq.pop();
        }
        // Return the kth largest element
        return pq.top();
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
- The `nth_element` function can be used to partially sort the array and find the `k`th largest element.
- The QuickSelect algorithm can be used to find the `k`th largest element with an average time complexity of O(n).
- The priority queue approach can be used to find the `k`th largest element with a time complexity of O(n log n).
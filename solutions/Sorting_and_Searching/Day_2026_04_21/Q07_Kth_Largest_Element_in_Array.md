# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. The `k`th largest element is the `k`th element when the array is sorted in descending order. If `k` is larger than the length of the array, return `-1`. For example, given `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`, which is the 2nd largest element in the array.

## Approach
The approach is to use the `sort` function in C++ to sort the array in descending order and then return the `k-1`th element. Alternatively, we can use a priority queue to store the `k` largest elements.

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
        
        // Return the k-1th element
        if (k > nums.size()) {
            return -1;
        }
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
- The `sort` function in C++ can be used to sort the array in descending order by using `rbegin()` and `rend()`.
- The `priority_queue` data structure can be used to store the `k` largest elements.
- The time complexity of the solution is O(n log n) due to the sorting operation.
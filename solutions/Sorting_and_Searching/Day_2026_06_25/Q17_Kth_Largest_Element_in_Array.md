# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and the kth largest element should be found in O(n log n) time complexity or better. For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5` because `5` is the 2nd largest element in the array.

## Approach
The solution involves sorting the array in descending order and then returning the kth element. This can be achieved using the built-in sort function in C++. Alternatively, a priority queue can be used to find the kth largest element.

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
        
        // Return the kth element
        return nums[k - 1];
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
- The time complexity of the solution is O(n log n) due to the sorting operation.
- The space complexity of the solution is O(n) for the sorting operation in the worst case.
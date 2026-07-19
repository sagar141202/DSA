# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative numbers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which can be obtained from the subarray `[4,-1,2,1]`. If the array is empty, return `0`.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It works by iterating through the array and at each step, it decides whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum found so far.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Initialize variables to store the maximum sum and the current sum
        int max_sum = INT_MIN;
        int current_sum = 0;
        
        // Iterate over the array
        for (int num : nums) {
            // Update the current sum
            current_sum = max(num, current_sum + num);
            // Update the maximum sum
            max_sum = max(max_sum, current_sum);
        }
        
        return max_sum;
    }
};
```

## Test Cases
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Input: nums = [1]
Output: 1
Input: nums = [0]
Output: 0
Input: nums = []
Output: 0
```

## Key Takeaways
- Kadane's algorithm has a linear time complexity, making it efficient for large arrays.
- The algorithm uses a single pass through the array, making it space-efficient.
- The maximum sum of a subarray can be negative if all numbers in the array are negative.
# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which corresponds to the subarray `[4,-1,2,1]`.

## Approach
Kadane's algorithm is used to solve this problem by iterating through the array and at each position, deciding whether to continue the current subarray or start a new one. The maximum sum of subarray ending at the current position is calculated and updated accordingly.

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
        // Initialize the maximum sum and the current sum to the first element of the array
        int maxSum = nums[0];
        int currentSum = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update the current sum to be the maximum of the current number and the sum of the current number and the previous current sum
            currentSum = max(nums[i], currentSum + nums[i]);
            // Update the maximum sum to be the maximum of the current maximum sum and the current sum
            maxSum = max(maxSum, currentSum);
        }
        
        // Return the maximum sum
        return maxSum;
    }
};
```

## Test Cases
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Input: nums = [1]
Output: 1
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Key Takeaways
- Kadane's algorithm is an efficient solution for finding the maximum subarray sum in an array.
- The algorithm works by iterating through the array and at each position, deciding whether to continue the current subarray or start a new one.
- The maximum sum of subarray ending at the current position is calculated and updated accordingly.
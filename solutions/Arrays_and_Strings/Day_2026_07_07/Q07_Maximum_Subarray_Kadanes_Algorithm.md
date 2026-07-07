# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which can be obtained from the subarray `[4,-1,2,1]`.

## Approach
Kadane's Algorithm is used to solve this problem, which iterates through the array and at each position, it decides whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum of subarray ending at each position and the maximum sum of subarray seen so far.

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
- Kadane's Algorithm is an efficient solution for the maximum subarray problem with a time complexity of O(n).
- The algorithm iterates through the array only once, making it suitable for large inputs.
- The maximum sum of subarray is updated at each position, allowing the algorithm to keep track of the maximum sum seen so far.
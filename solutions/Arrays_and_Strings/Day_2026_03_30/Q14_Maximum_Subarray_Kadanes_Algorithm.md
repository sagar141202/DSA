# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative numbers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which is the sum of the subarray `[4,-1,2,1]`. If the input array is empty, return 0.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It iterates over the array, at each step deciding whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum seen so far.

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
        // Handle edge case where input array is empty
        if (nums.empty()) {
            return 0;
        }

        // Initialize variables to keep track of maximum sum and current sum
        int maxSum = nums[0];
        int currentSum = nums[0];

        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Decide whether to continue the current subarray or start a new one
            currentSum = max(nums[i], currentSum + nums[i]);
            // Update the maximum sum if the current sum is greater
            maxSum = max(maxSum, currentSum);
        }

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
- Kadane's algorithm is an efficient solution for finding the maximum subarray sum with a time complexity of O(n).
- It's essential to handle edge cases, such as an empty input array.
- The algorithm's ability to decide whether to continue or start a new subarray at each step is key to its effectiveness.
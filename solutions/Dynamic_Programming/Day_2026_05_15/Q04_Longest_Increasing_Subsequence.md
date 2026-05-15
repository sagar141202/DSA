# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in `nums`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101]`, so the length of the LIS is `4`. The length of `nums` is between `1` and `2500`, and each element in `nums` is between `0` and `10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the LIS ending at that index. The final result is the maximum value in this table. We iterate through the array, updating the table based on whether the current element can extend any existing increasing subsequence.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        // Initialize a table to store the length of LIS ending at each position
        vector<int> dp(n, 1);
        
        // Initialize the maximum length of LIS
        int max_length = 1;
        
        // Iterate through the array
        for (int i = 1; i < n; i++) {
            // For each element, check all previous elements
            for (int j = 0; j < i; j++) {
                // If the current element can extend the increasing subsequence
                if (nums[i] > nums[j]) {
                    // Update the length of LIS ending at the current position
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            // Update the maximum length of LIS
            max_length = max(max_length, dp[i]);
        }
        
        // Return the maximum length of LIS
        return max_length;
    }
};
```

## Test Cases
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Input: nums = [7, 6, 5, 4, 3, 2]
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows us to efficiently compute the length of the LIS by avoiding redundant computations.
- The time complexity is O(n^2) due to the nested loops, where n is the length of the input array.
- The space complexity is O(n) for storing the dynamic programming table.
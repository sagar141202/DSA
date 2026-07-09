# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS) in the array. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, in the array `[10, 22, 9, 33, 21, 50, 41, 60, 80]`, the longest increasing subsequence is `[10, 22, 33, 50, 60, 80]` with a length of `6`. The array can contain duplicate elements and can be empty.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. The `dp` array is filled by iterating over the array and updating `dp[i]` based on the maximum length of increasing subsequences ending at previous indices.

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
        
        // Initialize dp array with 1s
        vector<int> dp(n, 1);
        
        // Initialize max length of LIS
        int maxLength = 1;
        
        // Fill dp array
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLength = max(maxLength, dp[i]);
        }
        
        return maxLength;
    }
};
```

## Test Cases
```
Input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 5
Input: [5, 4, 3, 2, 1]
Output: 1
```

## Key Takeaways
- The longest increasing subsequence problem has a time complexity of O(n^2) using dynamic programming.
- The problem can be solved using a bottom-up dynamic programming approach by filling a `dp` array.
- The `dp` array can be used to keep track of the maximum length of increasing subsequences ending at each index.
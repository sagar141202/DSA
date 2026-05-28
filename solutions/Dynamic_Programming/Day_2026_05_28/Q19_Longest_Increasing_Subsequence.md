# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The LIS is the longest subsequence that is strictly increasing. For example, given `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 101, 18]` and its length is `5`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the LIS ending at that index. The intuition is to maintain a table `dp` where `dp[i]` is the length of the LIS ending at index `i`. We iterate through the array and for each element, we check all previous elements to see if they are smaller, and if so, we update `dp[i]` accordingly.

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
        
        vector<int> dp(n, 1);
        int maxLen = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLen = max(maxLen, dp[i]);
        }
        
        return maxLen;
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The `dp` table is used to store the lengths of the LIS ending at each index, which helps to avoid redundant computations.
- The time complexity can be improved to O(n log n) using a binary search approach.
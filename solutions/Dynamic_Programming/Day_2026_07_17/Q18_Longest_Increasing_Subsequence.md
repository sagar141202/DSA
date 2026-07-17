# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums` of length `n`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the longest increasing subsequence is `[2, 3, 7, 101, 18]`, so the output should be `5`. The input array `nums` will have a length of at least `1` and at most `1000`, and each element will be between `0` and `10^9`.

## Approach
The algorithm uses dynamic programming to build up a table where each entry represents the length of the longest increasing subsequence ending at that index. The final result is the maximum value in this table. We initialize the table with all ones, since a single element is an increasing subsequence of length one. Then we fill up the table by comparing each element with all previous elements.

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
        // Initialize dp table with all ones
        vector<int> dp(n, 1);
        
        // Fill up the dp table
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                // If current element is greater than previous element, update dp[i]
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        // Find the maximum value in the dp table
        return *max_element(dp.begin(), dp.end());
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The `lengthOfLIS` function uses a bottom-up dynamic programming approach to fill up the dp table.
- The final result is the maximum value in the dp table, which represents the length of the longest increasing subsequence.
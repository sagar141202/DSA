# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums`, find the length of the longest increasing subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The problem has the following constraints: `1 <= nums.length <= 1000` and `0 <= nums[i] <= 10^9`. For example, if `nums = [10,9,2,5,3,7,101,18]`, the output should be `4` because the longest increasing subsequence is `[2,3,7,101]`.

## Approach
The algorithm uses dynamic programming to solve the problem, where each state `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. The intuition is to compare each element with all previous elements and update `dp[i]` accordingly.

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
        vector<int> dp(n, 1);
        int maxi = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxi = max(maxi, dp[i]);
        }
        return maxi;
    }
};
```

## Test Cases
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Input: nums = [0,1,0,3,2,3]
Output: 4
Input: nums = [7,6,5,4,3,2]
Output: 1
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The `dp` array is used to store the lengths of the longest increasing subsequences ending at each index.
- The time complexity of the solution is O(n^2) due to the nested loops, where n is the length of the input array.
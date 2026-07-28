# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A palindromic subsequence is a subsequence that reads the same backward as forward. The input string `s` consists of lowercase English letters, and its length is between 1 and 1000. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table `dp` to store the lengths of the longest palindromic subsequences for all substrings of `s`. We start by filling the diagonal of the table, where the length of the longest palindromic subsequence for a substring of length 1 is 1. Then, we fill the rest of the table in a bottom-up manner.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindromicSubsequence(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the diagonal of the table
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the rest of the table
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + (length == 2 ? 0 : dp[i + 1][j - 1]);
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: "banana"
Output: 5
Input: "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach is used to avoid redundant calculations and improve efficiency.
- The `dp` table is used to store the lengths of the longest palindromic subsequences for all substrings of `s`.
- The time complexity is O(n^2) due to the nested loops used to fill the `dp` table.
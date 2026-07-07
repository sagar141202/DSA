# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backwards as forwards. For example, in the string "banana", the longest palindromic subsequence is "anana". The input string `s` will have a length between 1 and 1000, and will only contain lowercase letters.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The table is filled in a bottom-up manner, starting from substrings of length 1 and 2, and then using previously computed values to fill in the rest of the table.

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
        // Create a 2D table to store the lengths of palindromic subsequences
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the table for substrings of length 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = 2;
            } else {
                dp[i][i + 1] = 1;
            }
        }
        
        // Fill the rest of the table
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // The length of the longest palindromic subsequence is stored in dp[0][n - 1]
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: "banana"
Output: 3
Input: "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The 2D table is used to store the lengths of palindromic subsequences for substrings of `s`.
- The final answer is stored in the top-right corner of the table, `dp[0][n - 1]`.
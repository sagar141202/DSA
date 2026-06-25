# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a subsequence that reads the same backward as forward. The string `s` consists of lowercase English letters and has a length of at most 1000 characters. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The algorithm fills the table in a bottom-up manner, starting from substrings of length 1 and 2, and then extending to longer substrings.

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
        int n = s.length();
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
        
        // Fill the table for longer substrings
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
        
        // The length of the longest palindromic subsequence is stored in dp[0][n-1]
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: s = "banana"
Output: 5
Input: s = "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems, such as the longest palindromic subsequence problem.
- The 2D table `dp` is used to store the lengths of palindromic subsequences for substrings of `s`, which helps to avoid redundant computations.
- The algorithm fills the table in a bottom-up manner, starting from substrings of length 1 and 2, and then extending to longer substrings.
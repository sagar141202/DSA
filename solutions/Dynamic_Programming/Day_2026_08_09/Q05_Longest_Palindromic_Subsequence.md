# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backward as forward. The input string `s` consists of only lowercase English letters and has a length of at most 1000 characters. For example, given the string "bbbab", the longest palindromic subsequence is "bbbb" with a length of 4.

## Approach
The algorithm uses dynamic programming to break down the problem into smaller subproblems and store their solutions to avoid redundant computation. It initializes a 2D table `dp` where `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The final solution is stored in `dp[0][n-1]`, where `n` is the length of the input string.

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
        // Initialize a 2D table to store the lengths of palindromic subsequences
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = 2;
            } else {
                dp[i][i + 1] = 1;
            }
        }
        
        // Check for lengths greater than 2
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
Input: "bbbab"
Output: 4
Input: "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach is effective for solving problems that have overlapping subproblems.
- The use of a 2D table `dp` allows for efficient storage and retrieval of solutions to subproblems.
- The final solution is obtained by considering all possible substrings and their corresponding palindromic subsequences.
# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backward as forward. The string `s` has a length of up to 1000 characters, and it only contains lowercase English letters. For example, given the string `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4.

## Approach
The approach to solve this problem is to use dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. We fill up the table by considering all possible substrings and checking if the first and last characters are the same.

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
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the diagonal of the table with 1s
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
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
Input: s = "bbbab"
Output: 4
Input: s = "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant computations and improve efficiency.
- The 2D table `dp` is used to store the lengths of the longest palindromic subsequences for all possible substrings.
- The final answer is stored in the cell `dp[0][n - 1]`, where `n` is the length of the input string.
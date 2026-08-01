# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that reads the same backward as forward. The input string `s` will have a length of at most 1000 characters. For example, if `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4. If `s = "cbbd"`, the longest palindromic subsequence is `"bb"` with a length of 2.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. It iterates over the string, filling the table in a bottom-up manner. The intuition is to consider all possible substrings and determine if the first and last characters are the same, in which case they can be part of the palindromic subsequence.

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
        // Create a 2D table to store lengths of palindromic subsequences
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
Input: s = "bbbab"
Output: 4
Input: s = "cbbd"
Output: 2
```

## Key Takeaways
- Dynamic programming is used to efficiently compute the lengths of all possible palindromic subsequences.
- The solution has a time complexity of O(n^2) and space complexity of O(n^2), where n is the length of the input string.
- The approach involves filling a 2D table in a bottom-up manner, considering all substrings of the input string.
# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that reads the same backward as forward. The input string `s` will have a length between 1 and 1000, and it will only contain lowercase English letters.

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table `dp` such that `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. We fill up the table in a bottom-up manner, starting from substrings of length 1 and going up to the full string.

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
        
        // Initialize the diagonal of the dp table to 1, since a single character is always a palindrome
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill up the dp table for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = 2;
            } else {
                dp[i][i + 1] = 1;
            }
        }
        
        // Fill up the dp table for substrings of length 3 and more
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
        
        // The answer is stored in the top-right corner of the dp table
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
- The dynamic programming table `dp` is used to store the lengths of the longest palindromic subsequences for all possible substrings of the input string.
- The table is filled up in a bottom-up manner, starting from substrings of length 1 and going up to the full string.
- The answer is stored in the top-right corner of the `dp` table, which represents the length of the longest palindromic subsequence in the full input string.
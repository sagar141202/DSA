# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that is also a palindrome. The input string `s` has a length of up to 1000 characters. For example, if `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i..j]`. The algorithm fills the table in a bottom-up manner, starting from substrings of length 1 and 2.

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
        // Create a 2D table to store the lengths of longest palindromic subsequences
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
        
        // Fill the table for substrings of length 3 and above
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
Input: s = "bbbab"
Output: 4
Input: s = "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The 2D table `dp` is used to store the lengths of the longest palindromic subsequences for each substring of `s`.
- The time complexity is O(n^2) because we need to fill the 2D table of size n x n.
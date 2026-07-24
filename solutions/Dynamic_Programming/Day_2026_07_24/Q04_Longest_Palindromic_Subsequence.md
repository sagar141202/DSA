# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A palindromic subsequence is a subsequence that reads the same backward as forward. The string `s` can contain up to 1000 characters, and all characters are lowercase English letters. For example, given `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

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
        
        // Fill the table in a bottom-up manner
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;  // A single character is always a palindrome
            for (int j = i + 1; j < n; j++) {
                // If the first and last characters are the same, consider them as part of the palindrome
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    // Otherwise, consider the maximum length without the first or last character
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // The length of the longest palindromic subsequence is stored in the top-left corner of the table
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
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by avoiding redundant calculations.
- The 2D table `dp` is used to store the lengths of palindromic subsequences for all possible substrings of `s`.
- The final result is stored in the top-left corner of the table, `dp[0][n - 1]`, where `n` is the length of the input string `s`.
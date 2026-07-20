# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A palindromic subsequence is a subsequence that reads the same backwards as forwards. The string `s` can contain up to 1000 characters, and all characters are lowercase English letters. For example, given the string "bbbab", the longest palindromic subsequence is "bbbb" with a length of 4.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The table is filled in a bottom-up manner, starting from substrings of length 1 and 2, and then extending to longer substrings. The final answer is stored in the top-right cell of the table.

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
        
        // Initialize the diagonal of the table with 1s
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    // If the first and last characters match, add 2 to the length of the subsequence
                    dp[i][j] = (length == 2) ? 2 : dp[i + 1][j - 1] + 2;
                } else {
                    // If the first and last characters do not match, take the maximum of the two subsequences
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // The final answer is stored in the top-right cell of the table
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
- The dynamic programming approach is used to avoid redundant computations and improve the efficiency of the algorithm.
- The 2D table `dp` is used to store the lengths of palindromic subsequences, where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`.
- The final answer is stored in the top-right cell of the table, which represents the length of the longest palindromic subsequence in the entire string `s`.
# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A palindromic subsequence is a subsequence that reads the same backward as forward. The input string `s` can contain up to 1000 characters. For example, if `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4. If `s = "cbbd"`, the longest palindromic subsequence is `"bb"` with a length of 2.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring from index `i` to `j`. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
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
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
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
- Dynamic programming can efficiently solve problems that have overlapping subproblems, like the Longest Palindromic Subsequence.
- The choice of the state (in this case, `dp[i][j]`) is crucial for solving dynamic programming problems.
- Filling the dynamic programming table in a bottom-up manner helps avoid redundant computations and ensures that each subproblem is solved only once.
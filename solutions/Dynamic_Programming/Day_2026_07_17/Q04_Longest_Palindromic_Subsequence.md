# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "bbbab" has a longest palindromic subsequence of "bbbb". The string `s` consists of lowercase English letters and has a length between 1 and 1000.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The intuition is to fill the table in a bottom-up manner, considering all possible substrings.

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
            dp[i][i] = 1;  // Substrings of length 1 are always palindromes
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    // If the first and last characters match, consider the substring in between
                    dp[i][j] = 2 + dp[i + 1][j - 1];
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
Input: "bbbab"
Output: 4
Input: "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and solve the problem efficiently.
- The 2D table `dp` is used to store the lengths of palindromic subsequences for all possible substrings.
- The final answer is stored in the top-left corner of the table, `dp[0][n - 1]`.
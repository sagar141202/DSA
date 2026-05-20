# Longest Palindromic Subsequence

## Problem Statement
Given a sequence, find the length of its longest palindromic subsequence. A palindromic subsequence is a subsequence that reads the same backward as forward. For example, in the sequence "banana", the longest palindromic subsequence is "anana". The sequence can contain lowercase English letters, and its length can range from 1 to 1000.

## Approach
The approach to solve this problem is to use dynamic programming to build a 2D table where each cell represents the length of the longest palindromic subsequence in the substring from the current start index to the current end index. We can then fill up the table in a bottom-up manner by considering all possible substrings.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestPalindromicSubsequence(string s) {
    int n = s.length();
    // Create a 2D table to store the lengths of longest palindromic subsequences
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
```

## Test Cases
```
Input: "banana"
Output: 3
Input: "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations by storing the results of subproblems in a table.
- The 2D table dp is used to store the lengths of the longest palindromic subsequences for all substrings.
- The final result is stored in dp[0][n-1], where n is the length of the input string.
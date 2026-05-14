# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that reads the same backward as forward. The input string `s` will have a length of at most 1000 characters. For example, if `s = "banana"`, the longest palindromic subsequence is `"anana"` with a length of 5.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The solution fills this table in a bottom-up manner, considering all possible substrings of `s`. If the characters at positions `i` and `j` are the same, the length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence of the substring `s[i+1...j-1]`. If the characters are different, the length is the maximum length of the longest palindromic subsequences of `s[i+1...j]` and `s[i...j-1]`.

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
        // Create a table to store results of subproblems
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Check for substring of length 2
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
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
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
Input: s = "banana"
Output: 5
Input: s = "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach efficiently solves the problem by avoiding redundant computations.
- The table `dp` stores the lengths of the longest palindromic subsequences for all substrings of `s`.
- The time complexity is O(n^2) due to the nested loops, and the space complexity is also O(n^2) for storing the `dp` table.
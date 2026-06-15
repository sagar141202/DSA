# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backwards as forwards. The input string `s` will have a length between 1 and 1000, and will only contain lowercase letters. For example, if `s = "bbbab"`, the longest palindromic subsequence is `"bbbb"` with a length of 4.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The algorithm iterates over the string, filling in the table by considering all possible substrings. If the characters at positions `i` and `j` are the same, the length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence in the substring `s[i+1...j-1]`.

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
        
        // Fill the diagonal with 1s, since single characters are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                // If the characters at positions i and j are the same, consider them as part of the palindrome
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + (length > 2 ? dp[i + 1][j - 1] : 0);
                } else {
                    // Otherwise, consider the maximum length without the character at position i or j
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // The length of the longest palindromic subsequence is stored in the top-right corner of the table
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
- The dynamic programming approach allows us to avoid redundant computations by storing the lengths of longest palindromic subsequences in a table.
- The table is filled in a bottom-up manner, starting with substrings of length 2 and considering all possible substrings.
- The final result is stored in the top-right corner of the table, representing the length of the longest palindromic subsequence in the entire string.
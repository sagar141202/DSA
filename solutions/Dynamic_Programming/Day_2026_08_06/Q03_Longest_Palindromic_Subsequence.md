# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest subsequence that is a palindrome. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "abc" has the following palindromic subsequences: "a", "b", "c", "aba", etc. The string only contains lowercase English letters. The length of the string is between 1 and 1000.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the length of the longest palindromic subsequence in the substring. The algorithm fills the table in a bottom-up manner, starting from substrings of length 1 and going up to the entire string. If the characters at the start and end of the substring are the same, the length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence of the substring in between.

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
                    dp[i][j] = 2 + dp[i + 1][j - 1];
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
Input: "bbbab"
Output: 4
Input: "cbbd"
Output: 2
```

## Key Takeaways
- Dynamic programming is used to solve the problem by building a 2D table.
- The table is filled in a bottom-up manner, starting from substrings of length 1.
- If the characters at the start and end of the substring are the same, the length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence of the substring in between.
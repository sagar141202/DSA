# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that appears the same when its characters are reversed. The input string `s` will have a length of at most 1000 characters. For example, given the string "bbbab", the longest palindromic subsequence is "bbbb" with a length of 4.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

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
        
        // Fill the table in a bottom-up manner
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;  // A single character is always a palindrome
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    // If the first and last characters match, consider the substring in between
                    dp[i][j] = 2 + (j - i > 1 ? dp[i + 1][j - 1] : 0);
                } else {
                    // If the first and last characters do not match, consider the maximum length without one of them
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
- The dynamic programming approach allows us to avoid redundant computations by storing the lengths of palindromic subsequences in a table.
- The table is filled in a bottom-up manner, starting from the smallest substrings and considering all possible substrings.
- The final answer is stored in the top-left corner of the table, representing the length of the longest palindromic subsequence in the entire input string.
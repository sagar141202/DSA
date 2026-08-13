# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that is also a palindrome, i.e., it reads the same backward as forward. The input string `s` consists of only lowercase English letters and has a length between 1 and 1000.

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
            dp[i][i] = 1; // A single character is always a palindrome
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    // If the characters match, consider the substring in between
                    dp[i][j] = 2 + (j - i > 1 ? dp[i + 1][j - 1] : 0);
                } else {
                    // If the characters do not match, consider the maximum of the two substrings
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
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
Input: "bbbab"
Output: 4
Input: "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by avoiding redundant calculations.
- The 2D table `dp` is used to store the lengths of palindromic subsequences for all possible substrings.
- The algorithm has a time complexity of O(n^2) due to the nested loops used to fill the `dp` table.
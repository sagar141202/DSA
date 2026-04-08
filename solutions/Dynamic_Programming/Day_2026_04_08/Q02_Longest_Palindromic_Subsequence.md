# Longest Palindromic Subsequence

## Problem Statement
The problem requires finding the length of the longest palindromic subsequence in a given string. A palindromic subsequence is a sequence that reads the same backward as forward. The input string can contain any ASCII characters, and the length of the string is between 1 and 1000. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The approach involves using dynamic programming to build a 2D table where each cell [i][j] represents the length of the longest palindromic subsequence in the substring from index i to j. The table is filled in a bottom-up manner, starting from substrings of length 1 and 2, and then expanding to longer substrings.

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
        
        // Fill the table for longer substrings
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
};
```

## Test Cases
```
Input: "banana"
Output: 5
Input: "abc"
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by avoiding redundant calculations.
- The 2D table provides a clear and organized way to store and access the lengths of palindromic subsequences for different substrings.
- The fill order of the table is crucial, as it ensures that the lengths of shorter palindromic subsequences are computed before the lengths of longer ones.
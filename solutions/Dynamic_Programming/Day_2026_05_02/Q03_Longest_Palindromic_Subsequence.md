# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that appears the same backward as forward. For example, "aba" is a palindrome, but "abc" is not. The input string can contain any ASCII characters and has a length between 1 and 1000. The goal is to write a function that returns the length of the longest palindromic subsequence.

## Approach
The approach to solve this problem is to use dynamic programming to build a 2D table where each cell [i][j] represents the length of the longest palindromic subsequence in the substring from index i to j. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

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
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                
                // If the first and last characters are the same, consider them as part of the palindrome
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1];
                } 
                // Otherwise, consider the maximum length without the first or last character
                else {
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
Input: "banana"
Output: 3
Input: "bbbab"
Output: 4
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by avoiding redundant calculations.
- The 2D table helps to store and reuse the lengths of palindromic subsequences for different substrings.
- The algorithm has a time complexity of O(n^2) and a space complexity of O(n^2), making it suitable for strings of moderate length.
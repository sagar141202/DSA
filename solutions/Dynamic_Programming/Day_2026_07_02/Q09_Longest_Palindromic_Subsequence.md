# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. A palindromic subsequence is a subsequence that is also a palindrome. The input string `s` has a length of up to 1000 characters. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the length of the longest palindromic subsequence in the substring from the corresponding row and column indices. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

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
        // Create a 2D table to store the lengths of the longest palindromic subsequences
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the table in a bottom-up manner
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1; // A single character is always a palindrome
            for (int j = i + 1; j < n; j++) {
                // If the current characters match, consider them as part of the palindrome
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } 
                // Otherwise, consider the maximum length without the current characters
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
Input: s = "banana"
Output: 5
Input: s = "bbbab"
Output: 4
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The Longest Palindromic Subsequence problem can be solved by building a 2D table in a bottom-up manner.
- The time complexity of the solution is O(n^2) due to the nested loops, and the space complexity is also O(n^2) for the 2D table.
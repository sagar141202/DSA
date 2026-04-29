# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that reads the same backwards as forwards. The input string will have a length between 1 and 1000 characters, and it will only contain lowercase English letters. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell [i][j] represents the length of the longest palindromic subsequence in the substring from index i to j. The algorithm fills the table in a bottom-up manner by considering all possible substrings.

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
        for (int i = n - 1; i >= 0; --i) {
            dp[i][i] = 1;  // A single character is always a palindrome
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j]) {
                    // If the first and last characters match, consider the substring in between
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    // If the first and last characters do not match, consider the maximum length without one of them
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
Input: "banana"
Output: 5
Input: "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and solve the problem efficiently.
- The 2D table is filled in a bottom-up manner to ensure that the lengths of shorter palindromic subsequences are computed before the lengths of longer ones.
- The final result is stored in the cell [0][n - 1] of the table, where n is the length of the input string.
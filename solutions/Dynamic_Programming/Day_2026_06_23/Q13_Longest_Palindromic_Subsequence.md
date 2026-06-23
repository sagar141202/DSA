# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backward as forward. The string `s` has a length of up to 1000 characters. For example, if `s = "banana"`, the longest palindromic subsequence is `"anana"` with a length of 5. If `s = "abc"`, the longest palindromic subsequence is `"a"` or `"b"` or `"c"` with a length of 1.

## Approach
The problem can be solved using dynamic programming by creating a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. The solution builds up by filling the table in a bottom-up manner. If `s[i]` is equal to `s[j]`, then the length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence in the substring `s[i+1...j-1]`.

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
        // Create a 2D table to store the lengths of the longest palindromic subsequences
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Fill the diagonal of the table with 1, since a single character is always a palindrome
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                
                // If the first and last characters are the same, consider them as part of the palindrome
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + (length > 2 ? dp[i + 1][j - 1] : 0);
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
Input: s = "banana"
Output: 5
Input: s = "abc"
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by avoiding redundant calculations.
- The 2D table `dp` is used to store the lengths of the longest palindromic subsequences for each substring of `s`.
- The solution has a time complexity of O(n^2) and a space complexity of O(n^2), where n is the length of the input string `s`.
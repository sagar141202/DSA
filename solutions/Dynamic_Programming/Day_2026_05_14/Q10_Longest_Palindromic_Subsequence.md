# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a sequence that reads the same backwards as forwards. The string `s` has a length of up to 1000 characters. For example, if `s = "banana"`, the longest palindromic subsequence is `"anana"` with a length of 5.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the lengths of palindromic subsequences. The table is filled in a bottom-up manner, starting from substrings of length 1 and 2. The length of the longest palindromic subsequence is then stored in the top-right corner of the table.

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
        
        // Fill the table for substrings of length 3 and more
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
- The dynamic programming approach is suitable for this problem because it has overlapping subproblems and optimal substructure.
- The 2D table is used to store the lengths of palindromic subsequences, which helps to avoid redundant calculations.
- The time complexity of the solution is O(n^2) due to the nested loops used to fill the table.
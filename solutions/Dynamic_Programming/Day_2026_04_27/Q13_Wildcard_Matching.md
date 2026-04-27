# Wildcard Matching

## Problem Statement
The wildcard matching problem is a classic problem in computer science where we are given two strings: a pattern string and a text string. The pattern string can contain two special characters: '?' and '*'. The '?' character matches any single character, while the '*' character matches any sequence of characters, including an empty sequence. The goal is to determine whether the text string matches the pattern string. For example, if the pattern string is "a*b" and the text string is "aab", then the output should be true because the '*' character in the pattern string can match the extra 'a' character in the text string.

## Approach
We can solve this problem using dynamic programming by creating a 2D table to store the matching status of substrings. The table will have (m+1) x (n+1) cells, where m and n are the lengths of the pattern and text strings respectively. We will fill the table in a bottom-up manner, starting from the base cases and then using the previously computed values to fill the rest of the table.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        
        // Create a 2D table to store the matching status of substrings
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base cases
        dp[0][0] = true;
        
        // Fill the first row of the table
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        // Return the result
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s = "aab", p = "a*b"
Output: true

Input: s = "aa", p = "a"
Output: false

Input: s = "", p = "*"
Output: true
```

## Key Takeaways
- The '*' character in the pattern string can match any sequence of characters, including an empty sequence.
- The '?' character in the pattern string can match any single character.
- We can use dynamic programming to solve this problem efficiently by creating a 2D table to store the matching status of substrings.
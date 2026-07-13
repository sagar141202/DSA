# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire input string matches the pattern, and false otherwise. For example, "aa" matches "a*" and "ab" matches ".*".

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the matching status of substrings. We start by initializing the base cases, and then fill in the rest of the table based on the pattern and input string. The key intuition is to consider the last character of the pattern and the input string, and decide whether to include or exclude it from the match.

## Complexity
- Time: O(len(s) * len(p))
- Space: O(len(s) * len(p))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize base cases
        dp[m][n] = true;
        for (int i = m; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                // If the current characters match or the pattern is '.', consider including the current character
                bool match = i < m && (p[j] == s[i] || p[j] == '.');
                if (j + 1 < n && p[j + 1] == '*') {
                    // If the pattern has a '*', consider including or excluding the current character
                    dp[i][j] = dp[i][j + 2] || (match && dp[i + 1][j]);
                } else {
                    // If the pattern does not have a '*', consider including the current character
                    dp[i][j] = match && dp[i + 1][j + 1];
                }
            }
        }
        
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: s = "aa", p = "a*"
Output: true
Input: s = "ab", p = ".*"
Output: true
Input: s = "aab", p = "c*a*b"
Output: true
```

## Key Takeaways
- Use dynamic programming to build a 2D table for storing the matching status of substrings.
- Consider the last character of the pattern and the input string, and decide whether to include or exclude it from the match.
- Handle the '*' character in the pattern by considering including or excluding the preceding element.
# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the `*` and `?` wildcards. The `*` wildcard matches any sequence of characters (including an empty sequence), and the `?` wildcard matches any single character. The function should return `true` if the input string matches the pattern, and `false` otherwise. The input string `s` and pattern `p` consist only of lowercase letters `a-z`, `*`, and `?`. The length of `s` is at most 100, and the length of `p` is at most 100.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `dp[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The table is filled in a bottom-up manner, considering the possibilities for the current characters in `s` and `p`. If the current character in `p` is `*`, it can match any sequence of characters in `s`, so we consider two possibilities: using the `*` to match zero characters in `s`, or using it to match one or more characters in `s`.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        // Initialize the base case where both strings are empty
        dp[0][0] = true;
        
        // Fill the first row, considering the '*' wildcard
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current character in p is '?', it matches any character in s
                if (p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                // If the current character in p is '*', consider two possibilities
                else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
                // If the current characters in s and p match, consider the match
                else {
                    dp[i][j] = (s[i - 1] == p[j - 1]) && dp[i - 1][j - 1];
                }
            }
        }
        
        // The result is stored in the bottom-right cell of the table
        return dp[n][m];
    }
};
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The `*` wildcard can match any sequence of characters, including an empty sequence.
- The `?` wildcard can match any single character.
- Dynamic programming can be used to solve the problem efficiently by building a 2D table to store the intermediate results.
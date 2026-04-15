# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `*` matches any sequence of characters (including an empty sequence).
- `?` matches any single character.
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Examples: 
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "cb", p = "?a"` Output: `false`
- Input: `s = "adceb", p = "*a*b"` Output: `true`
Constraints: 
- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `*`, and `?`.

## Approach
The problem can be solved using dynamic programming, where a 2D table is used to store the intermediate results of subproblems. The table `dp[i][j]` is `true` if the first `i` characters in `s` match the first `j` characters in `p`. 
The final result will be stored in `dp[s.length()][p.length()]`.

## Complexity
- Time: O(s.length() * p.length())
- Space: O(s.length() * p.length())

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isMatch(string s, string p) {
    int m = s.length(), n = p.length();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    
    // Initialize base case
    dp[0][0] = true;
    
    // Initialize the first row
    for (int j = 1; j <= n; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
    
    // Fill up the rest of the table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            } else if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }
    
    return dp[m][n];
}
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "a*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations by storing the results of subproblems in a table.
- The base case is when both strings are empty, in which case they match.
- The `*` character can match any sequence of characters, including an empty sequence, so it can be used to match any number of characters in the input string.
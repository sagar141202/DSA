# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Examples:
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "cb", p = "?a"` Output: `false`
- Input: `s = "adceb", p = "*a*b"` Output: `true`
Constraints: 
- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters
- `p` contains only lowercase English letters, `?`, and `*`

## Approach
We can solve this problem using dynamic programming by creating a 2D array `dp` where `dp[i][j]` represents whether the first `i` characters in `s` match the first `j` characters in `p`.
The algorithm iterates through both strings, updating the `dp` array based on whether the current characters match or if a wildcard is encountered.

## Complexity
- Time: O(n*m) where n and m are the lengths of `s` and `p` respectively
- Space: O(n*m) for the `dp` array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length(), m = p.length();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        // Initialize base case
        dp[0][0] = true;
        
        // Handle '*' in the pattern
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill dp array
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        return dp[n][m];
    }
};
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
- Use dynamic programming to solve string matching problems with wildcards.
- Initialize base cases carefully, especially when dealing with '*' in the pattern.
- Handle '?' and '*' separately in the algorithm to ensure correct matching.
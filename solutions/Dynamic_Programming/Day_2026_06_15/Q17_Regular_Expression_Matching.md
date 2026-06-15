# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string matches the pattern, and false otherwise. For example, `isMatch("aa", "a")` returns false, while `isMatch("aa", "a*")` returns true. The input string `s` and pattern `p` only contain characters from the set `{a-z, ., *}`.

## Approach
We can solve this problem using dynamic programming by maintaining a 2D table `dp` where `dp[i][j]` represents whether the first `i` characters in the string match the first `j` characters in the pattern. The table is filled in a bottom-up manner based on the current characters in the string and pattern.

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
        int m = s.length(), n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base case where the pattern is empty
        dp[m][n] = true;
        
        // Fill the last row of the table
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (p[j] == '*') {
                    // If the current character in the pattern is '*', we have two options:
                    // 1. Ignore the '*' and move to the next character in the pattern
                    // 2. Use the '*' to match the current character in the string
                    dp[i][j] = dp[i][j + 1] || (dp[i + 1][j] && (p[j - 1] == s[i] || p[j - 1] == '.'));
                } else {
                    // If the current character in the pattern is not '*', we simply check if it matches the current character in the string
                    dp[i][j] = dp[i + 1][j + 1] && (p[j] == s[i] || p[j] == '.');
                }
            }
        }
        
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "a*"
Output: true
Input: s = "ab", p = ".*"
Output: true
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and solve the problem efficiently.
- The 2D table `dp` is used to store the intermediate results and build up the solution to the original problem.
- The base case where the pattern is empty is used to initialize the table, and the rest of the table is filled in a bottom-up manner based on the current characters in the string and pattern.
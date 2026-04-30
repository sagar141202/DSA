# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` matches any single character
- `*` matches zero or more of the preceding element.
The function should return `true` if the entire string `s` matches the entire pattern `p`, otherwise return `false`.
For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", ".a")` returns `true`, and `isMatch("ab", ".*")` returns `true`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table `dp` where `dp[i][j]` is `true` if the first `i` characters in `s` match the first `j` characters in `p`.
We can fill up this table by comparing characters from `s` and `p` and using the previous values in the table.
The final result will be stored in `dp[s.size()][p.size()]`.

## Complexity
- Time: O(s.size() * p.size())
- Space: O(s.size() * p.size())

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base case
        dp[m][n] = true;
        
        // Fill the last row
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                // If the current characters match or p[j] is '.'
                if (s[i] == p[j] || p[j] == '.') {
                    dp[i][j] = dp[i + 1][j + 1];
                } 
                // If p[j] is '*'
                else if (p[j] == '*') {
                    // Two cases: 
                    // 1. We ignore the '*' and the preceding character
                    // 2. We use the '*' to match the current character in s
                    dp[i][j] = dp[i][j + 1] || (dp[i + 1][j] && (s[i] == p[j - 1] || p[j - 1] == '.'));
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
- The `dp` table is used to store the intermediate results to avoid redundant computation.
- The base case is `dp[s.size()][p.size()] = true`, which means an empty string matches an empty pattern.
- The `*` in the pattern can match zero or more of the preceding element, so we consider two cases when filling the table.
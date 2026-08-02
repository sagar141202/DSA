# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` matches any single character
- `*` matches zero or more of the preceding element.
The matching should cover the entire string, not just a part of it. Return `true` if the string matches the pattern, otherwise return `false`.
Examples:
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "ab", p = ".*"` Output: `true`

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the intermediate results of subproblems. We iterate through the string and pattern, updating the table based on whether the current characters match or if the pattern character is `.` or `*`.

## Complexity
- Time: O(length of s * length of p)
- Space: O(length of s * length of p)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize base case
        dp[m][n] = true;
        
        // Fill the last row where the pattern is empty
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // If the pattern character is '*', then it can match zero or more of the preceding character
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (i < m && (p[j - 1] == s[i] || p[j - 1] == '.') && dp[i + 1][j]);
                } 
                // If the pattern character is not '*', then it must match the current string character
                else {
                    dp[i][j] = i < m && (p[j] == s[i] || p[j] == '.') && dp[i + 1][j + 1];
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
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- The `*` in the pattern can match zero or more of the preceding character, which needs to be handled carefully.
- The `.` in the pattern can match any single character.
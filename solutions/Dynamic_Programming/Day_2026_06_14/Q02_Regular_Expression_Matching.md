# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string `s` matches the entire pattern `p`, otherwise return false. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "a*")` returns true, `isMatch("ab", ".*")` returns true.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the match status between substrings of `s` and subpatterns of `p`. We iterate through the table, filling in the values based on whether the current characters in `s` and `p` match or not. The '*' character is handled by considering two cases: zero occurrences and one or more occurrences of the preceding character.

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
        dp[m][n] = true;
        
        // handle '*' in p when s is empty
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // fill in the dp table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool match = s[i] == p[j] || p[j] == '.';
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || (match && dp[i + 1][j]);
                } else {
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
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "a*"
Output: true
Input: s = "ab", p = ".*"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Handle the '*' character by considering zero occurrences and one or more occurrences of the preceding character.
- Initialize the dp table carefully, especially when handling the '*' character in the pattern when the input string is empty.
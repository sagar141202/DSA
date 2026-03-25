# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. The '?' wildcard matches any single character, while the '*' wildcard matches any sequence of characters, including an empty sequence. The function should return true if the input string matches the pattern, and false otherwise. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "*")` returns true, and `isMatch("cb", "?a")` returns false. The input strings only contain lowercase English letters.

## Approach
The solution uses dynamic programming to build a 2D table where each cell represents whether the substring of `s` matches the substring of `p`. The '*' wildcard is handled by considering two cases: matching zero characters or matching one or more characters. The '?' wildcard is handled by always considering a match.

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
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[m][n] = true;
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                bool match = i < m && (p[j] == s[i] || p[j] == '?');
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (i < m && dp[i + 1][j]);
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
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
```

## Key Takeaways
- The '*' wildcard can match any sequence of characters, including an empty sequence.
- The '?' wildcard can match any single character.
- Dynamic programming can be used to efficiently solve the problem by building a 2D table of substring matches.
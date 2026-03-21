# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where: '.' matches any single character, '*' matches zero or more of the preceding element, and the matching should cover the entire string, not just a part of it. The function should return true if the string matches the pattern, otherwise false. For example, isMatch("aa", "a") returns false, isMatch("aa", "a*") returns true, and isMatch("ab", ".*") returns true.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents whether the first i characters in the string match the first j characters in the pattern. The solution iterates through the string and pattern, filling the table based on the current characters and the previous matches.

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
        
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                bool match = i < m && (p[j] == s[i] || p[j] == '.');
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || match && dp[i + 1][j];
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
- The '*' character in the pattern can match zero or more occurrences of the preceding character.
- The '.' character in the pattern can match any single character in the string.
- Dynamic programming is used to efficiently fill a 2D table that tracks matches between substrings and subpatterns.
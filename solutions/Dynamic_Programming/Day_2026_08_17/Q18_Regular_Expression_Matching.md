# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string `s` matches the entire pattern `p`, otherwise return false. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "a*")` returns true, and `isMatch("ab", ".*")` returns true.

## Approach
We will use dynamic programming to solve this problem by creating a 2D table to store the matching results of substrings and subpatterns. The table will be filled in a bottom-up manner, and the final result will be stored in the top-right corner of the table. We will handle the '*' character by considering two cases: zero occurrences and one or more occurrences of the preceding character.

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
        for (int i = m; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool match = i < m && (p[j] == s[i] || p[j] == '.');
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
- Use dynamic programming to solve regular expression matching problems with '.' and '*' characters.
- Create a 2D table to store the matching results of substrings and subpatterns.
- Handle the '*' character by considering two cases: zero occurrences and one or more occurrences of the preceding character.
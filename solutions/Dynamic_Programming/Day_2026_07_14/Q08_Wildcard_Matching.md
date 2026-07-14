# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. The '?' wildcard matches any single character, while the '*' wildcard matches any sequence of characters, including an empty sequence. The function should return `true` if the input string matches the pattern, and `false` otherwise. The input string `s` and pattern `p` consist only of lowercase English letters, '?' and '*'. The length of `s` is at most 200, and the length of `p` is at most 200.

## Approach
The solution uses dynamic programming to build a 2D table where each cell represents whether the corresponding substring of `s` matches the corresponding substring of `p`. The algorithm iterates over the input string and pattern, filling in the table based on the current characters and the '*' and '?' wildcards.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isMatch(string s, string p) {
    int n = s.size(), m = p.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
    dp[0][0] = true;
    for (int j = 1; j <= m; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
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
- The '*' wildcard can match any sequence of characters, including an empty sequence.
- The '?' wildcard matches any single character.
- Dynamic programming is used to efficiently fill in the 2D table and determine whether the input string matches the pattern.
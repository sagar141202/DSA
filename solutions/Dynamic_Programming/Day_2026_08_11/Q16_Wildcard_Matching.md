# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `'?'` and `'*'` wildcards. The `'?'` wildcard matches any single character, while the `'*'` wildcard matches any sequence of characters (including an empty sequence). Return `true` if the input string matches the pattern, and `false` otherwise. The input string only contains lowercase letters, and the pattern only contains lowercase letters, `'?'`, and `'*'`. The length of the input string is at most 2000, and the length of the pattern is at most 2000.

## Approach
The solution uses dynamic programming to track the matching status between the input string and the pattern. It initializes a 2D array `dp` where `dp[i][j]` represents whether the first `i` characters in the input string match the first `j` characters in the pattern. The algorithm iterates through the input string and the pattern, updating the `dp` array based on the current characters and the wildcard rules.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The dynamic programming approach is suitable for solving problems with overlapping subproblems, like the wildcard matching problem.
- The `'*'` wildcard can match any sequence of characters, including an empty sequence, which requires careful handling in the dynamic programming algorithm.
- The `dp` array is used to store the intermediate results and avoid redundant computation, reducing the time complexity to O(n*m).
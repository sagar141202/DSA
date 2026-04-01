# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where: '.' matches any single character, '*' matches zero or more of the preceding element, and the matching should cover the entire string, not just a part of it. The function should return `true` if the string matches the pattern, otherwise, it should return `false`. For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "a*")` returns `true`, `isMatch("ab", ".*")` returns `true`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the match status of substrings and subpatterns. We fill the table in a bottom-up manner, considering all possible matches between the input string and the pattern. The final result is stored in the last cell of the table.

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
- We use dynamic programming to solve this problem efficiently by avoiding redundant computation.
- The `dp` table is filled in a bottom-up manner, starting from the base case where both the input string and the pattern are empty.
- The '*' character in the pattern can match zero or more occurrences of the preceding character, which is handled by checking `dp[i][j + 2]` and `dp[i + 1][j]`.
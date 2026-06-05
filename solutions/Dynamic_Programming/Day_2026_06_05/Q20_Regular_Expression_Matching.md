# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` special characters. The `'.'` character matches any single character, and the `'*'` character matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. The input string `s` and pattern `p` consist only of lowercase letters `a-z`, `'.'`, and `'*'`. The length of `s` is at most 100, and the length of `p` is at most 100.

## Approach
We will use dynamic programming to solve this problem by creating a 2D table to store the match status of substrings and subpatterns. The table will be filled in a bottom-up manner, considering all possible matches between the input string and the pattern. The final result will be stored in the top-right corner of the table.

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
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (dp[i + 1][j] && (p[j - 1] == s[i] || p[j - 1] == '.'));
                } else {
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
- The `'*'` character in the pattern can match zero or more of the preceding element, which requires special handling in the dynamic programming table.
- The `'.'` character in the pattern can match any single character, which simplifies the comparison between the input string and the pattern.
- The dynamic programming table is filled in a bottom-up manner to ensure that all possible matches are considered.
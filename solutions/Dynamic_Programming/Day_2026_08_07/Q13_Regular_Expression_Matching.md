# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` matches any single character
- `*` matches zero or more of the preceding element.
The function should return `true` if the entire string `s` matches the entire pattern `p`, otherwise return `false`.
Examples:
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "ab", p = ".*"` Output: `true`

## Approach
We will use dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters in `s` match the first `j` characters in `p`.
The final result will be stored in the last cell of the table.
We iterate through `s` and `p`, updating the table based on whether the current characters match or if we encounter a `*`.

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
- Dynamic programming is key to solving this problem efficiently by avoiding redundant computations.
- The `*` character complicates the matching because it can match zero or more of the preceding element, requiring special handling in the DP table update logic.
- The DP table's final cell contains the result, indicating whether the entire string matches the entire pattern.
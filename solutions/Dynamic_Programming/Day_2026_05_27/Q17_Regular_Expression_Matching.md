# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where: 
- '.' matches any single character, 
- '*' matches zero or more of the preceding element. 
The function should return true if the entire string matches the pattern, otherwise false. 
For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "a*")` returns true, `isMatch("ab", ".*")` returns true.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the match status of substrings and subpatterns. 
We fill the table in a bottom-up manner by comparing characters and handling '*' and '.' cases. 
This approach allows us to avoid redundant computations and solve the problem efficiently.

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
        
        // Initialize base case
        dp[n][m] = true;
        
        // Fill the table in a bottom-up manner
        for (int i = n; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                bool match = (i < n && (p[j] == s[i] || p[j] == '.'));
                if (j + 1 < m && p[j + 1] == '*') {
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
- Dynamic programming can be used to solve regular expression matching problems efficiently by avoiding redundant computations.
- The '*' character in regular expressions can match zero or more occurrences of the preceding element, which needs to be handled carefully in the dynamic programming approach.
- The '.' character in regular expressions can match any single character, which can be handled by comparing the current character in the string with the pattern.
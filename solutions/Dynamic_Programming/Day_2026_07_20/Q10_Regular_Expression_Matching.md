# Regular Expression Matching
## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire input string matches the pattern, and false otherwise. The input string `s` and pattern `p` only contain characters from the set {a-z, ., *}. The length of `s` is at most 100, and the length of `p` is at most 100. For example, isMatch("aa","a") returns false, and isMatch("aa","a*") returns true.

## Approach
The approach to solve this problem is to use dynamic programming to build a 2D table where each cell [i][j] represents whether the first i characters in the string match the first j characters in the pattern. We fill up the table by comparing characters from the string and the pattern, and using the '*' wildcard to match zero or more preceding characters.

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
- Use dynamic programming to solve string matching problems with wildcards.
- Build a 2D table to track matches between the input string and the pattern.
- Handle the '*' wildcard by checking for matches with and without the preceding character.
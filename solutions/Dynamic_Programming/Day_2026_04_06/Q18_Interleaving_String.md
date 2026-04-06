# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings in a way that the order of characters in each string is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`. For example, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, the function should return `false` because `s3` is not an interleaving of `s1` and `s2`. However, if `s3 = "aadbbbccac"`, the function should return `true` because `s3` is an interleaving of `s1` and `s2`.

## Approach
We can solve this problem using dynamic programming. The idea is to create a 2D table where each cell represents whether the substrings of `s1` and `s2` can interleave to form the corresponding substring of `s3`. We then fill up this table in a bottom-up manner.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size(), n = s2.size();
        if (m + n != s3.size()) return false;
        
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        
        // Initialize the first row and column of the dp table
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        
        // Fill up the rest of the dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: false
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbccac"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve the interleaving string problem.
- Initialize the first row and column of the dp table based on the characters in `s1` and `s2` and the corresponding characters in `s3`.
- Fill up the rest of the dp table by checking if the current character in `s3` matches the current character in either `s1` or `s2`.
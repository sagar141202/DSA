# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in individual strings is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table where each cell represents whether the corresponding substrings of `s1` and `s2` can interleave to form the corresponding substring of `s3`. We fill the table in a bottom-up manner.

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
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        
        // Create a 2D table to store results of subproblems
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the table
        dp[0][0] = true;
        
        // Fill the first row
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        
        // Fill the first column
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }
        
        // Fill the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int k = i + j - 1;
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[k]) || (dp[i][j - 1] && s2[j - 1] == s3[k]);
            }
        }
        
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

## Key Takeaways
- The dynamic programming approach allows us to solve the problem efficiently by avoiding redundant computations.
- The 2D table `dp` is used to store the results of subproblems, where `dp[i][j]` represents whether the first `i` characters of `s1` and the first `j` characters of `s2` can interleave to form the first `i + j` characters of `s3`.
- The base cases are when either `s1` or `s2` is empty, in which case we can simply check if the corresponding substring of `s3` matches the non-empty string.
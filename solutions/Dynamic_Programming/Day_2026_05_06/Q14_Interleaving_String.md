# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in individual strings is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`. For example, given `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, the function should return `true` because `s3` is an interleaving of `s1` and `s2`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s1` and the first `j` characters of `s2` can interleave to form the first `i + j` characters of `s3`. The solution builds up this table iteratively based on character matches between `s1`, `s2`, and `s3`.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isInterleave(string s1, string s2, string s3) {
    int m = s1.size(), n = s2.size();
    if (m + n != s3.size()) return false;
    
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true;
    
    for (int i = 1; i <= m; ++i) {
        dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
    }
    
    for (int j = 1; j <= n; ++j) {
        dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
    }
    
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
        }
    }
    
    return dp[m][n];
}
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

## Key Takeaways
- The dynamic programming approach is essential for solving this problem efficiently by avoiding redundant computations.
- Initializing the base cases correctly (e.g., `dp[0][0]`, `dp[i][0]`, `dp[0][j]`) is crucial for the algorithm to work correctly.
- The final result is stored in `dp[m][n]`, which indicates whether `s3` is an interleaving of `s1` and `s2`.
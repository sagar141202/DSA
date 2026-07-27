# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in individual strings is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to track whether each substring of `s1` and `s2` can interleave to form a substring of `s3`. The table is filled in a bottom-up manner, considering all possible combinations of characters from `s1` and `s2` that can match the characters in `s3`.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size(), n = s2.size();
        if (m + n != s3.size()) return false;
        
        // Create a 2D table to store the interleaving status
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Base case: empty strings can interleave to form an empty string
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
- The dynamic programming approach helps to avoid redundant computations and improves the efficiency of the solution.
- The 2D table `dp` is used to store the interleaving status of substrings of `s1` and `s2` to form substrings of `s3`.
- The base cases and the filling of the table are crucial steps in the dynamic programming approach.
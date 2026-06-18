# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in individual strings is preserved. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. For example, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, the function should return `false` because `s3` is not an interleaving of `s1` and `s2`. However, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbbccca"`, the function should return `true`.

## Approach
We can solve this problem using dynamic programming by creating a 2D table where each cell represents whether the corresponding substrings of `s1` and `s2` can interleave to form the corresponding substring of `s3`. We fill the table in a bottom-up manner, checking for matches between characters in `s1`, `s2`, and `s3`.

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
        int m = s1.size();
        int n = s2.size();
        
        // Check if the length of s3 is equal to the sum of lengths of s1 and s2
        if (m + n != s3.size()) {
            return false;
        }
        
        // Create a 2D table to store the results of subproblems
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base cases
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
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        
        // Return the result
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: false
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbccca"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- Create a 2D table to store the results of subproblems and fill it in a bottom-up manner.
- Initialize the base cases and fill the table based on the problem constraints and conditions.
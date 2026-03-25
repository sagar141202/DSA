# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings in a way that the order of characters in each string is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. Note that the length of `s3` should be equal to the sum of lengths of `s1` and `s2`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the interleaving status of substrings of `s1` and `s2`. The algorithm iterates over `s1` and `s2` and checks if the current character in `s3` matches the current character in either `s1` or `s2`.

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
        if (m + n != s3.size()) return false;
        
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1];
        }
        
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j-1] && s2[j-1] == s3[j-1];
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
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

Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Key Takeaways
- The problem can be solved using dynamic programming with a 2D table to store the interleaving status of substrings.
- The time complexity is O(m*n), where m and n are the lengths of `s1` and `s2`, respectively.
- The space complexity is O(m*n) for the 2D table.
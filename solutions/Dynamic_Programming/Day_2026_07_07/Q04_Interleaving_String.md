# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in the individual strings is preserved. The length of `s3` must be equal to the sum of lengths of `s1` and `s2`. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. For example, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, then `s3` is an interleaving of `s1` and `s2`.

## Approach
We will use dynamic programming to solve this problem by creating a 2D table where each cell represents whether the substring of `s3` can be formed by interleaving the corresponding substrings of `s1` and `s2`. The final result will be stored in the last cell of the table.

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
        
        // Create a 2D table to store the dynamic programming results
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base cases
        dp[0][0] = true;
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        
        // Fill in the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        
        // The final result is stored in the last cell of the table
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
- The problem can be solved using dynamic programming by creating a 2D table to store the interleaving results of substrings.
- The time complexity is O(m*n), where m and n are the lengths of the input strings `s1` and `s2`, respectively.
- The space complexity is also O(m*n) due to the 2D table used to store the dynamic programming results.
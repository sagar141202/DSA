# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`. An interleaving of two strings is formed by taking characters from each string in an alternating manner, starting from the first character of each string. For example, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, then `s3` is an interleaving of `s1` and `s2`. However, if `s3 = "aadbbbaccc"`, then it is not an interleaving of `s1` and `s2`. The function should return `true` if `s3` is an interleaving of `s1` and `s2`, and `false` otherwise.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the interleaving status of substrings of `s1` and `s2`. We will iterate through `s1` and `s2` and check if the current character in `s3` matches the current character in either `s1` or `s2`.

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
        
        // If lengths of s1 and s2 do not add up to length of s3, it cannot be an interleaving
        if (m + n != s3.size()) {
            return false;
        }
        
        // Create a 2D table to store the interleaving status
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
                // If the current character in s3 matches the current character in s1, 
                // then check the interleaving status of the remaining strings
                if (s1[i - 1] == s3[i + j - 1]) {
                    dp[i][j] = dp[i - 1][j];
                }
                // If the current character in s3 matches the current character in s2, 
                // then check the interleaving status of the remaining strings
                if (s2[j - 1] == s3[i + j - 1]) {
                    dp[i][j] = dp[i][j] || dp[i][j - 1];
                }
            }
        }
        
        // The interleaving status of the entire strings is stored in the last cell
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
- The problem can be solved using dynamic programming by creating a 2D table to store the interleaving status of substrings of `s1` and `s2`.
- The time complexity of the solution is O(m*n), where m and n are the lengths of `s1` and `s2`, respectively.
- The space complexity of the solution is O(m*n), which is used to store the 2D table.
# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The problem can be solved using dynamic programming, where the state dp[i][j] represents the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T.

## Approach
The algorithm uses a 2D dynamic programming table to store the number of distinct subsequences. It iterates over the characters of S and T, updating the table based on whether the current characters match or not. The final result is stored in the last cell of the table.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
        
        // Initialize the base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters match, consider two cases: 
                // 1. The current character in S is used to match the current character in T.
                // 2. The current character in S is not used.
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters do not match, the current character in S cannot be used.
                else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[n][m];
    }
};
```

## Test Cases
```
Input: S = "rabbbit", T = "rabbit"
Output: 3
Input: S = "subscription", T = "subscription"
Output: 1
```

## Key Takeaways
- The problem can be solved using a 2D dynamic programming table to store the number of distinct subsequences.
- The state dp[i][j] represents the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T.
- The final result is stored in the last cell of the table, dp[n][m].
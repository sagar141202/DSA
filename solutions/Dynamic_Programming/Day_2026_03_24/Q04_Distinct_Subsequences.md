# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "abc" has 8 distinct subsequences: "", "a", "b", "c", "ab", "ac", "bc", and "abc". The length of both S and T will be in the range [1, 100]. 

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array dp where dp[i][j] represents the number of distinct subsequences of S[0...i] that equals T[0...j]. We fill up the dp array in a bottom-up manner. 

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
                // If the current characters in S and T are the same, 
                // we have two options: either include the current character in S or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters are different, we cannot include the current character in S
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
```

## Key Takeaways
- We use a 2D array dp to store the number of distinct subsequences of S that equals T.
- We fill up the dp array in a bottom-up manner by considering two options: either include the current character in S or not.
- The final answer is stored in dp[n][m] where n and m are the lengths of S and T respectively.
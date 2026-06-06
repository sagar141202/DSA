# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not. The length of both strings S and T will not exceed 100, and the characters in both strings are lowercase English letters.

## Approach
The problem can be solved by using dynamic programming to store the number of distinct subsequences. We create a 2D array dp where dp[i][j] represents the number of distinct subsequences of the first i characters of S that equals the first j characters of T. We iterate over both strings and update dp[i][j] based on whether the current characters in S and T are equal or not.

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
        vector<vector<unsigned int>> dp(n + 1, vector<unsigned int>(m + 1, 0));
        
        // Initialize base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If current characters in S and T are equal, consider two cases:
                // 1. Include the current character in S in the subsequence
                // 2. Exclude the current character in S from the subsequence
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If current characters in S and T are not equal, exclude the current character in S from the subsequence
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
Input: S = "abc", T = "abc"
Output: 1
```

## Key Takeaways
- Use dynamic programming to store the number of distinct subsequences.
- Initialize base case where the target string is empty.
- Fill up the dp array by considering two cases: including or excluding the current character in S from the subsequence.
# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ABC" is a subsequence of "AHBGDC" because H, B, and G are not used in "ABC". The problem can be solved using dynamic programming. The constraints are 1 <= S.length, T.length <= 10^5 and S and T consist of lowercase English letters.

## Approach
The algorithm uses a 2D DP table where dp[i][j] represents the number of distinct subsequences of S[0..i-1] that equals T[0..j-1]. The base case is when T is empty, in which case there is only one distinct subsequence, the empty string. The recurrence relation is based on whether the current character in S matches the current character in T.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<vector<unsigned long long>> dp(m + 1, vector<unsigned long long>(n + 1, 0));
        
        // Base case: one way to get an empty string
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current characters match, consider two cases:
                // 1. Use the current character in S to match the current character in T
                // 2. Do not use the current character in S
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the current characters do not match, do not use the current character in S
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Input: s = "subscription", t = "subscription"
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The 2D DP table is used to store the number of distinct subsequences of S that equals T.
- The base case and recurrence relation are crucial in solving the problem using dynamic programming.
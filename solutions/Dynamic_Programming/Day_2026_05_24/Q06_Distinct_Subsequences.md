# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not. The length of both S and T will not exceed 100.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of the first i characters of S that equals the first j characters of T. We can fill this array in a bottom-up manner by considering two cases: either the current character in S is equal to the current character in T or not.

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
        
        // Initialize the base case where T is empty
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters in S and T are equal, consider two cases:
                // 1. The current character in S is included in the subsequence.
                // 2. The current character in S is not included in the subsequence.
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the current characters in S and T are not equal, the current character in S cannot be included in the subsequence.
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
Input: S = "abcd", T = "abcd"
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*m) where n and m are the lengths of the strings S and T respectively.
- The space complexity is also O(n*m) to store the 2D array.
- The base case is when T is empty, in which case there is only one subsequence (the empty string).
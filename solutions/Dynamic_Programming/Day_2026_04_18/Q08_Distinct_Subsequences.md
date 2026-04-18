# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The problem has the following constraints: 1 <= S.length, T.length <= 10^5, and S and T consist only of lowercase English letters.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T. We fill up this array in a bottom-up manner. If the current characters in S and T are equal, we add the number of subsequences without the current character in S to the number of subsequences without the current characters in both S and T.

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
        
        // Initialize base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
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
- The dynamic programming approach is used to solve the problem efficiently by avoiding redundant calculations.
- The 2D array dp is used to store the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T.
- The base case is initialized with dp[i][0] = 1, which means there is only one way to form an empty string from any string S.
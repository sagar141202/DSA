# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ACE" is a subsequence of "ABCDE". The problem has the following constraints: 1 <= S.length, T.length <= 10^5, and S and T consist of lowercase English letters.

## Approach
We can solve this problem using dynamic programming, where we build a 2D table to store the number of distinct subsequences of S that equals T up to a certain position. The table is filled in a bottom-up manner, and the final result is stored in the last cell of the table. We use the previously computed values to calculate the number of distinct subsequences.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<vector<unsigned long long>> dp(m + 1, vector<unsigned long long>(n + 1, 0));
        
        // Initialize base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If current characters match, consider two cases: include or exclude the current character
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If current characters do not match, exclude the current character
                else {
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
Input: S = "rabbbit", T = "rabbit"
Output: 3
Input: S = "abc", T = "abc"
Output: 1
```

## Key Takeaways
- Use dynamic programming to build a 2D table and store the number of distinct subsequences of S that equals T up to a certain position.
- Initialize the base case where the number of distinct subsequences is 1 when T is an empty string.
- Fill the table in a bottom-up manner, considering two cases when the current characters match: include or exclude the current character.
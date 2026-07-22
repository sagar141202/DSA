# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ACE" is a subsequence of "ABCDE". The problem has the following constraints: 1 <= length of S, T <= 100. Examples: S = "rabbbit", T = "rabbit", output = 3; S = "abcd", T = "abc", output = 1.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of S[0...i] that equals T[0...j]. We fill up this array in a bottom-up manner. If the current character in S matches the current character in T, we have two options: either include the current character in the subsequence or not.

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
        int n = s.size();
        int m = t.size();
        vector<vector<unsigned long long>> dp(n + 1, vector<unsigned long long>(m + 1, 0));
        
        // base case: there is one way to get an empty string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) {
                    // if the current character matches, we have two options: include or exclude
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // if the current character does not match, we cannot include it
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
Input: S = "abcd", T = "abc"
Output: 1
```

## Key Takeaways
- Use a 2D array to store the number of distinct subsequences.
- Fill up the array in a bottom-up manner.
- If the current character in S matches the current character in T, we have two options: include or exclude the current character.
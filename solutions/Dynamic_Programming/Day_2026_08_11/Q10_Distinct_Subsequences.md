# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The problem constraints are 1 <= S.length, T.length <= 10^5, and the strings consist only of lowercase English letters.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell represents the number of distinct subsequences of S up to that point that are equal to T up to that point. We iterate over both strings and update the array accordingly. The final answer will be stored in the last cell of the array.

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
        int n = s.length(), m = t.length();
        // Create a 2D array to store the number of distinct subsequences
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
        
        // Initialize the base case where T is an empty string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        // Fill up the dp array
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters in S and T are the same, we have two options:
                // 1. Use the current character in S to match the current character in T
                // 2. Do not use the current character in S
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters in S and T are different, we cannot use the current character in S
                else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        // The final answer is stored in the last cell of the dp array
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
- Dynamic programming is used to solve this problem by breaking it down into smaller subproblems and storing the results in a 2D array.
- The time complexity is O(n*m) where n and m are the lengths of the strings S and T respectively.
- The space complexity is also O(n*m) due to the 2D array used to store the number of distinct subsequences.
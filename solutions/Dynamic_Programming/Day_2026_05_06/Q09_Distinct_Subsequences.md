# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer is guaranteed to fit within an int. Constraints: 1 <= S.length, T.length <= 10^5, S and T consist of lowercase English letters.

## Approach
This problem can be solved using dynamic programming, where we build a 2D table to store the number of distinct subsequences. We fill the table by iterating over the strings S and T, and for each character, we check if it matches the current character in T. The algorithm uses the previously computed values to calculate the number of distinct subsequences.

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
        vector<vector<unsigned int>> dp(n + 1, vector<unsigned int>(m + 1, 0));
        
        // Initialize the base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters match, we have two options: include or exclude the current character
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters do not match, we cannot include the current character
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
Input: s = "rabbbit", t = "rabbit"
Output: 3
Input: s = "subscription", t = "subscription"
Output: 1
```

## Key Takeaways
- We use a 2D table to store the number of distinct subsequences, where dp[i][j] represents the number of distinct subsequences of the first i characters of S that equals the first j characters of T.
- We fill the table by iterating over the strings S and T, and for each character, we check if it matches the current character in T.
- The final answer is stored in dp[n][m], where n and m are the lengths of S and T, respectively.
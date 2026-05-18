# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases will be generated such that the answer will always be less than or equal to 2^31 - 1. Constraints: 1 <= S.length, T.length <= 100.

## Approach
The problem can be solved by using dynamic programming, where we create a 2D array to store the number of distinct subsequences of S that equals T up to a certain index. We iterate through S and T, and for each character, we check if it matches the current character in T. If it does, we update the count of distinct subsequences.

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
        int m = s.size(), n = t.size();
        vector<vector<unsigned int>> dp(m + 1, vector<unsigned int>(n + 1, 0));
        
        // Initialize base case where T is empty
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If current characters match, update count
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If characters don't match, no new subsequences are formed
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
Input: S = "subscription", T = "subscription"
Output: 1
```

## Key Takeaways
- Use dynamic programming to store the count of distinct subsequences up to a certain index.
- Initialize a base case where T is empty, and update the count based on whether the current characters match.
- The final answer is stored in the last cell of the 2D array.
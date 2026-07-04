# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The length of S is less than or equal to 100, and the length of T is less than or equal to 100.

## Approach
We can solve this problem using dynamic programming by creating a 2D array to store the number of distinct subsequences. The algorithm iterates over the strings S and T, and for each character, it checks if the current character in S is equal to the current character in T. If they are equal, it adds the number of distinct subsequences without the current character in S to the current number of distinct subsequences.

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
        
        // Initialize the base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) {
                    // If the current characters in S and T are equal, add the number of distinct subsequences without the current character in S
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the current characters in S and T are not equal, the number of distinct subsequences is the same as without the current character in S
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The time complexity of this solution is O(n*m), where n and m are the lengths of the strings S and T, respectively.
- The space complexity of this solution is O(n*m), which is used to store the 2D array dp.
# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer will be in the range of integer.

## Approach
We will use dynamic programming to solve this problem by maintaining a 2D array where each cell represents the number of distinct subsequences of the substring of S up to that point that are equal to the substring of T up to that point. The final result will be stored in the last cell of the array.

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
        
        // Create a 2D array to store the number of distinct subsequences
        vector<vector<unsigned long long>> dp(n + 1, vector<unsigned long long>(m + 1, 0));
        
        // Initialize the first row and column of the array
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        // Fill the array using dynamic programming
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        // The final result is stored in the last cell of the array
        return dp[n][m];
    }
};
```

## Test Cases
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a 2D array to store the number of distinct subsequences.
- The time complexity of the solution is O(n*m) where n and m are the lengths of the strings S and T respectively.
- The space complexity of the solution is O(n*m) which is used to store the 2D array.
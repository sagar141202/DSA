# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer is guaranteed to fit in a 32-bit integer. For example, given S = "rabbbit" and T = "rabbit", the answer is 3, because there are three different subsequences of S that equal T: "r-a-b-b-i-t", "r-a--b-b-i-t", and "r-a-b--b-i-t".

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of S[0..i] that equals T[0..j]. We fill up this array by iterating over the strings S and T. If the current characters in S and T match, we have two options: either include the current character in the subsequence or not.

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
        int m = s.size();
        int n = t.size();
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));
        
        // Initialize base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If characters match, consider both options: include or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If characters do not match, do not include the current character
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
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize base cases carefully to avoid errors.
- Consider all possible options when making a decision in the dynamic programming approach.
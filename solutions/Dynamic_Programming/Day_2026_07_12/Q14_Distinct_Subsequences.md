# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer is guaranteed to fit in a 32-bit integer. For example, given S = "rabbbit" and T = "rabbit", there are 3 different ways to get T from S: remove 'r', remove 'b', or remove both 'b's. The constraints are 1 <= S.length, T.length <= 1000.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array to store the number of distinct subsequences. We iterate over both strings and update the array based on whether the current characters match or not. This approach ensures that we consider all possible subsequences and avoid overcounting.

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
        
        // Initialize the base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current characters match, consider two cases: include the current character or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the characters do not match, do not include the current character
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
Input: S = "bag", T = "bag"
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows us to efficiently count the number of distinct subsequences by avoiding redundant computations.
- The 2D array dp is used to store the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T.
- The base case is initialized such that there is only one way to get an empty string from any string, which is to remove all characters.
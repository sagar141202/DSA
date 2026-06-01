# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases will be such that the answer will always be less than or equal to 2^31 - 1. Constraints: 1 <= S.length, T.length <= 10^5, S and T consist of lowercase English letters.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell represents the number of distinct subsequences of the substring of S and T. We iterate over the strings S and T, and for each character, we update the count of distinct subsequences. The final result will be stored in the last cell of the array.

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
        int n = s.length();
        int m = t.length();
        
        // Create a 2D array to store the number of distinct subsequences
        vector<vector<unsigned int>> dp(n + 1, vector<unsigned int>(m + 1, 0));
        
        // Initialize the base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        // Fill the dp array
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters in S and T are equal, consider two cases:
                // 1. The current character in S is included in the subsequence
                // 2. The current character in S is not included in the subsequence
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters in S and T are not equal, the current character in S cannot be included in the subsequence
                else {
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
Input: S = "rabbbit", T = "rabbit"
Output: 3
Input: S = "abc", T = "abc"
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a 2D array to store the number of distinct subsequences.
- The time complexity of the solution is O(n*m), where n and m are the lengths of the strings S and T, respectively.
- The space complexity of the solution is also O(n*m), which is used to store the dp array.
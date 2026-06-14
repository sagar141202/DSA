# Distinct Subsequences
## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer will be in the range of int.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell represents the number of distinct subsequences of the substring S[0..i] that equals the substring T[0..j]. We fill up this array in a bottom-up manner. If the current character in S matches the current character in T, we have two options: either include the current character in the subsequence or not.

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
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
        
        // Initialize the base case where T is an empty string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current character in S matches the current character in T,
                // we have two options: either include the current character in the subsequence or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the current character in S does not match the current character in T,
                    // we cannot include the current character in the subsequence
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
Input: S = "hello", T = "hello"
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*m) and a space complexity of O(n*m).
- The dynamic programming array is filled up in a bottom-up manner, where each cell represents the number of distinct subsequences of the substring S[0..i] that equals the substring T[0..j].
- The base case is when T is an empty string, in which case there is only one possible subsequence (an empty string).
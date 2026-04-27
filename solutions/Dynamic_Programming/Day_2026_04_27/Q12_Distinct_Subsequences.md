# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The length of S is at most 1000, and the length of T is at most 1000. For example, if S = "rabbbit" and T = "rabbit", then the number of distinct subsequences of S that are equal to T is 3.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of distinct subsequences of S that are equal to the first i characters of T. We iterate over S and T, and for each character, we update the table based on whether the current characters in S and T are equal or not. The final result is stored in the last cell of the table.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int numDistinct(string S, string T) {
    int n = S.size();
    int m = T.size();
    vector<vector<unsigned long long>> dp(n + 1, vector<unsigned long long>(m + 1, 0));
    
    // Initialize the base case
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 1;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // If the current characters in S and T are equal, 
            // we have two options: include the current character in S or not
            if (S[i - 1] == T[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            } 
            // If the current characters in S and T are not equal, 
            // we cannot include the current character in S
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    return dp[n][m];
}

int main() {
    string S = "rabbbit";
    string T = "rabbit";
    cout << numDistinct(S, T) << endl;
    return 0;
}
```

## Test Cases
```
Input: S = "rabbbit", T = "rabbit"
Output: 3
Input: S = "abc", T = "abc"
Output: 1
Input: S = "abc", T = "def"
Output: 0
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The 2D table is used to store the number of distinct subsequences of S that are equal to the first i characters of T.
- The final result is stored in the last cell of the table.
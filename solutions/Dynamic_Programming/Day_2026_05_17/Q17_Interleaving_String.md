# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in individual strings is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s3` should be equal to the sum of lengths of `s1` and `s2`. For example, if `s1 = "aabcc"`, `s2 = "dbbca"`, and `s3 = "aadbbcbcac"`, then `s3` is an interleaving of `s1` and `s2`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the interleaving status of substrings of `s1` and `s2`. We can fill the table in a bottom-up manner by checking if the current characters in `s1` and `s2` match the current character in `s3`. The algorithm checks for matches and updates the table accordingly.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isInterleave(string s1, string s2, string s3) {
    int m = s1.size(), n = s2.size();
    if (m + n != s3.size()) return false;
    
    // Create a 2D table to store the interleaving status
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    
    // Initialize the base cases
    dp[0][0] = true;
    for (int i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
    }
    for (int j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
        }
    }
    
    return dp[m][n];
}

int main() {
    string s1 = "aabcc";
    string s2 = "dbbca";
    string s3 = "aadbbcbcac";
    cout << boolalpha << isInterleave(s1, s2, s3) << endl;
    return 0;
}
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Key Takeaways
- The dynamic programming approach helps in solving the problem efficiently by avoiding redundant computations.
- The 2D table `dp` is used to store the interleaving status of substrings of `s1` and `s2`.
- The base cases are initialized carefully to ensure correct results.
# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "AGGTAB" and "GXTXAYB", the longest common subsequence is "GTAB". The sequences can contain any characters and have a maximum length of 1000.

## Approach
The problem can be solved using Dynamic Programming by creating a 2D table to store the lengths of common subsequences. The table is filled in a bottom-up manner, and the final answer is stored in the last cell of the table. The algorithm iterates over the characters in both sequences, updating the table based on whether the current characters match or not.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    
    // Create a 2D table to store the lengths of common subsequences
    int dp[m + 1][n + 1];
    
    // Initialize the first row and column to 0
    for (int i = 0; i <= m; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = 0;
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                // If the current characters match, update the table accordingly
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // If the current characters do not match, update the table accordingly
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The final answer is stored in the last cell of the table
    return dp[m][n];
}

int main() {
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    cout << "Length of longest common subsequence: " << longestCommonSubsequence(s1, s2);
    return 0;
}
```

## Test Cases
```
Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
Input: s1 = "ABCBDAB", s2 = "BDCABA"
Output: 4
```

## Key Takeaways
- The Dynamic Programming approach is used to solve the Longest Common Subsequence problem.
- A 2D table is created to store the lengths of common subsequences, and the table is filled in a bottom-up manner.
- The final answer is stored in the last cell of the table, which represents the length of the longest common subsequence.
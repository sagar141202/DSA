# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "AGGTAB" and "GXTXAYB", the longest common subsequence is "GTAB". The sequences can be of any length, and the characters can be any alphanumeric characters. The goal is to find the length of the longest common subsequence.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the lengths of common subsequences. We fill the table in a bottom-up manner, considering all possible subsequences. The final answer will be stored in the bottom-right corner of the table. We use the previously computed values to avoid redundant computations.

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
    // Create a table to store lengths of longest common subsequences of substrings.
    int dp[m + 1][n + 1];
    // Initialize the table.
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            // If either of the strings is empty, the longest common subsequence is 0.
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            }
            // If the current characters match, consider it as part of the subsequence.
            else if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            }
            // If the characters do not match, consider the maximum length without the current character.
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    // The length of the longest common subsequence is stored in the bottom-right corner of the table.
    return dp[m][n];
}

int main() {
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    cout << "Length of LCS: " << longestCommonSubsequence(s1, s2) << endl;
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
- Dynamic programming is used to solve the problem efficiently by avoiding redundant computations.
- The problem can be broken down into smaller sub-problems, and the solutions to these sub-problems are used to construct the solution to the original problem.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input sequences.
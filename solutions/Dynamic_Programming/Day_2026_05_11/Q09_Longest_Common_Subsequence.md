# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and the length of the sequences can be up to 1000.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the lengths of the longest common subsequences of subproblems. We fill the table in a bottom-up manner, considering all possible cases of matching and non-matching characters.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.size();
    int n = s2.size();
    // Create a 2D table to store the lengths of the longest common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, consider it as part of the subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // If the current characters do not match, consider the maximum length without it
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    // The length of the longest common subsequence is stored in the last cell of the table
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    cout << "Length of the longest common subsequence: " << longestCommonSubsequence(s1, s2);
    return 0;
}
```

## Test Cases
```
Input: s1 = "ABCBDAB", s2 = "BDCABA"
Output: 4
Input: s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Output: 26
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems with overlapping subproblems.
- The 2D table helps to store and reuse the solutions of subproblems, reducing the time complexity.
- The longest common subsequence problem has various applications in data compression, bioinformatics, and text processing.
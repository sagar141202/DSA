# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and the length of the sequences can be up to 1000.

## Approach
The Longest Common Subsequence problem can be solved using Dynamic Programming by creating a 2D table to store the lengths of the longest common subsequences of substrings. The table is filled in a bottom-up manner by comparing characters from both sequences. If the characters match, the length of the longest common subsequence is incremented by 1. If the characters do not match, the maximum length of the longest common subsequences of the substrings without the current characters is taken.

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
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the characters match, increment the length of the longest common subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // If the characters do not match, take the maximum length of the longest common subsequences
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The length of the longest common subsequence is stored in the bottom-right corner of the table
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    cout << "Length of Longest Common Subsequence: " << longestCommonSubsequence(s1, s2) << endl;
    return 0;
}
```

## Test Cases
```
Input: s1 = "ABCBDAB", s2 = "BDCABA"
Output: 4
Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
```

## Key Takeaways
- The Longest Common Subsequence problem can be solved using Dynamic Programming with a time complexity of O(m*n) and a space complexity of O(m*n).
- The problem can be generalized to find the longest common subsequence of more than two sequences.
- The solution can be modified to print the longest common subsequence itself instead of just its length.
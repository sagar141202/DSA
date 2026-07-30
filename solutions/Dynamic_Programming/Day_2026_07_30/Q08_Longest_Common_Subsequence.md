# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "abc" is a subsequence of "ahbgdc" because 'a', 'b', and 'c' appear in the same order in both sequences. The problem is to find the length of the longest common subsequence between two sequences, and optionally to reconstruct the subsequence itself. The sequences can be strings, arrays of integers, or any other type of sequence. The problem has a constraint that the sequences are not empty and contain only characters or integers.

## Approach
The problem can be solved using Dynamic Programming by building a 2D table where each cell represents the length of the longest common subsequence up to that point in the sequences. The table is filled in a bottom-up manner, and the final answer is stored in the last cell of the table. The algorithm iterates over both sequences, comparing characters and updating the table accordingly.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to find the length of the longest common subsequence
int longestCommonSubsequence(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    
    // Create a 2D table to store the lengths of common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, increase the length of the subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // Otherwise, take the maximum length from the previous cells
            else {
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
    cout << "Length of LCS: " << longestCommonSubsequence(s1, s2);
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
- The Longest Common Subsequence problem can be solved using Dynamic Programming with a time complexity of O(m*n), where m and n are the lengths of the input sequences.
- The solution involves building a 2D table to store the lengths of common subsequences and filling it in a bottom-up manner.
- The final answer is stored in the last cell of the table, which represents the length of the longest common subsequence between the two input sequences.
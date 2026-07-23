# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any alphanumeric characters and can have a maximum length of 1000.

## Approach
This problem can be solved using dynamic programming by creating a 2D table to store the lengths of the longest common subsequences. The algorithm iterates over the two sequences, comparing characters and updating the table accordingly. The final result is stored in the bottom-right corner of the table.

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
    // Create a 2D table to store the lengths of the longest common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Iterate over the two sequences
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, update the table accordingly
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // Otherwise, take the maximum of the two possible subsequences
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The final result is stored in the bottom-right corner of the table
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
Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
```

## Key Takeaways
- The longest common subsequence problem can be solved using dynamic programming with a time complexity of O(m*n) and a space complexity of O(m*n).
- The algorithm creates a 2D table to store the lengths of the longest common subsequences and iterates over the two sequences, comparing characters and updating the table accordingly.
- The final result is stored in the bottom-right corner of the table, which represents the length of the longest common subsequence.
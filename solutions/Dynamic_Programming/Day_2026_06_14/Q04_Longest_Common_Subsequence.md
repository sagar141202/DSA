# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters, and the length of the sequences can be up to 1000 characters.

## Approach
The Longest Common Subsequence problem can be solved using Dynamic Programming by creating a 2D table to store the lengths of common subsequences. The algorithm iterates over the characters in both sequences, updating the table based on whether the current characters match or not. This approach allows for efficient computation of the longest common subsequence by avoiding redundant calculations.

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
    // Create a 2D table to store the lengths of common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    // Iterate over the characters in both sequences
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, update the table accordingly
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // Otherwise, take the maximum length from the previous cells
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The length of the longest common subsequence is stored in the bottom-right cell
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    cout << "Length of the longest common subsequence: " << longestCommonSubsequence(s1, s2) << endl;
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
- The Dynamic Programming approach is suitable for solving the Longest Common Subsequence problem efficiently.
- The 2D table helps avoid redundant calculations by storing the lengths of common subsequences.
- The algorithm has a time complexity of O(m*n) and a space complexity of O(m*n), where m and n are the lengths of the input sequences.
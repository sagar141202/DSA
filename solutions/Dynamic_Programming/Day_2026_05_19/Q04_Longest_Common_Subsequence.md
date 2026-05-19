# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and the length of the sequences can be up to 1000 characters.

## Approach
The problem can be solved using dynamic programming by storing the lengths of the longest common subsequences of subproblems in a 2D array. The final answer will be stored in the bottom-right corner of the array. We fill the array in a bottom-up manner by comparing characters from both sequences.

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
    // Create a 2D array to store lengths of longest common subsequences
    int dp[m + 1][n + 1];
    // Initialize the first row and column to 0
    for (int i = 0; i <= m; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = 0;
    }
    // Fill the array in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                // If the current characters match, increase the length by 1
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // If the current characters do not match, take the maximum from the left or top cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    // The final answer is stored in the bottom-right corner of the array
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    int length = longestCommonSubsequence(s1, s2);
    cout << "Length of the longest common subsequence: " << length << endl;
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
- The dynamic programming approach is used to store and reuse the results of subproblems, reducing the time complexity from exponential to polynomial.
- The 2D array is used to store the lengths of the longest common subsequences of subproblems, and the final answer is stored in the bottom-right corner of the array.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input sequences.
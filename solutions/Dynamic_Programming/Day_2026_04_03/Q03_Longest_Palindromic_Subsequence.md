# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that is the same when reversed. For example, "aba" and "abcba" are palindromic subsequences, while "abcd" is not. The input string will have a length between 1 and 1000 characters. The string will only contain lowercase letters.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the lengths of the longest palindromic subsequences for all substrings. We start by filling the table for substrings of length 1 and then move to longer substrings. The length of the longest palindromic subsequence for a substring can be determined by checking if the first and last characters are the same.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestPalindromicSubsequence(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    // Fill the table for substrings of length 1
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Fill the table for substrings of length 2
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = 2;
        } else {
            dp[i][i + 1] = 1;
        }
    }

    // Fill the table for longer substrings
    for (int length = 3; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[0][n - 1];
}

int main() {
    string s = "abcba";
    cout << longestPalindromicSubsequence(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: "abcba"
Output: 5
Input: "abcd"
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems and the solutions to these subproblems can be stored in a table for later use.
- The time complexity of the solution is O(n^2), where n is the length of the input string.
# Longest Palindromic Subsequence

## Problem Statement
Given a sequence of characters, find the length of the longest subsequence that is a palindrome. A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. The input string will have a length between 1 and 1000 characters. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the length of the longest palindromic subsequence in the substring from the row index to the column index. It iterates over the string, filling the table in a bottom-up manner. The final result is stored in the top-right cell of the table.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestPalindromicSubsequence(string s) {
    int n = s.length();
    // Create a 2D table to store the lengths of palindromic subsequences
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1; // A single character is a palindrome of length 1
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                // If the first and last characters match, consider the subsequence in between
                if (length == 2) {
                    dp[i][j] = 2;
                } else {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                }
            } else {
                // If the first and last characters don't match, consider the maximum of the two subsequences
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The final result is stored in the top-right cell of the table
    return dp[0][n - 1];
}

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;
    cout << "Length of the longest palindromic subsequence: " << longestPalindromicSubsequence(s);
    return 0;
}
```

## Test Cases
```
Input: banana
Output: 3
Input: abc
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the longest palindromic subsequence by breaking down the problem into smaller subproblems and storing their solutions.
- The 2D table helps to avoid redundant computations and reduce the time complexity to O(n^2).
- The final result is obtained by considering the maximum length of palindromic subsequences in the input string.
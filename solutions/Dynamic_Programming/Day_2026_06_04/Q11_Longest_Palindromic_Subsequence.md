# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest subsequence that is a palindrome. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "banana" has a longest palindromic subsequence of "anana". The string can contain any ASCII characters and has a maximum length of 1000 characters.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the length of the longest palindromic subsequence within a substring. The table is filled in a bottom-up manner, starting from substrings of length 1 and 2, and then expanding to longer substrings. The final result is stored in the top-right cell of the table.

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
    vector<vector<int>> table(n, vector<int>(n, 0));
    
    // Fill the table for substrings of length 1
    for (int i = 0; i < n; i++) {
        table[i][i] = 1;
    }
    
    // Fill the table for substrings of length 2
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            table[i][i + 1] = 2;
        } else {
            table[i][i + 1] = 1;
        }
    }
    
    // Fill the table for longer substrings
    for (int length = 3; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                table[i][j] = table[i + 1][j - 1] + 2;
            } else {
                table[i][j] = max(table[i + 1][j], table[i][j - 1]);
            }
        }
    }
    
    // The final result is stored in the top-right cell of the table
    return table[0][n - 1];
}

int main() {
    string s = "banana";
    cout << "Length of longest palindromic subsequence: " << longestPalindromicSubsequence(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: "banana"
Output: 3
Input: "abc"
Output: 1
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems, like the longest palindromic subsequence problem.
- The 2D table is used to store the lengths of palindromic subsequences for different substrings, which helps to avoid redundant calculations.
- The final result is obtained by filling the table in a bottom-up manner and then returning the value stored in the top-right cell.
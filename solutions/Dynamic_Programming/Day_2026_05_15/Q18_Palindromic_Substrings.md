# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings. A palindromic substring is a substring that reads the same backward as forward. For example, "aba" is a palindrome, but "abc" is not. The string will contain only lowercase English letters and will have a length between 1 and 1000 characters.

## Approach
The approach is to use dynamic programming to build a 2D table where each cell represents whether a substring is a palindrome or not. We start by filling the diagonal of the table, as single characters are always palindromes, and then fill the rest of the table based on the characters and previously computed values.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int count = 0;
        
        // Fill the diagonal of the table
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // Fill the table for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // Fill the table for substrings of length 3 and more
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: "abc"
Output: 3
Input: "aaa"
Output: 6
```

## Key Takeaways
- The dynamic programming approach allows us to efficiently compute the number of palindromic substrings by avoiding redundant computations.
- The use of a 2D table enables us to keep track of the palindromic status of each substring.
- The solution has a time complexity of O(n^2) and a space complexity of O(n^2), where n is the length of the input string.
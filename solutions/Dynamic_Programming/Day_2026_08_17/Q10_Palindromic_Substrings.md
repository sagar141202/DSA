# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backward as forward. For example, "aba" is a palindromic substring, but "abc" is not. The input string only contains lowercase English letters. The length of the input string is at most 1000 characters.

## Approach
The approach to solve this problem is to use dynamic programming to store whether each substring is palindromic or not. We will iterate over the string and check for palindromic substrings of length 1, 2, and greater than 2. We will use a 2D array to store the dynamic programming state.

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
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // Check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // Check for lengths greater than 2
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
- We use a 2D array `dp` to store whether each substring is palindromic or not.
- We start by marking all substrings with one character as palindromes.
- We then check for substrings of length 2 and mark them as palindromes if the characters are the same.
- Finally, we check for lengths greater than 2 by comparing the first and last characters and checking if the substring in between is a palindrome.
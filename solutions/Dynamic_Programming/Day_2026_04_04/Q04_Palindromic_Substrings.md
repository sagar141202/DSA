# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", the palindromic substrings are "a", "b", and "c". In the string "aaa", the palindromic substrings are "a", "aa", "aaa". The input string will only contain lowercase English letters. The length of the input string will not exceed 1000 characters.

## Approach
The approach to solve this problem is to use dynamic programming to store whether each substring is palindromic or not. We will iterate over all possible substrings, check if they are palindromic, and count them. The key intuition is to expand around the center of the palindrome.

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
        
        // all substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // check for lengths greater than 2
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The key to solving this problem is to expand around the center of the palindrome.
- The time complexity of this solution is O(n^2) because we are checking all possible substrings of the input string.
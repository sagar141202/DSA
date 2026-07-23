# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", the palindromic substrings are "a", "b", and "c". In the string "aaa", the palindromic substrings are "a", "aa", "aaa". The string will only contain lowercase English letters and the length of the string will be in the range [1, 1000].

## Approach
The approach to solve this problem involves using dynamic programming to store whether each substring is a palindrome or not. We will create a 2D table where each cell [i][j] represents whether the substring from index i to j is a palindrome. We will then count the number of palindromic substrings by iterating over this table.

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
        int n = s.size();
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
- We use a dynamic programming approach to store whether each substring is a palindrome or not.
- The time complexity is O(n^2) because we are iterating over the string to fill the dp table.
- The space complexity is also O(n^2) because we are using a 2D table of size n x n to store the dp values.
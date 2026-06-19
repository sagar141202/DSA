# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", the palindromic substrings are "a", "b", and "c". In the string "aaa", the palindromic substrings are "a", "aa", "aaa". The input string will contain only lowercase English letters and will have a length between 1 and 1000.

## Approach
We can solve this problem using dynamic programming by maintaining a 2D table where each cell represents whether the substring from the corresponding start index to the end index is a palindrome. We then count the number of palindromic substrings by iterating over this table.

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
- We used a bottom-up dynamic programming approach to solve this problem, starting with substrings of length 1 and then moving to longer lengths.
- The time complexity of this solution is O(n^2), where n is the length of the input string, because we are using two nested loops to fill the dp table.
- The space complexity is also O(n^2) because we are using a 2D table of size n x n to store the dp values.
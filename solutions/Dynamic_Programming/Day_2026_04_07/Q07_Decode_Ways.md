# Decode Ways

## Problem Statement
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26. Given a non-empty string containing only digits, determine the number of ways to decode it. The encoding is done such that each digit or pair of digits can be mapped to a letter. For example, "12" can be decoded as "AB" (1 -> A, 2 -> B) or "L" (12 -> L). The string is valid if it does not contain any leading zeros (except for the number 0 itself) and each number or pair of numbers is within the range [1, 26]. For instance, "027" is not valid because it contains a leading zero for the number 27.

## Approach
The problem can be solved using dynamic programming by maintaining an array where each element represents the number of ways to decode the string up to that point. We consider each digit or pair of digits and update the array accordingly. The final result will be the last element in the array.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        if (n == 0 || s[0] == '0') return 0;
        
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            // Check if the current digit can be decoded separately
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            
            // Check if the current and previous digits can be decoded together
            int num = stoi(s.substr(i - 2, 2));
            if (num >= 10 && num <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        
        return dp[n];
    }
};
```

## Test Cases
```
Input: "12"
Output: 2
Input: "226"
Output: 3
Input: "0"
Output: 0
```

## Key Takeaways
- The dynamic programming approach is suitable for problems that have overlapping subproblems and optimal substructure.
- The base cases are crucial in dynamic programming, and they should be handled carefully to avoid incorrect results.
- The time and space complexity of the solution should be analyzed to ensure it can handle large inputs efficiently.
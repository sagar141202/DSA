# Generate Parentheses

## Problem Statement
Given an integer n, generate all possible combinations of well-formed parentheses. A well-formed parenthesis is one in which every open parenthesis can be matched with a corresponding closing parenthesis. For example, "(())" and "(()())" are well-formed, while ")(" and "(()" are not. The input integer n represents the number of pairs of parentheses, and the output should be a list of all possible well-formed combinations of n pairs of parentheses.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of well-formed parentheses. It starts with an empty string and adds open and close parentheses recursively, ensuring that the number of open parentheses never exceeds n and the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the Catalan number sequence
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }
    
    void backtrack(vector<string>& result, string s, int open, int close, int n) {
        // base case: when the length of the string is equal to 2n
        if (s.length() == 2 * n) {
            result.push_back(s);
            return;
        }
        
        // add open parenthesis if the number of open parentheses is less than n
        if (open < n) {
            backtrack(result, s + "(", open + 1, close, n);
        }
        
        // add close parenthesis if the number of close parentheses is less than the number of open parentheses
        if (close < open) {
            backtrack(result, s + ")", open, close + 1, n);
        }
    }
};
```

## Test Cases
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible combinations of well-formed parentheses.
- The base case for the recursion is when the length of the string is equal to 2n, at which point the string is added to the result.
- The number of open parentheses should never exceed n, and the number of close parentheses should never exceed the number of open parentheses.
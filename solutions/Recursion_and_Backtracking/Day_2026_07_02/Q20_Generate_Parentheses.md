# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The constraint is that the input `n` will be a positive integer.

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. We start with an empty string and add open and close parentheses recursively, ensuring that the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of ways to create well-formed parentheses
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursive call stack

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
    
    void backtrack(vector<string>& result, string current, int open, int close, int max) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }
        
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
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
- Recursion and backtracking can be used to solve problems that involve generating all possible combinations of a certain pattern, like well-formed parentheses.
- Ensuring the base case is correctly defined is crucial for recursion to terminate properly.
- Using a helper function like `backtrack` can simplify the code and make it easier to understand the recursive process.
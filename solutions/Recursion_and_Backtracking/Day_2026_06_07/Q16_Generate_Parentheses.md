# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The input `n` is a positive integer, and the output should be a list of all possible well-formed combinations of `n` pairs of parentheses.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. We will use a recursive function to add open and close parentheses to the current combination, ensuring that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of binary trees with n nodes, and by extension, the number of well-formed parentheses combinations.
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack.

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
        // Base case: if the length of the current combination is equal to 2n, add it to the result
        if (current.length() == 2 * max) {
            result.push_back(current);
            return;
        }
        
        // Add an open parenthesis if the number of open parentheses is less than n
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }
        
        // Add a close parenthesis if the number of close parentheses is less than the number of open parentheses
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
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- Ensure that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.
- The problem is related to Catalan numbers, which represent the number of binary trees with `n` nodes.
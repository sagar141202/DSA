# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of all possible combinations of `n` pairs of well-formed parentheses. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, and `()()()`.

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of parentheses. The algorithm will add an open parenthesis if the number of open parentheses is less than `n`, and add a close parenthesis if the number of close parentheses is less than the number of open parentheses. This ensures that the generated combinations are always well-formed.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of binary trees with n internal nodes, which is equivalent to the number of well-formed parentheses combinations.
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

    void backtrack(vector<string>& result, string current, int open, int close, int n) {
        // base case: if the length of the current combination is equal to 2n, add it to the result
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        // add an open parenthesis if the number of open parentheses is less than n
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
        // add a close parenthesis if the number of close parentheses is less than the number of open parentheses
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, n);
        }
    }
};
```

## Test Cases
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

## Key Takeaways
- The problem can be solved using recursion and backtracking by ensuring that the number of close parentheses never exceeds the number of open parentheses.
- The time complexity is related to Catalan numbers, which grow rapidly with the input size `n`.
- The space complexity includes both the space required for storing the result and the recursion stack.
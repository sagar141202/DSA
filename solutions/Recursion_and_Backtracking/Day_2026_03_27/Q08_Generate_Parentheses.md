# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of strings, where each string represents a well-formed combination of `n` pairs of parentheses. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, and `()()()`.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. The idea is to add an open parenthesis if the number of open parentheses is less than `n`, and add a close parenthesis if the number of close parentheses is less than the number of open parentheses. This ensures that every combination generated is well-formed.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers, which represent the number of well-formed combinations of `n` pairs of parentheses.
- Space: O(4^n / n^(3/2)) for storing the generated combinations, as well as the space required by the recursive call stack.

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

int main() {
    Solution solution;
    int n = 3;
    vector<string> result = solution.generateParenthesis(n);
    for (const auto& combination : result) {
        cout << combination << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Key Takeaways
- The use of recursion and backtracking allows for the efficient generation of all possible combinations of well-formed parentheses.
- The base case for the recursion is when the length of the current combination is equal to `2n`, at which point the combination is added to the result.
- The recursive calls are made by adding either an open or close parenthesis to the current combination, depending on the current state of the combination.
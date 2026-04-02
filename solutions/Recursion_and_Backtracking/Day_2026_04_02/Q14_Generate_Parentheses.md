# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The input `n` is a positive integer, and the output should be a list of all possible combinations of well-formed parentheses.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty string and add open and close parentheses recursively, ensuring that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of binary trees with n internal nodes, or the number of well-formed combinations of n pairs of parentheses.
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

int main() {
    Solution solution;
    vector<string> result = solution.generateParenthesis(3);
    for (const auto& str : result) {
        cout << str << endl;
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
- Use recursion and backtracking to generate all combinations of well-formed parentheses.
- Ensure the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.
- The time and space complexity are related to the Catalan numbers, which describe the number of well-formed combinations of `n` pairs of parentheses.
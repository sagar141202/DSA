# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parentheses combination is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`. The constraint is that the total number of open and close parentheses must be `2n`.

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. We start by adding an open parenthesis if the number of open parentheses is less than `n`, and then add a close parenthesis if the number of close parentheses is less than the number of open parentheses. This ensures that every combination is well-formed.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of well-formed parentheses combinations.
- Space: O(4^n / n^(3/2)) for storing the generated combinations.

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
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- Ensure that the number of close parentheses never exceeds the number of open parentheses to maintain well-formedness.
- The total number of combinations is given by the `n`-th Catalan number, which is `O(4^n / n^(3/2))`.
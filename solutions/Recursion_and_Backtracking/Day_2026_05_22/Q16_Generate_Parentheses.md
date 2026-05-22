# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` is a positive integer, and the output should be a list of all possible combinations of well-formed parentheses. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of well-formed parentheses. It starts by adding an open parenthesis and then recursively adds more parentheses. If the number of close parentheses exceeds the number of open parentheses, it backtracks and tries a different combination.

## Complexity
- Time: O(4^n / n^(3/2))
- Space: O(4^n / n^(3/2))

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
        // base case: if the length of the current combination is equal to 2n
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }

        // add an open parenthesis if the number of open parentheses is less than n
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }

        // add a close parenthesis if the number of close parentheses is less than the number of open parentheses
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
Input: n = 1
Output: ["()"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- Keep track of the number of open and close parentheses to ensure that the combination is well-formed.
- Use a base case to stop the recursion when the length of the current combination is equal to 2n.
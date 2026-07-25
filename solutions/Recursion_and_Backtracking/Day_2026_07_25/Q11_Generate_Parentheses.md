# Generate Parentheses

## Problem Statement
The problem asks to generate all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`. The input `n` is a positive integer, and the output should be a list of all possible combinations of well-formed parentheses.

## Approach
We will use a recursive approach with backtracking to generate all possible combinations of well-formed parentheses. The algorithm will add an open parenthesis if the number of open parentheses is less than `n`, and add a close parenthesis if the number of close parentheses is less than the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
- Space: O(4^n / n^(3/2)) for storing the result

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
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
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
- The problem can be solved using a recursive approach with backtracking.
- The base case for the recursion is when the length of the current combination is equal to `2 * n`.
- The algorithm uses two counters, `open` and `close`, to keep track of the number of open and close parentheses in the current combination.
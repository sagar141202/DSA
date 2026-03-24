# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of all possible combinations of well-formed parentheses. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
This problem can be solved using recursion and backtracking, where we build the combinations of parentheses by adding open and close parentheses one by one. We use a recursive function to generate all possible combinations, and we use backtracking to remove the last added parenthesis when it does not lead to a well-formed combination.

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
        // base case: if the length of the current combination is equal to 2*n, add it to the result
        if (current.length() == 2 * max) {
            result.push_back(current);
            return;
        }
        
        // add an open parenthesis if the number of open parentheses is less than max
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
- The base case for the recursion is when the length of the current combination is equal to 2*n.
- Use two counters, open and close, to keep track of the number of open and close parentheses in the current combination.
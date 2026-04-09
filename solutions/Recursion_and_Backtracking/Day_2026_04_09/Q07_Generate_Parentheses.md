# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parenthesis is one in which every open parenthesis can be matched with a corresponding close parenthesis. The constraints are: `1 <= n <= 20`. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
The problem can be solved using recursion and backtracking. The idea is to add an open parenthesis if the number of open parentheses is less than `n`, and add a close parenthesis if the number of close parentheses is less than the number of open parentheses. This ensures that the generated parentheses are always well-formed.

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
        // base case: if the length of the current string is equal to 2n
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
- The problem can be solved using recursion and backtracking.
- The base case for the recursion is when the length of the current string is equal to `2n`.
- The time and space complexity of the solution is due to the nature of Catalan numbers.
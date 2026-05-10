# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parentheses combination is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, given `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`. The input `n` will be in the range `[1, 8]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible combinations of parentheses by adding an open parenthesis when the number of open parentheses is less than `n`, and adding a close parenthesis when the number of close parentheses is less than the number of open parentheses. This ensures that the generated combinations are well-formed.

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
        // base case: when the length of the current combination is equal to 2n
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }

        // add an open parenthesis when the number of open parentheses is less than n
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }

        // add a close parenthesis when the number of close parentheses is less than the number of open parentheses
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
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- Ensure that the generated combinations are well-formed by adding an open parenthesis when the number of open parentheses is less than `n`, and adding a close parenthesis when the number of close parentheses is less than the number of open parentheses.
- The time and space complexity of the solution is due to the nature of Catalan numbers, which represent the number of well-formed parentheses combinations of length `2n`.
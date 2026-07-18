# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of all possible combinations of `n` pairs of well-formed parentheses. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The goal is to write a function that generates all such combinations.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty string and add open and close parentheses recursively, ensuring that the number of close parentheses never exceeds the number of open parentheses. This way, we can generate all possible combinations of well-formed parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of ways to create well-formed parentheses
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack

## C++ Solution
```cpp
#include <vector>
#include <string>
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

Input: n = 1
Output: ["()"]
```

## Key Takeaways
- Recursion and backtracking are powerful tools for solving combinatorial problems.
- Ensuring that the recursive calls have a clear base case and that the problem is divided into smaller sub-problems is crucial for an efficient solution.
- Understanding the constraints and how they limit the solution space can significantly reduce the complexity of the problem.
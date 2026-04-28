# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The input `n` will be a positive integer, and the output should be a list of all possible combinations of well-formed parentheses.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of parentheses. We start by adding an open parenthesis and then recursively add more parentheses. If the number of open parentheses is less than `n`, we can add another open parenthesis. If the number of close parentheses is less than the number of open parentheses, we can add a close parenthesis.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers, which represent the number of ways to create well-formed sequences of parentheses.
- Space: O(4^n / n^(3/2)) for storing the result.

## C++ Solution
```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> generateParenthesis(int n) {
        std::vector<std::string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }
    
    void backtrack(std::vector<std::string>& result, std::string current, int open, int close, int n) {
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
```

## Key Takeaways
- Recursion and backtracking are essential techniques for solving problems that involve generating all possible combinations of a certain structure.
- Understanding the constraints of the problem, such as the balance between open and close parentheses, is crucial for implementing an efficient solution.
- The time and space complexity of the solution are related to the number of possible combinations, which in this case is represented by Catalan numbers.
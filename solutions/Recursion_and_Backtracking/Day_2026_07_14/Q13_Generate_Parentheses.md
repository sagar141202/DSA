# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` is a positive integer, and the output should be a list of all possible well-formed combinations of `n` pairs of parentheses. For example, if `n = 3`, the output should include combinations like `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. The algorithm starts with an empty string and recursively adds open and close parentheses to form valid combinations.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of valid combinations for `n` pairs of parentheses.
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack.

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
    
    void backtrack(std::vector<std::string>& result, std::string current, int open, int close, int max) {
        if (current.size() == max * 2) {
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
- Recursion and backtracking are powerful tools for solving problems that involve generating combinations or permutations.
- Understanding the constraints and the requirements of the problem is crucial for devising an efficient solution.
- The use of recursive functions can simplify the code and make it easier to understand, but it may also increase the memory usage due to the recursion stack.
# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of strings, where each string represents a well-formed combination of `n` pairs of parentheses. For example, if `n = 3`, the output should include combinations like `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. The algorithm starts with an empty string and adds open and close parentheses recursively, ensuring that the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of binary trees with n internal nodes, or the number of well-formed sequences of n pairs of parentheses.
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack.

## C++ Solution
```cpp
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> generateParenthesis(int n) {
        std::vector<std::string> result;
        generate(result, "", 0, 0, n);
        return result;
    }
    
    void generate(std::vector<std::string>& result, std::string current, int open, int close, int max) {
        if (current.length() == max * 2) {
            result.push_back(current);
            return;
        }
        
        if (open < max) {
            generate(result, current + "(", open + 1, close, max);
        }
        
        if (close < open) {
            generate(result, current + ")", open, close + 1, max);
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
- The use of recursion and backtracking is essential for generating all possible combinations of well-formed parentheses.
- Ensuring that the number of close parentheses never exceeds the number of open parentheses is crucial for maintaining the well-formed property.
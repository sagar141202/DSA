# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parenthesis is one in which every open parenthesis can be matched with a corresponding closing parenthesis. For example, if `n = 3`, the output should include all possible combinations of 3 pairs of well-formed parentheses, such as `((()))`, `(()())`, `(())()`, `()(())`, and `()()()`. The input `n` will be a positive integer, and the output should be a list of strings, where each string represents a combination of `n` pairs of well-formed parentheses.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of well-formed parentheses. It maintains a balance between open and close parentheses to ensure well-formedness. The base case for recursion is when the length of the current combination equals `2n`, at which point the combination is added to the result list.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of ways to create well-formed parentheses
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack

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
        // Base case: if the length of the current combination equals 2n, add it to the result
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        // If the number of open parentheses is less than n, add an open parenthesis
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
        // If the number of close parentheses is less than the number of open parentheses, add a close parenthesis
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
- Recursion and backtracking can be used to generate all possible combinations of well-formed parentheses.
- Maintaining a balance between open and close parentheses is crucial for ensuring well-formedness.
- The time and space complexity are related to the number of ways to create well-formed parentheses, which is represented by Catalan numbers.
# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should be all possible combinations of 3 pairs of well-formed parentheses, such as `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The input `n` will be a positive integer, and the output should be a list of all possible combinations of well-formed parentheses.

## Approach
The solution utilizes backtracking to generate all possible combinations of parentheses. It starts with an empty string and adds open and close parentheses recursively, ensuring that the combination remains well-formed. The base case for the recursion is when the length of the current combination equals `2n`, at which point the combination is added to the result list.

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
        backtrack(result, "", 0, 0, n);
        return result;
    }
    
    void backtrack(std::vector<std::string>& result, std::string current, int open, int close, int n) {
        // Base case: if the length of the current combination equals 2n, add it to the result
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        // Add an open parenthesis if possible
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
        // Add a close parenthesis if there's a matching open parenthesis
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
- Ensuring that a combination remains well-formed is crucial, which is achieved by maintaining a balance between open and close parentheses.
- The time and space complexity are related to Catalan numbers, which is a characteristic of problems involving well-formed parentheses.
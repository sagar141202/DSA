# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parentheses sequence is one where every open parenthesis can be matched with a corresponding closed parenthesis. For example, given `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`. The input `n` will be a positive integer.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of well-formed parentheses. It maintains a balance between the number of open and closed parentheses to ensure that the generated sequences are well-formed. The base case is when the length of the current combination is equal to `2n`, at which point it is added to the result list.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
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
- The use of recursion and backtracking allows for the efficient generation of all possible combinations of well-formed parentheses.
- Maintaining a balance between the number of open and closed parentheses is crucial to ensure that the generated sequences are well-formed.
- The solution has a time and space complexity related to Catalan numbers, which describe the number of well-formed parentheses sequences of a given length.
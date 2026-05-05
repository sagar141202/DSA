# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number of pairs. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The input is an integer `n`, representing the number of pairs of parentheses, and the output should be a list of all possible well-formed combinations of `n` pairs of parentheses. For example, if `n = 3`, the output should include combinations like `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`.

## Approach
The solution utilizes recursion and backtracking to generate all possible combinations. It starts by adding an open parenthesis and then recursively adds more parentheses, ensuring that the number of close parentheses never exceeds the number of open ones. Once the combination is complete, it is added to the result list.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of combinations of well-formed parentheses for `n` pairs.
- Space: O(4^n / n^(3/2)) for storing the result, as in the worst case, we might have to store all combinations.

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
```

## Key Takeaways
- The problem can be solved using recursion and backtracking by ensuring that the number of close parentheses never exceeds the number of open ones.
- The time and space complexity are related to the Catalan numbers, which grow rapidly with `n`.
- The base case for the recursion is when the length of the current combination equals `2*n`, at which point it is added to the result list.
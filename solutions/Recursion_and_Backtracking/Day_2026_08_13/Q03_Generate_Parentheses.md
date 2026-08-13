# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parentheses combination is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, given `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`. The input `n` will be in the range `[1, 8]`.

## Approach
The solution utilizes a recursive backtracking approach to generate all possible combinations of well-formed parentheses. It ensures that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses. This guarantees that every combination is well-formed.

## Complexity
- Time: O(4^n / n^(3/2))
- Space: O(4^n / n^(3/2))

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
Input: n = 1
Output: ["()"]
```

## Key Takeaways
- Use recursive backtracking to generate all possible combinations of well-formed parentheses.
- Ensure that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.
- Utilize a helper function `backtrack` to explore all possible combinations recursively.
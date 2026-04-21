# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number of pairs. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, given the number of pairs as 3, the output should include all possible combinations of 3 pairs of well-formed parentheses, such as "(())()", "(()())", "(())()", etc. The input is an integer representing the number of pairs of parentheses, and the output is a list of all possible combinations of well-formed parentheses.

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible combinations. The algorithm starts with an empty string and adds open and close parentheses recursively, ensuring that the combination remains well-formed at each step.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers which represent the number of binary trees with n internal nodes, or the number of well-formed parentheses sequences of length 2n.
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack.

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
        // if the length of the current string is equal to 2 * max, add it to the result
        if (current.length() == 2 * max) {
            result.push_back(current);
            return;
        }
        
        // add an open parenthesis if the number of open parentheses is less than max
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }
        
        // add a close parenthesis if the number of close parentheses is less than the number of open parentheses
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
};
```

## Test Cases
```
Input: 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible combinations of well-formed parentheses.
- Ensuring the combination remains well-formed at each step is crucial to avoid invalid combinations.
- The time and space complexity of the solution are dependent on the number of pairs of parentheses.
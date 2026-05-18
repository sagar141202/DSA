# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number of pairs. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. The input is an integer `n`, representing the number of pairs of parentheses, and the output is a list of all possible well-formed combinations of `n` pairs of parentheses. For example, given `n = 3`, the output should include combinations like `"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`.

## Approach
This problem can be solved using recursion and backtracking, where we build the combinations by adding open and close parentheses one at a time, ensuring that the combination remains well-formed at each step. We use a recursive function to explore all possible combinations.

## Complexity
- Time: O(4^n / n^(3/2))
- Space: O(4^n / n^(3/2))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }
    
    void backtrack(vector<string>& result, string s, int open, int close, int max) {
        if (s.length() == max * 2) {
            result.push_back(s);
            return;
        }
        
        if (open < max) {
            backtrack(result, s + "(", open + 1, close, max);
        }
        if (close < open) {
            backtrack(result, s + ")", open, close + 1, max);
        }
    }
};

int main() {
    Solution solution;
    int n = 3;
    vector<string> result = solution.generateParenthesis(n);
    for (const auto& combination : result) {
        cout << combination << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## Key Takeaways
- The use of recursion and backtracking allows for the systematic exploration of all possible combinations of parentheses.
- Ensuring that the number of close parentheses never exceeds the number of open parentheses guarantees well-formed combinations.
- The base case for the recursion is when the length of the current combination equals `2 * n`, at which point the combination is added to the result list.
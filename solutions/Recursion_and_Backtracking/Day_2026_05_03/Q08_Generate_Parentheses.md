# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed combination of parentheses is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, if `n = 3`, the output should include combinations like `((()))`, `(()())`, `(())()`, `()(())`, `()()()`. The constraints are `1 <= n <= 20`, and the output should not contain any invalid combinations.

## Approach
The approach involves using recursion and backtracking to generate all possible combinations of well-formed parentheses. The algorithm starts with an empty string and adds open and close parentheses recursively, ensuring that the number of close parentheses never exceeds the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
- Space: O(4^n / n^(3/2)) for storing the generated combinations

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
    
    void backtrack(vector<string>& result, string current, int open, int close, int max) {
        // base case: when the length of the current string is equal to 2 * max
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
((()))
(()())
(())()
()(())
()()()
```

## Key Takeaways
- The problem can be solved using recursion and backtracking.
- The base case for the recursion is when the length of the current string is equal to 2 * n.
- The algorithm ensures that the number of close parentheses never exceeds the number of open parentheses.
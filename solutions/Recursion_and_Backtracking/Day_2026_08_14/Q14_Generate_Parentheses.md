# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed parenthesis is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of all possible combinations of well-formed parentheses. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible combinations of parentheses by adding open and close parentheses one by one, and backtrack when the combination is not well-formed. The base case for the recursion is when the length of the current combination is equal to `2n`.

## Complexity
- Time: O(4^n / n^(3/2)) due to the Catalan number formula
- Space: O(4^n / n^(3/2)) for storing the result

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
    
    void backtrack(vector<string>& result, string current, int open, int close, int n) {
        // base case: when the length of the current combination is equal to 2n
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        // add open parenthesis if possible
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
        // add close parenthesis if possible
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, n);
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
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- The base case for the recursion is when the length of the current combination is equal to `2n`.
- Add open and close parentheses one by one, and backtrack when the combination is not well-formed.
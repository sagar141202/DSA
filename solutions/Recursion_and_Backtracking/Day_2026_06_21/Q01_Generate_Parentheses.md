# Generate Parentheses

## Problem Statement
The problem requires generating all possible combinations of well-formed parentheses for a given number `n`. A well-formed parenthesis is one where every open parenthesis can be matched with a corresponding close parenthesis. The constraints are that the input `n` will be a positive integer, and the output should be a list of strings, each representing a combination of well-formed parentheses. For example, if `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will start with an empty string and add open and close parentheses recursively, ensuring that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses. This will guarantee that the generated parentheses are well-formed.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
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
    
    void backtrack(vector<string>& result, string current, int open, int close, int max) {
        // base case: if the length of the current string is equal to 2 * max, add it to the result
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
    for (const auto& str : result) {
        cout << str << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Input: n = 1
Output: ["()"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of well-formed parentheses.
- Ensure that the number of open parentheses never exceeds `n` and the number of close parentheses never exceeds the number of open parentheses.
- The time and space complexity of the solution is related to the Catalan numbers, which represent the number of binary trees with `n` internal nodes.
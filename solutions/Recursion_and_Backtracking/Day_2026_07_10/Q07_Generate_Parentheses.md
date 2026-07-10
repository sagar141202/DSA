# Generate Parentheses

## Problem Statement
Given an integer `n`, generate all possible combinations of well-formed parentheses. A well-formed parenthesis is one where every open parenthesis can be matched with a corresponding close parenthesis. For example, given `n = 3`, the output should be `["((()))","(()())","(())()","()(())","()()()"]`. The input `n` will be a positive integer, and the output should be a list of strings representing all possible combinations of well-formed parentheses.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible combinations of parentheses by adding an open parenthesis if the number of open parentheses is less than `n`, and adding a close parenthesis if the number of close parentheses is less than the number of open parentheses.

## Complexity
- Time: O(4^n / n^(3/2)) due to the nature of Catalan numbers
- Space: O(4^n / n^(3/2)) for storing the result, and O(n) for the recursion stack

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
        // if the length of the current string is equal to 2n, add it to the result
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        
        // add an open parenthesis if the number of open parentheses is less than n
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }
        
        // add a close parenthesis if the number of close parentheses is less than the number of open parentheses
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, n);
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
- The base case for the recursion is when the length of the current string is equal to 2n.
- The time complexity of the solution is O(4^n / n^(3/2)) due to the nature of Catalan numbers.
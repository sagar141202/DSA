# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The string `s` contains digits, `'+', '-', '*', '/'` operators, and spaces. The expression is evaluated from left to right, ignoring the order of operations. For example, `3+2*2` is evaluated as `(3+(2*2)) = 7`, not as `((3+2)*2) = 10`. Assume that the input expression is always valid and does not contain any division by zero.

## Approach
We use a stack to store the intermediate results and operators. We iterate through the string, and for each digit, we calculate the current number. If the current operator is `'*'` or `'/'`, we calculate the result immediately. If the current operator is `'+'` or `'-'`, we push the current number and operator into the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> stack;
        int currNum = 0;
        char operation = '+';
        for (int i = 0; i < s.length(); i++) {
            // calculate current number
            if (isdigit(s[i])) {
                currNum = currNum * 10 + s[i] - '0';
            }
            // if we encounter an operator or reach the end of the string
            if ((s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') || i == s.length() - 1) {
                if (operation == '+') {
                    stack.push(currNum);
                } else if (operation == '-') {
                    stack.push(-currNum);
                } else if (operation == '*') {
                    int top = stack.top();
                    stack.pop();
                    stack.push(top * currNum);
                } else if (operation == '/') {
                    int top = stack.top();
                    stack.pop();
                    stack.push(top / currNum);
                }
                operation = s[i];
                currNum = 0;
            }
        }
        int result = 0;
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        return result;
    }
};
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- Use a stack to store intermediate results and operators.
- Calculate the result immediately for `'*'` and `'/'` operators.
- Push the current number and operator into the stack for `'+'` and `'-'` operators.
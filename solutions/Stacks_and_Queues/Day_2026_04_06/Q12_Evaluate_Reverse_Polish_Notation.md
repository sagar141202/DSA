# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The output should be the result of the expression. For example, the input ["2", "1", "+", "3", "*"] represents the expression (2 + 1) * 3, which equals 9. The input ["4", "13", "5", "/", "+"] represents the expression 4 + (13 / 5), which equals 6.

## Approach
The algorithm uses a stack to store the operands. When an operator is encountered, the top two operands are popped from the stack, the operation is performed, and the result is pushed back onto the stack. The final result is the only element left in the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = stk.top(); stk.pop();
                int a = stk.top(); stk.pop();
                if (token == "+") stk.push(a + b);
                else if (token == "-") stk.push(a - b);
                else if (token == "*") stk.push(a * b);
                else stk.push(a / b);
            } else {
                stk.push(stoi(token));
            }
        }
        return stk.top();
    }
};
```

## Test Cases
```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Input: ["4", "13", "5", "/", "+"]
Output: 6
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

## Key Takeaways
- Use a stack to store operands and intermediate results.
- Handle operators by popping the top two operands, performing the operation, and pushing the result back onto the stack.
- The final result is the only element left in the stack after processing all tokens.
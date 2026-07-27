# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The output should be the result of the expression. For example, the input ["2", "1", "+", "3", "*"] represents the expression (2 + 1) * 3, which equals 9. The input is guaranteed to be valid and will not cause division by zero.

## Approach
We use a stack-based approach to solve this problem. When we encounter an operand, we push it to the stack. When we encounter an operator, we pop two operands from the stack, apply the operation, and push the result back to the stack. The final result will be the only element left in the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> stack;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();
                if (token == "+") {
                    stack.push(a + b);
                } else if (token == "-") {
                    stack.push(a - b);
                } else if (token == "*") {
                    stack.push(a * b);
                } else {
                    stack.push(a / b);
                }
            } else {
                stack.push(std::stoi(token));
            }
        }
        return stack.top();
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
- Handle operators by popping two operands, applying the operation, and pushing the result.
- The final result will be the only element left in the stack after processing all tokens.
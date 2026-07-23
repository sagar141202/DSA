# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings, where each string is either an operator or an operand. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] and the expression " 5 / (2 + 3)" can be represented as ["5", "2", "3", "+", "/"]. The constraints are that the input list is not empty and the expression is valid.

## Approach
We can use a stack to store the operands. When we encounter an operator, we pop the last two operands from the stack, apply the operation, and push the result back onto the stack. The final result will be the only element left in the stack. This approach takes advantage of the fact that Reverse Polish Notation is a prefix notation, where the operator follows its operands.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = s.top(); s.pop();
                int a = s.top(); s.pop();
                if (token == "+") s.push(a + b);
                else if (token == "-") s.push(a - b);
                else if (token == "*") s.push(a * b);
                else s.push(a / b);
            } else {
                s.push(stoi(token));
            }
        }
        return s.top();
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
- Use a stack to store operands in Reverse Polish Notation.
- When encountering an operator, apply the operation to the top two operands and push the result back onto the stack.
- The final result is the only element left in the stack after processing all tokens.
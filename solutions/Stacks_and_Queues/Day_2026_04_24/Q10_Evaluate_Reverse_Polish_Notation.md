# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] and the expression " 10 MUL 2 DIV 3 SUB 11 ADD 4 DIV" can be represented as ["10", "2", "MUL", "3", "SUB", "11", "ADD", "4", "DIV"]. The output should be the result of the expression. Assume that the input is valid and does not contain division by zero.

## Approach
We can use a stack to store the operands. When we encounter an operator, we pop two operands from the stack, apply the operation, and push the result back to the stack. The final result will be the only element left in the stack. This approach takes advantage of the properties of Reverse Polish Notation, where operators follow their operands.

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
        stack<int> st;
        for (const auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b);
            } else {
                st.push(stoi(token));
            }
        }
        return st.top();
    }
};
```

## Test Cases
```
Input: ["2","1","+","3","*"]
Output: 9
Input: ["4","13","5","/","+"]
Output: 6
Input: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Key Takeaways
- Use a stack to store the operands in Reverse Polish Notation.
- When an operator is encountered, pop two operands from the stack, apply the operation, and push the result back to the stack.
- The final result will be the only element left in the stack after processing all tokens.
# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the RPN expression. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] and the expression " 10 MUL 2 DIV 3 SUB 11 ADD 4 MUL 12 SUB" can be represented as ["10", "2", "MUL", "3", "SUB", "11", "ADD", "4", "MUL", "12", "SUB"]. The constraints are that the input expression is valid and the division is integer division.

## Approach
We use a stack to store the intermediate results. We iterate through the input tokens. If the token is a number, we push it to the stack. If the token is an operator, we pop two numbers from the stack, apply the operation, and push the result back to the stack.

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
- Using a stack to store intermediate results is a common approach for evaluating postfix expressions.
- Be careful when handling division to avoid precision loss.
- The time complexity is linear because we process each token exactly once.
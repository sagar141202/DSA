# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] and the expression " 5 / ( 3 + 2 ) " can be represented as ["5", "3", "2", "+", "/"]. The constraints are that the input expression is guaranteed to be valid and the output will always be an integer.

## Approach
The algorithm uses a stack to store the intermediate results. It iterates over the input expression, pushing operands onto the stack and popping them when encountering an operator to compute the result. The result is then pushed back onto the stack. This process continues until all tokens have been processed, at which point the stack contains a single element, the final result.

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
        for (const string& token : tokens) {
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
- Use a stack to store intermediate results in Reverse Polish Notation.
- When an operator is encountered, pop two operands from the stack, apply the operation, and push the result back onto the stack.
- At the end of processing, the stack will contain a single element, which is the final result of the expression.
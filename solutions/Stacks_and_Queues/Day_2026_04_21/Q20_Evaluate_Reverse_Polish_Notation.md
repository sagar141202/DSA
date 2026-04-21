# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings where each string is either an operator or an operand. The expression is guaranteed to be valid, and every operand is a non-negative integer. For example, the expression ["2", "1", "+", "3", "*"] is equivalent to (2 + 1) * 3, and the expression ["4", "13", "5", "/", "+"] is equivalent to 4 + (13 / 5). The constraints are 1 <= tokens.length <= 10^4, tokens[i] is either an operator (+, -, *, /) or an operand (a non-negative integer), and the division operator '/' only appears if the second operand is non-zero.

## Approach
We will use a stack-based approach to solve this problem. We iterate over each token in the input list. If the token is an operand, we push it onto the stack. If the token is an operator, we pop two operands from the stack, apply the operation, and push the result back onto the stack. The final result is the only element left in the stack.

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
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
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
- Use a stack to store operands and intermediate results
- Iterate over each token in the input list and apply the corresponding operation
- Handle division by zero by ensuring the second operand is non-zero before division
- The final result is the only element left in the stack after processing all tokens
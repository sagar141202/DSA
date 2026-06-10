# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The output should be the result of the expression. For example, the input ["2", "1", "+", "3", "*"] represents the expression (2 + 1) * 3, and the output should be 9. The input ["4", "13", "5", "/", "+"] represents the expression 4 + (13 / 5), and the output should be 6.

## Approach
We will use a stack-based approach to solve this problem. The idea is to iterate through the input list and whenever we encounter an operand, we push it to the stack. When we encounter an operator, we pop two operands from the stack, apply the operation, and push the result back to the stack.

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
Input: ["2", "1", "+", "3", "*"]
Output: 9
Input: ["4", "13", "5", "/", "+"]
Output: 6
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

## Key Takeaways
- Use a stack to store the operands and intermediate results.
- Iterate through the input list and apply the operators to the top two elements of the stack.
- Handle the division operator carefully to avoid integer division by zero.
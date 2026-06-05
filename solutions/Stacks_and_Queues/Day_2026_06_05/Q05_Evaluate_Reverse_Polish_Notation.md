# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The output should be the result of the expression evaluation. Constraints: 1 <= tokens.length <= 10^4, tokens[i] is either an operator or an operand, operands are in the range [-10^9, 10^9], division is integer division (i.e., round toward zero). Examples: Input: ["2","1","+","3","*"] Output: 9, Input: ["4","13","5","/","+"] Output: 6.

## Approach
The approach is to use a stack to store the operands and then pop them when an operator is encountered. The popped operands are then used to calculate the result based on the operator. This result is then pushed back onto the stack. The final result will be the only element left in the stack.

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
                else st.push(a / b); // integer division
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
- Use a stack to store operands and intermediate results.
- When an operator is encountered, pop the required operands from the stack, perform the operation, and push the result back onto the stack.
- Be careful with the order of operations when using a stack, as it is a LIFO (Last In First Out) data structure.
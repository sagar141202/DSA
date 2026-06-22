# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The expression is guaranteed to be valid, and every operand and operator is separated by a space. For example, the expression "3 4 +" is equivalent to the expression "3 + 4". The expression "3 4 + 2 *" is equivalent to the expression "(3 + 4) * 2". The input expression will not contain any spaces other than those separating the operands and operators. The division operator "/" will always be integer division, and the result of the division will always be an integer.

## Approach
We will use a stack data structure to store the operands and then pop them when an operator is encountered. We will then apply the operator to the popped operands and push the result back onto the stack. This process will continue until all tokens have been processed, at which point the stack will contain a single element, the result of the expression.

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
                if (token == "+") {
                    st.push(a + b);
                } else if (token == "-") {
                    st.push(a - b);
                } else if (token == "*") {
                    st.push(a * b);
                } else {
                    st.push(a / b);
                }
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
- Use a stack to store operands and pop them when an operator is encountered.
- Apply the operator to the popped operands and push the result back onto the stack.
- The final result will be the only element left in the stack after processing all tokens.
# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. For example, the input ["2", "1", "+", "3", "*"] represents the expression (2 + 1) * 3. The input will not contain any division by zero. The input will not contain any invalid notation.

## Approach
The algorithm uses a stack to store the intermediate results. It iterates over the input tokens, pushing operands to the stack and popping the required number of operands when it encounters an operator. The result of the operation is then pushed back to the stack. The final result is the only element left in the stack.

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
            // Check if the token is an operator
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                // Pop two operands from the stack
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                // Perform the operation and push the result back to the stack
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b);
            } else {
                // The token is an operand, convert it to an integer and push it to the stack
                st.push(stoi(token));
            }
        }
        // The final result is the only element left in the stack
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
- Use a stack to store the intermediate results in Reverse Polish Notation.
- Iterate over the input tokens, pushing operands to the stack and popping the required number of operands when encountering an operator.
- The final result is the only element left in the stack.
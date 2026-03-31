# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the tokens in the expression. The output should be the result of the evaluated expression. For example, given the input ["2", "1", "+", "3", "*"], the output should be 9, as the expression is equivalent to (2 + 1) * 3. The input expression is guaranteed to be valid.

## Approach
The approach is to use a stack to store the operands and pop them when an operator is encountered. The algorithm processes each token in the input list, pushing operands to the stack and applying operators to the top two elements on the stack. The final result is the only element left on the stack.

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
- Use a stack to store operands and pop them when an operator is encountered.
- Process each token in the input list, applying operators to the top two elements on the stack.
- The final result is the only element left on the stack.
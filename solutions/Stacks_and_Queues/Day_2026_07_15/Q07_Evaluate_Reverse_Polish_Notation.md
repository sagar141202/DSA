# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. Note that division operator / computes integer division. The input array is guaranteed to be a valid Reverse Polish Notation expression. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] and the expression " 10 MUL 2 DIV 3 SUB 11 ADD 4 DIV" can be represented as ["10", "2", "MUL", "3", "SUB", "11", "ADD", "4", "DIV"]. The constraints are 1 <= tokens.length <= 10^4, tokens[i] is either an operator (+, -, *, /) or an integer (-2^31 <= tokens[i] <= 2^31 - 1).

## Approach
We can solve this problem using a stack data structure, where we iterate over the tokens array and push the operands to the stack. When we encounter an operator, we pop two elements from the stack, apply the operation, and push the result back to the stack. The final result will be the only element left in the stack.

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
Input: tokens = ["2","1","+","3","*"]
Output: 9
Input: tokens = ["4","13","5","/","+"]
Output: 6
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Key Takeaways
- We use a stack to store the intermediate results.
- We iterate over the tokens array and apply the operations accordingly.
- The final result is the only element left in the stack.
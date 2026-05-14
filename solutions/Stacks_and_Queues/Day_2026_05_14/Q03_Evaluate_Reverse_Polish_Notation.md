# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"] in Reverse Polish Notation. The expression should be evaluated and the result should be returned. If there are multiple operators with the same precedence, they should be evaluated from left to right.

## Approach
We will use a stack to store the operands. When we encounter an operator, we will pop two operands from the stack, apply the operator, and push the result back onto the stack. This process will be repeated until all tokens have been processed.

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

int main() {
    Solution solution;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << solution.evalRPN(tokens) << endl;
    return 0;
}
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
- Use a stack to store operands in Reverse Polish Notation.
- When encountering an operator, pop two operands from the stack, apply the operator, and push the result back onto the stack.
- Repeat the process until all tokens have been processed.
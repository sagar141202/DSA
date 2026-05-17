# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression. For example, the expression "3+4*2" can be represented as ["3", "+", "4", "*", "2"] but in Reverse Polish Notation, it would be ["2", "4", "*", "+", "3"]. The division should truncate toward zero. You may assume that the input is valid.

## Approach
The algorithm uses a stack to store the intermediate results. It iterates over each token in the expression, pushing operands onto the stack and popping the required operands when an operator is encountered. The result of the operation is then pushed back onto the stack.

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
            // Check if the token is an operator
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b); // integer division
            } else {
                // Token is an operand, push it onto the stack
                st.push(stoi(token));
            }
        }
        return st.top();
    }
};

int main() {
    Solution solution;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << solution.evalRPN(tokens) << endl;  // Output: 9
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
- Use a stack to store intermediate results.
- Iterate over the tokens in the Reverse Polish Notation expression.
- When encountering an operand, push it onto the stack.
- When encountering an operator, pop the required operands, perform the operation, and push the result back onto the stack.
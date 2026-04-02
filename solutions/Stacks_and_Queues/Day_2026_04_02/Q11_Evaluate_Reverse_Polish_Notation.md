# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the tokens in the expression. The output should be the result of the evaluated expression. For example, the input ["2", "1", "+", "3", "*"] represents the expression (2 + 1) * 3, which equals 9. Constraints: 1 <= tokens.length <= 10^4, tokens[i] is either an operator or an operand, 0 <= operand <= 10^9.

## Approach
The algorithm uses a stack to store operands. When an operator is encountered, the top two operands are popped, the operation is applied, and the result is pushed back onto the stack. This process continues until all tokens have been processed, at which point the stack contains a single element, the result of the expression.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <string>
#include <vector>

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
- Use a stack to store operands and apply operators to the top two elements.
- Handle division carefully to avoid integer division issues.
- Ensure the stack is properly updated after each operation to maintain the correct order of operations.
# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The expression is guaranteed to be valid, and there will not be any division by zero. For example, the expression ["2", "1", "+", "3", "*"] evaluates to (2 + 1) * 3 = 9.

## Approach
We can use a stack to store the intermediate results. When we encounter an operand, we push it onto the stack. When we encounter an operator, we pop two operands from the stack, apply the operation, and push the result back onto the stack.

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
- Use a stack to store intermediate results when evaluating Reverse Polish Notation.
- When encountering an operand, push it onto the stack.
- When encountering an operator, pop two operands from the stack, apply the operation, and push the result back onto the stack.
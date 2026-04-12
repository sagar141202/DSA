# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings, where each string represents either an operand or an operator. The division operator must perform integer division, which truncates toward zero. You may assume that the input expression is always valid. For example, the expression ["2", "1", "+", "3", "*"] is equal to (2 + 1) * 3 = 9.

## Approach
We will use a stack data structure to solve this problem. We iterate over the input list, pushing operands onto the stack and popping the top two elements when we encounter an operator, applying the operation and pushing the result back onto the stack.

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
Input: ["2","1","+","3","*"]
Output: 9
Input: ["4","13","5","/","+"]
Output: 6
Input: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

## Key Takeaways
- Use a stack to store operands and intermediate results.
- Iterate over the input list, applying operators and pushing results back onto the stack.
- The final result is the only element left on the stack after processing the entire input list.
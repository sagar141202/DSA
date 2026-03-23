# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The expression is guaranteed to be valid, and there will not be any division by zero. For example, the expression ["2", "1", "+", "3", "*"] evaluates to (2 + 1) * 3 = 9.

## Approach
We will use a stack-based approach to solve this problem, iterating over the expression and pushing operands onto the stack, then popping them off and applying operators when encountered. The result of each operation is then pushed back onto the stack.

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
        // Create a stack to hold the intermediate results
        stack<int> st;
        
        // Define the operators
        set<string> operators = {"+", "-", "*", "/"};
        
        // Iterate over each token in the expression
        for (string token : tokens) {
            // Check if the token is an operator
            if (operators.count(token)) {
                // Pop the top two elements off the stack
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                
                // Apply the operator and push the result back onto the stack
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b);
            } else {
                // The token is an operand, so convert it to an integer and push it onto the stack
                st.push(stoi(token));
            }
        }
        
        // The final result is the only element left on the stack
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
- Use a stack to hold intermediate results when evaluating postfix expressions.
- Be sure to handle the operator precedence correctly by applying operators immediately when encountered.
- Consider using a set to store the operators for efficient lookups.
# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the expression in Reverse Polish Notation. The expression is guaranteed to be valid, and there will not be any division by zero. For example, the expression "3+4*2" can be represented as ["3", "4", "2", "*", "+"].

## Approach
We can use a stack to store the operands and then pop them when an operator is encountered. The result of the operation is then pushed back onto the stack. This process continues until all elements in the input list have been processed. The final result will be the only element left in the stack.

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
        // Create a stack to store the operands
        stack<int> st;
        
        // Iterate over each token in the input list
        for (const string& token : tokens) {
            // If the token is an operator, pop two operands, perform the operation, and push the result
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int operand2 = st.top();
                st.pop();
                int operand1 = st.top();
                st.pop();
                int result;
                if (token == "+") {
                    result = operand1 + operand2;
                } else if (token == "-") {
                    result = operand1 - operand2;
                } else if (token == "*") {
                    result = operand1 * operand2;
                } else {
                    result = operand1 / operand2;
                }
                st.push(result);
            } 
            // If the token is an operand, convert it to an integer and push it onto the stack
            else {
                st.push(stoi(token));
            }
        }
        
        // The final result will be the only element left in the stack
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
- Use a stack to store the operands and intermediate results.
- Process each token in the input list, performing operations and pushing results onto the stack as needed.
- The final result will be the only element left in the stack after processing all tokens.
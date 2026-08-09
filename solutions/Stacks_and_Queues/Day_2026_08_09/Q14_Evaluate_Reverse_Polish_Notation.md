# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings representing the tokens in the expression. The output should be the result of the expression. For example, given the input ["2", "1", "+", "3", "*"], the output should be 9, because ((2 + 1) * 3) = 9. The input array will not contain empty strings and will not contain more than one operator in a row. The input will not contain division by zero.

## Approach
We can use a stack to store the operands and then pop them when we encounter an operator. We then apply the operator to the popped operands and push the result back onto the stack. This process continues until we have processed all tokens.

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
        for (string token : tokens) {
            // if token is a number, convert it to int and push to stack
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                st.push(stoi(token));
            } else {
                // pop two numbers from stack, apply operation, and push result
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b);
            }
        }
        return st.top();
    }
};

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
- Use a stack to store operands and apply operators when encountered
- Be careful with the order of operations and the conversion of strings to integers
- Consider edge cases such as division by zero and invalid input tokens
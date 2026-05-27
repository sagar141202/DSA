# Evaluate Reverse Polish Notation

## Problem Statement
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. The input is a list of strings, where each string is either an integer or an operator. The division operator / always rounds down to the nearest integer. For example, "3/2" = 1 and "-3/2" = -2. It is guaranteed that the input is valid and does not contain any division by zero. The input array does not contain any empty strings.

## Approach
We will use a stack to store the intermediate results. When we encounter an operator, we pop two elements from the stack, apply the operation, and push the result back onto the stack. This approach allows us to efficiently evaluate the expression in Reverse Polish Notation.

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
        for (const string& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                if (token == "+") st.push(a + b);
                else if (token == "-") st.push(a - b);
                else if (token == "*") st.push(a * b);
                else st.push(a / b); // Note: In C++, the / operator performs integer division when both operands are integers
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
- Use a stack to store intermediate results when evaluating expressions in Reverse Polish Notation.
- Be mindful of the order of operations when encountering operators in the input.
- The / operator in C++ performs integer division when both operands are integers, which matches the problem requirements.